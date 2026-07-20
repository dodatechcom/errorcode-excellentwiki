---
title: "[Solution] PHP REDIS_CONNECTION_ERROR — Redis Connect Failed"
description: "Fix PHP Redis::connect() / Redis::pconnect() failed. Connection refused or timeout errors with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 105
---

# PHP REDIS_CONNECTION_ERROR — Redis Connect Failed

The `Redis::connect()` or `Redis::pconnect()` call failed because the Redis server is unreachable, the host/port is wrong, or a timeout occurred. This is one of the most common PHP Redis errors and typically indicates a configuration or infrastructure issue rather than a code bug.

## Common Causes

### Connection refused — Redis server is not running

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
// PHP Fatal error: Uncaught RedisException: Connection refused
?>
```

### Wrong host or port configuration

```php
<?php
$redis = new Redis();
$redis->connect('wrong-host.local', 6379);
// RedisException: Can't connect to wrong-host.local:6379
?>
```

### Default timeout too low for slow networks

```php
<?php
$redis = new Redis();
$redis->connect('10.0.0.5', 6379); // default timeout 0 — may hang
$redis->connect('10.0.0.5', 6379, 0.5); // 0.5s timeout — may be too short
?>
```

### Firewall blocking Redis port

```php
<?php
$redis = new Redis();
$redis->connect('192.168.1.100', 6379);
// RedisException: Connection refused — port blocked by firewall
?>
```

### Persistent connection reuse after server restart

```php
<?php
$redis = new Redis();
$redis->pconnect('127.0.0.1', 6379); // stale persistent connection
// RedisException: Connection closed
?>
```

## How to Fix

### Fix 1: Verify Redis Server Is Running

Check that the Redis service is active before attempting to connect.

```php
<?php
function getRedisConnection(): Redis
{
    $redis = new Redis();
    try {
        $redis->connect('127.0.0.1', 6379, 2.0);
        $redis->ping(); // +PONG
        return $redis;
    } catch (RedisException $e) {
        error_log('Redis connection failed: ' . $e->getMessage());
        throw $e;
    }
}
?>
```

### Fix 2: Increase Connection Timeout

Set a generous timeout to handle slow or distant Redis servers.

```php
<?php
$redis = new Redis();
$redis->connect('redis.example.com', 6379, 5.0); // 5 second timeout
$redis->setOption(Redis::OPT_READ_TIMEOUT, 10);   // 10s read timeout
?>
```

### Fix 3: Use Persistent Connections with Retry

Use `pconnect()` for long-running processes and add retry logic.

```php
<?php
function getPersistentRedis(): Redis
{
    $redis = new Redis();
    $host = '127.0.0.1';
    $port = 6379;
    $timeout = 2.0;
    $retryInterval = 100;
    $readTimeout = 0;

    $connected = $redis->pconnect($host, $port, $timeout, 'persistent_id_1', $retryInterval, $readTimeout);
    if (!$connected) {
        throw new RuntimeException('Cannot connect to Redis at ' . $host . ':' . $port);
    }
    return $redis;
}
?>
```

### Fix 4: Check Firewall and Redis Bind Configuration

Ensure Redis listens on the correct interface and the firewall allows traffic.

```bash
# Redis config — bind to all interfaces (or specific IP)
# /etc/redis/redis.conf
bind 0.0.0.0

# Verify Redis is listening
ss -tlnp | grep 6379

# Test connectivity
redis-cli -h <host> -p 6379 ping
```

### Fix 5: Configure Connection with Error Handling

Wrap all connection attempts in a try-catch with proper logging.

```php
<?php
class RedisConnectionFactory
{
    private string $host;
    private int $port;
    private float $timeout;

    public function __construct(string $host, int $port = 6379, float $timeout = 3.0)
    {
        $this->host = $host;
        $this->port = $port;
        $this->timeout = $timeout;
    }

    public function create(): Redis
    {
        $redis = new Redis();
        $redis->setOption(Redis::OPT_RETRY, true);
        $redis->setOption(Redis::OPT_BACKOFF_FUNCTION, function ($retries) {
            return min(1000 * (2 ** $retries), 10000);
        });

        try {
            $redis->connect($this->host, $this->port, $this->timeout);
            $redis->ping();
        } catch (RedisException $e) {
            error_log(sprintf(
                'Redis connection to %s:%d failed: %s',
                $this->host,
                $this->port,
                $e->getMessage()
            ));
            throw $e;
        }

        return $redis;
    }
}
?>
```

## Examples

### Health Check Script

```php
<?php
function redisHealthCheck(string $host, int $port): array
{
    $redis = new Redis();
    $start = microtime(true);

    try {
        $redis->connect($host, $port, 3.0);
        $latency = round((microtime(true) - $start) * 1000, 2);
        $info = $redis->info('server');

        return [
            'status'   => 'healthy',
            'latency'  => $latency . 'ms',
            'version'  => $info['redis_version'] ?? 'unknown',
            'uptime'   => $info['uptime_in_seconds'] ?? 0,
        ];
    } catch (RedisException $e) {
        return [
            'status'  => 'unhealthy',
            'error'   => $e->getMessage(),
        ];
    }
}

$result = redisHealthCheck('127.0.0.1', 6379);
print_r($result);
?>
```

### Laravel Redis Configuration

```php
<?php
// config/database.php
'redis' => [
    'client' => env('REDIS_CLIENT', 'phpredis'),
    'default' => [
        'url' => env('REDIS_URL'),
        'host' => env('REDIS_HOST', '127.0.0.1'),
        'username' => env('REDIS_USERNAME'),
        'password' => env('REDIS_PASSWORD'),
        'port' => env('REDIS_PORT', '6379'),
        'database' => env('REDIS_DB', '0'),
        'timeout' => env('REDIS_TIMEOUT', 3.0),
        'read_timeout' => env('REDIS_READ_TIMEOUT', 0),
        'persistent_id' => env('REDIS_PERSISTENT_ID'),
    ],
],
?>
```

## Related Errors

- [Redis Auth Error]({{< relref "/languages/php/redis-auth-error" >}})
- [Redis Timeout Error]({{< relref "/languages/php/redis-timeout-error" >}})
- [Redis Persistence Error]({{< relref "/languages/php/redis-persistence-error" >}})
