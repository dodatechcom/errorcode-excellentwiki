---
title: "[Solution] PHP MEMCACHED_CONNECTION_ERROR — Memcached Connect Failed"
description: "Fix PHP Memcached::addServer() failed and connection errors. Check server status, verify ports, and use consistent hashing."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 111
---

# PHP MEMCACHED_CONNECTION_ERROR — Memcached Connect Failed

The `Memcached::addServer()` or `Memcached::addServers()` call returns failure, or subsequent operations return `Memcached::RES_HOST_LOOKUP_FAILURE` / `Memcached::RES_CONNECTION_FAILURE`. The Memcached server is unreachable, the port is wrong, or the server is not running.

## Common Causes

### Memcached server not running

```php
<?php
$mc = new Memcached();
$mc->addServer('127.0.0.1', 11211);
$mc->set('key', 'value');
var_dump($mc->getResultCode()); // Memcached::RES_HOST_LOOKUP_FAILURE
?>
```

### Wrong port or host

```php
<?php
$mc = new Memcached();
$mc->addServer('wrong-host.local', 11211);
$mc->set('key', 'value');
var_dump($mc->getResultCode()); // Memcached::RES_UNKNOWN_READ_FAILURE
?>
```

### Firewall blocking port 11211

```php
<?php
$mc = new Memcached();
$mc->addServer('10.0.0.50', 11211);
$mc->set('key', 'value');
var_dump($mc->getResultMessage()); // "NOT CONNECTED"
?>
```

### Server rejected connection — max connections reached

```php
<?php
$mc = new Memcached();
$mc->addServer('memcached.prod.internal', 11211);
$mc->get('session_abc');
var_dump($mc->getResultCode()); // Memcached::RES_PROTOCOL_ERROR
?>
```

### Using hostname that doesn't resolve

```php
<?php
$mc = new Memcached();
$mc->addServer('memcached.internal', 11211);
// Hostname fails DNS resolution silently
var_dump($mc->getServerList()); // [] — no servers added
?>
```

## How to Fix

### Fix 1: Verify Server Is Running and Reachable

Check the Memcached server status before connecting.

```php
<?php
function checkMemcachedServer(string $host, int $port): bool
{
    $socket = @fsockopen($host, $port, $errno, $errstr, 3);
    if (!$socket) {
        error_log("Memcached unreachable at {$host}:{$port} — {$errstr}");
        return false;
    }
    fclose($socket);
    return true;
}

if (!checkMemcachedServer('127.0.0.1', 11211)) {
    throw new RuntimeException('Memcached server is not running');
}

$mc = new Memcached();
$mc->addServer('127.0.0.1', 11211);
?>
```

### Fix 2: Add Servers with Retry and Failure Limits

Configure failure limits so bad servers don't block the connection pool.

```php
<?php
$mc = new Memcached();
$mc->setOption(Memcached::OPT_RETRY_TIMEOUT, 5);
$mc->setOption(Memcached::OPT_SEND_TIMEOUT, 5000000);  // 5s in microseconds
$mc->setOption(Memcached::OPT_RECV_TIMEOUT, 5000000);
$mc->setOption(Memcached::OPT_SERVER_FAILURE_LIMIT, 3);

$mc->addServer('127.0.0.1', 11211);
$mc->addServer('10.0.0.50', 11211);

var_dump($mc->getServerList());
?>
```

### Fix 3: Use Consistent Hashing for Multi-Server Setup

Distribute keys across servers using consistent hashing for better reliability.

```php
<?php
$mc = new Memcached();
$mc->setOption(Memcached::OPT_DISTRIBUTION, Memcached::DISTRIBUTION_CONSISTENT);
$mc->setOption(Memcached::OPT_LIBKETAMA_COMPATIBLE, true);
$mc->setOption(Memcached::OPT_AUTO_EJECT_HOSTS, true);
$mc->setOption(Memcached::OPT_SERVER_FAILURE_LIMIT, 2);
$mc->setOption(Memcached::OPT_RETRY_TIMEOUT, 30);

$servers = [
    ['memcached-1.internal', 11211, 1],
    ['memcached-2.internal', 11211, 1],
    ['memcached-3.internal', 11211, 1],
];

$mc->addServers($servers);

// Verify server list
foreach ($mc->getServerList() as $server) {
    echo $server['host'] . ':' . $server['port'] . PHP_EOL;
}
?>
```

### Fix 4: Use Connection Pool with Health Checks

Create a connection manager that validates servers and handles failures.

```php
<?php
class MemcachedPool
{
    private array $instances = [];

    public function __construct(array $serverGroups)
    {
        foreach ($serverGroups as $group => $servers) {
            $mc = new Memcached($group);
            $mc->setOption(Memcached::OPT_RETRY_TIMEOUT, 5);
            $mc->setOption(Memcached::OPT_SERVER_FAILURE_LIMIT, 3);
            $mc->setOption(Memcached::OPT_AUTO_EJECT_HOSTS, true);
            $mc->addServers($servers);
            $this->instances[$group] = $mc;
        }
    }

    public function get(string $key, string $group = 'default'): mixed
    {
        if (!isset($this->instances[$group])) {
            throw new RuntimeException("No Memcached group: {$group}");
        }
        return $this->instances[$group]->get($key);
    }

    public function set(string $key, mixed $value, int $ttl = 3600, string $group = 'default'): bool
    {
        if (!isset($this->instances[$group])) {
            throw new RuntimeException("No Memcached group: {$group}");
        }
        return $this->instances[$group]->set($key, $value, $ttl);
    }

    public function getStatus(string $group = 'default'): array
    {
        $mc = $this->instances[$group] ?? null;
        if (!$mc) {
            return [];
        }
        return [
            'servers' => $mc->getServerList(),
            'status'  => $mc->getResultCode() === Memcached::RES_SUCCESS,
        ];
    }
}

$pool = new MemcachedPool([
    'default' => [
        ['127.0.0.1', 11211, 1],
    ],
]);

$pool->set('greeting', 'hello');
echo $pool->get('greeting');
?>
```

### Fix 5: Handle Connection Failures with Retry

Wrap Memcached operations with retry logic for transient failures.

```php
<?php
function memcachedWithRetry(Memcached $mc, string $method, mixed ...$args): mixed
{
    $maxRetries = 2;
    for ($attempt = 0; $attempt <= $maxRetries; $attempt++) {
        $result = $mc->{$method}(...$args);
        $code = $mc->getResultCode();

        if ($code === Memcached::RES_SUCCESS || $code === Memcached::RES_NOTFOUND) {
            return $result;
        }

        if ($attempt < $maxRetries) {
            $mc->flush();
            usleep(50000 * (2 ** $attempt)); // 50ms, 100ms
        }
    }

    error_log("Memcached {$method} failed after {$maxRetries} retries: " . $mc->getResultMessage());
    return false;
}

$mc = new Memcached();
$mc->addServer('127.0.0.1', 11211);

$value = memcachedWithRetry($mc, 'get', 'mykey');
?>
```

## Examples

### Server Discovery with DNS

```php
<?php
function discoverMemcachedServers(string $dnsName): array
{
    $ips = gethostbynameall($dnsName);
    $servers = [];
    foreach ($ips as $ip) {
        $servers[] = [$ip, 11211, 1];
    }
    return $servers;
}

$mc = new Memcached();
$servers = discoverMemcachedServers('memcached.internal.mycompany.com');
$mc->addServers($servers);

$mc->set('key', 'value');
echo $mc->get('key');
?>
```

## Related Errors

- [Memcached Get Error]({{< relref "/languages/php/memcached-get-error" >}})
- [Memcached Server Mark Bad]({{< relref "/languages/php/memcached-server-mark-bad" >}})
- [Redis Connection Error]({{< relref "/languages/php/redis-connection-error" >}})
