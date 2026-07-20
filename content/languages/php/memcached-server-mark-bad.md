---
title: "[Solution] PHP MEMCACHED_SERVER_MARK_BAD — Server Auto-Recovery Failed"
description: "Fix PHP Memcached auto-recovery and server marked as bad errors. Configure failure limits, handle recovery, and use SASL auth."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 113
---

# PHP MEMCACHED_SERVER_MARK_BAD — Server Auto-Recovery Failed

Memcached marks a server as "bad" (ejected from the pool) after repeated failures, then periodically tries to reconnect. If auto-recovery fails or is misconfigured, requests silently fail or return stale data. The `getServerList()` may show fewer servers than expected, and `getResultCode()` returns `Memcached::RES_NOTCONNECTED` or `Memcached::RES_SERVER_MARKED_DEAD`.

## Common Causes

### Auto-eject after too many failures

```php
<?php
$mc = new Memcached();
$mc->setOption(Memcached::OPT_AUTO_EJECT_HOSTS, true);
$mc->setOption(Memcached::OPT_SERVER_FAILURE_LIMIT, 3);
$mc->addServer('10.0.0.50', 11211);

// After 3 failures, server is ejected — subsequent calls skip it
$mc->set('key', 'value');
var_dump($mc->getServerList()); // server may be gone
?>
```

### Server recovered but pool not refreshed

```php
<?php
$mc = new Memcached();
$mc->addServer('10.0.0.50', 11211);

// Server went down, was ejected, then restarted
// Memcached client still thinks it's dead
$value = $mc->get('key');
var_dump($mc->getResultCode()); // Memcached::RES_NOTCONNECTED
?>
```

### Retry timeout too short or too long

```php
<?php
$mc = new Memcached();
$mc->setOption(Memcached::OPT_RETRY_TIMEOUT, 0); // retries instantly
$mc->setOption(Memcached::OPT_SERVER_FAILURE_LIMIT, 2);
$mc->addServer('unstable-server.internal', 11211);

// Server keeps failing — client spams reconnection attempts
$mc->get('key');
?>
```

### All servers ejected from pool

```php
<?php
$mc = new Memcached();
$mc->setOption(Memcached::OPT_AUTO_EJECT_HOSTS, true);
$mc->setOption(Memcached::OPT_SERVER_FAILURE_LIMIT, 1);
$mc->addServer('server1', 11211);
$mc->addServer('server2', 11211);

// Both servers hit failure limit — pool is empty
$mc->set('key', 'value');
var_dump($mc->getServerList()); // []
?>
```

### SASL authentication not configured

```php
<?php
$mc = new Memcached();
$mc->setOption(Memcached::OPT_BINARY_PROTOCOL, true);
$mc->addServer('secure-memcached.internal', 11211);

// Server requires SASL — no auth configured
$mc->get('key');
var_dump($mc->getResultCode()); // Memcached::RES_AUTH_FAILURE
?>
```

## How to Fix

### Fix 1: Configure Failure Limits and Retry Timeout

Set reasonable failure limits and retry intervals for production environments.

```php
<?php
$mc = new Memcached();
$mc->setOption(Memcached::OPT_AUTO_EJECT_HOSTS, true);
$mc->setOption(Memcached::OPT_SERVER_FAILURE_LIMIT, 5);
$mc->setOption(Memcached::OPT_RETRY_TIMEOUT, 30);       // 30 seconds
$mc->setOption(Memcached::OPT_SEND_TIMEOUT, 5000000);   // 5 seconds
$mc->setOption(Memcached::OPT_RECV_TIMEOUT, 5000000);

$mc->addServer('memcached-1.internal', 11211);
$mc->addServer('memcached-2.internal', 11211);
?>
```

### Fix 2: Implement Server Health Monitoring

Periodically check server health and re-add ejected servers.

```php
<?php
class MemcachedHealthMonitor
{
    private Memcached $mc;
    private array $originalServers;

    public function __construct(Memcached $mc)
    {
        $this->mc = $mc;
        $this->originalServers = $mc->getServerList();
    }

    public function checkAndRecover(): array
    {
        $current = $this->mc->getServerList();
        $currentHosts = array_map(fn($s) => $s['host'] . ':' . $s['port'], $current);
        $missing = [];

        foreach ($this->originalServers as $server) {
            $id = $server['host'] . ':' . $server['port'];
            if (!in_array($id, $currentHosts)) {
                $missing[] = $server;
            }
        }

        if (!empty($missing)) {
            error_log('Re-adding ' . count($missing) . ' ejected servers');

            // Create a fresh Memcached instance with all servers
            $fresh = new Memcached();
            $fresh->setOption(Memcached::OPT_RETRY_TIMEOUT, 30);
            $foreach ($this->originalServers as $server) {
                $fresh->addServer($server['host'], $server['port'], $server['weight']);
            }

            // Copy the persistent ID to reuse the same pool
            return ['recovered' => true, 'count' => count($missing)];
        }

        return ['recovered' => false, 'count' => 0];
    }

    public function getServerStatus(): array
    {
        $list = $this->mc->getServerList();
        $status = [];
        foreach ($list as $server) {
            $status[] = [
                'host' => $server['host'],
                'port' => $server['port'],
                'connected' => true,
            ];
        }
        return $status;
    }
}

$monitor = new MemcachedHealthMonitor($mc);
$status = $monitor->checkAndRecover();
?>
```

### Fix 3: Set Up SASL Authentication

Configure SASL for Memcached servers that require authentication.

```php
<?php
$mc = new Memcached();
$mc->setOption(Memcached::OPT_BINARY_PROTOCOL, true);

// Set SASL credentials
$mc->setSaslAuthData('username', 'password');

$mc->addServer('secure-memcached.internal', 11211);

$value = $mc->get('key');
$code = $mc->getResultCode();

if ($code === Memcached::RES_AUTH_FAILURE) {
    error_log('SASL authentication failed — check credentials');
} elseif ($code !== Memcached::RES_SUCCESS) {
    error_log('Memcached error: ' . $mc->getResultMessage());
}
?>
```

### Fix 4: Disable Auto-Eject for Critical Data

Keep servers in the pool even when failing to avoid data loss.

```php
<?php
$mc = new Memcached();
$mc->setOption(Memcached::OPT_AUTO_EJECT_HOSTS, false);
$mc->setOption(Memcached::OPT_SERVER_FAILURE_LIMIT, 0); // no ejection
$mc->setOption(Memcached::OPT_RETRY_TIMEOUT, 10);

$mc->addServer('critical-cache.internal', 11211);

// Server failures won't eject it — requests will retry
$value = $mc->get('important_key');
?>
```

### Fix 5: Use Persistent Connections with Connection Pooling

Use named persistent instances to maintain stable connections.

```php
<?php
function getMemcachedInstance(string $persistentId = 'default'): Memcached
{
    static $instances = [];

    if (!isset($instances[$persistentId])) {
        $mc = new Memcached($persistentId);
        $mc->setOption(Memcached::OPT_RETRY_TIMEOUT, 15);
        $mc->setOption(Memcached::OPT_SERVER_FAILURE_LIMIT, 5);
        $mc->setOption(Memcached::OPT_AUTO_EJECT_HOSTS, true);
        $mc->setOption(Memcached::OPT_LIBKETAMA_COMPATIBLE, true);
        $mc->setOption(Memcached::OPT_BINARY_PROTOCOL, true);

        $mc->addServers([
            ['memcached-1.internal', 11211, 1],
            ['memcached-2.internal', 11211, 1],
        ]);

        $instances[$persistentId] = $mc;
    }

    return $instances[$persistentId];
}

$cache = getMemcachedInstance('production');
$cache->set('session:abc', 'data', 3600);
?>
```

## Examples

### Monitoring Dashboard Data

```php
<?php
function memcachedClusterStatus(array $serverConfigs): array
{
    $statuses = [];

    foreach ($serverConfigs as $name => $config) {
        $mc = new Memcached();
        $mc->setOption(Memcached::OPT_RETRY_TIMEOUT, 5);
        $mc->addServer($config['host'], $config['port']);

        $start = microtime(true);
        $mc->set('__health_check__', '1', 10);
        $latency = round((microtime(true) - $start) * 1000, 2);
        $code = $mc->getResultCode();

        $statuses[$name] = [
            'host'     => $config['host'],
            'port'     => $config['port'],
            'healthy'  => $code === Memcached::RES_SUCCESS,
            'latency'  => $latency . 'ms',
            'code'     => $code,
            'message'  => $mc->getResultMessage(),
        ];
    }

    return $statuses;
}

$statuses = memcachedClusterStatus([
    'cache-1' => ['host' => '10.0.0.1', 'port' => 11211],
    'cache-2' => ['host' => '10.0.0.2', 'port' => 11211],
]);
print_r($statuses);
?>
```

### Automatic Server Pool Refresh

```php
<?php
class MemcachedPoolManager
{
    private Memcached $mc;
    private array $servers;
    private int $lastRefresh = 0;
    private int $refreshInterval = 60;

    public function __construct(array $servers)
    {
        $this->servers = $servers;
        $this->initializePool();
    }

    private function initializePool(): void
    {
        $this->mc = new Memcached();
        $this->mc->setOption(Memcached::OPT_RETRY_TIMEOUT, 15);
        $this->mc->setOption(Memcached::OPT_SERVER_FAILURE_LIMIT, 5);
        $this->mc->setOption(Memcached::OPT_AUTO_EJECT_HOSTS, true);
        $this->mc->addServers($this->servers);
        $this->lastRefresh = time();
    }

    public function getMc(): Memcached
    {
        if (time() - $this->lastRefresh > $this->refreshInterval) {
            $this->initializePool();
        }
        return $this->mc;
    }
}

$pool = new MemcachedPoolManager([
    ['memcached-1.internal', 11211, 1],
    ['memcached-2.internal', 11211, 1],
]);

$mc = $pool->getMc();
$mc->set('key', 'value');
?>
```

## Related Errors

- [Memcached Connection Error]({{< relref "/languages/php/memcached-connection-error" >}})
- [Memcached Get Error]({{< relref "/languages/php/memcached-get-error" >}})
- [Redis Connection Error]({{< relref "/languages/php/redis-connection-error" >}})
