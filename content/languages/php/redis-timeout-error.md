---
title: "[Solution] PHP REDIS_TIMEOUT_ERROR — Redis Read/Write Timeout"
description: "Fix PHP Redis read and write timeout errors. Increase timeouts, optimize network latency, and use persistent connections."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 108
---

# PHP REDIS_TIMEOUT_ERROR — Redis Read/Write Timeout

A Redis timeout occurs when a read or write operation does not complete within the configured time limit. The PHP Redis extension throws a `RedisException: read/write on ... timed out` error. This is different from a connection timeout — the connection was established but a command took too long to execute or return data.

## Common Causes

### Default read timeout too low

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
// default read timeout is 0 (infinite) in older versions
// or very low in newer versions — causes premature timeouts
$redis->get('large_key');
// RedisException: read error on connection
?>
```

### Slow command on large datasets

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379, 0, '', 0, 1.0); // 1s read timeout
$redis->keys('user:*'); // O(N) — slow on millions of keys
// RedisException: read error on connection
?>
```

### Network latency between PHP and Redis

```php
<?php
$redis = new Redis();
$redis->connect('10.0.0.200', 6379, 5.0, '', 0, 1.0);
// high latency makes the 1s read timeout too aggressive
$redis->get('mykey');
// RedisException: read error on connection
?>
```

### Server under memory pressure or busy

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->setOption(Redis::OPT_READ_TIMEOUT, 2);
// Redis is doing BGSAVE — blocks all commands
$redis->get('mykey');
// RedisException: read error on connection
?>
```

### Pipeline timeout on large batches

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->setOption(Redis::OPT_READ_TIMEOUT, 5);
$redis->pipeline(function ($pipe) {
    for ($i = 0; $i < 100000; $i++) {
        $pipe->set("key:{$i}", "value:{$i}");
    }
});
// RedisException: read error on connection
?>
```

## How to Fix

### Fix 1: Increase the Read Timeout

Set a higher read timeout to accommodate slow commands or network latency.

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

// Set read timeout to 30 seconds
$redis->setOption(Redis::OPT_READ_TIMEOUT, 30);

$redis->keys('user:*'); // Now has enough time to complete
?>
```

### Fix 2: Use Persistent Connections

Persistent connections avoid the overhead of re-establishing TCP handshakes, which reduces timeout risk.

```php
<?php
$redis = new Redis();
$redis->pconnect('127.0.0.1', 6379, 3.0, 'persistent_id_1', 100, 10);
//                                       timeout  retry    read_timeout
?>
```

### Fix 3: Replace KEYS with SCAN for Large Datasets

Use cursor-based iteration instead of blocking O(N) commands.

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->setOption(Redis::OPT_READ_TIMEOUT, 10);

$cursor = 0;
$keys = [];
do {
    [$cursor, $batch] = $redis->scan($cursor, 'user:*', 100);
    $keys = array_merge($keys, $batch);
} while ($cursor > 0);

echo 'Found ' . count($keys) . ' keys';
?>
```

### Fix 4: Use MULTI/EXEC for Atomic Operations Instead of Slow Pipelines

Break large pipelines into smaller transaction batches.

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->setOption(Redis::OPT_READ_TIMEOUT, 30);

function batchSet(Redis $redis, array $data, int $chunkSize = 500): void
{
    foreach (array_chunk($data, $chunkSize, true) as $chunk) {
        $redis->multi();
        foreach ($chunk as $key => $value) {
            $redis->set($key, $value);
        }
        $redis->exec();
    }
}

$data = range('key:', 10000);
batchSet($redis, $data);
?>
```

### Fix 5: Monitor and Diagnose Timeout Issues

Add timing instrumentation to identify slow operations.

```php
<?php
class RedisTimeoutMonitor
{
    private Redis $redis;
    private float $threshold;

    public function __construct(Redis $redis, float $threshold = 1.0)
    {
        $this->redis = $redis;
        $this->threshold = $threshold;
    }

    public function execute(string $command, mixed ...$args): mixed
    {
        $start = microtime(true);
        try {
            $result = $this->redis->{$command}(...$args);
            $elapsed = microtime(true) - $start;

            if ($elapsed > $this->threshold) {
                error_log(sprintf(
                    'Slow Redis command: %s took %.2fs (threshold: %.2fs)',
                    $command,
                    $elapsed,
                    $this->threshold
                ));
            }

            return $result;
        } catch (RedisException $e) {
            $elapsed = microtime(true) - $start;
            error_log(sprintf(
                'Redis command failed after %.2fs: %s — %s',
                $elapsed,
                $command,
                $e->getMessage()
            ));
            throw $e;
        }
    }
}

$monitor = new RedisTimeoutMonitor($redis, 2.0);
$monitor->execute('get', 'mykey');
?>
```

## Examples

### Optimize Redis for Large-Scale Reads

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->setOption(Redis::OPT_READ_TIMEOUT, 0); // no read timeout
$redis->setOption(Redis::OPT_SCAN, Redis::SCAN_RETRY);

// Use pipeline for batch reads
$keys = ['key1', 'key2', 'key3'];
$results = $redis->pipeline(function ($pipe) use ($keys) {
    foreach ($keys as $key) {
        $pipe->get($key);
    }
});

foreach ($results as $index => $value) {
    echo $keys[$index] . ': ' . ($value ?: 'null') . PHP_EOL;
}
?>
```

### Timeout Configuration for Production

```php
<?php
function createProductionRedis(): Redis
{
    $redis = new Redis();
    $redis->connect(
        getenv('REDIS_HOST') ?: '127.0.0.1',
        (int) (getenv('REDIS_PORT') ?: 6379),
        5.0   // connection timeout
    );

    // Aggressive read timeout to detect problems early
    $redis->setOption(Redis::OPT_READ_TIMEOUT, 10);

    // Enable automatic reconnection on read errors
    $redis->setOption(Redis::OPT_RETRY, true);
    $redis->setOption(Redis::OPT_BACKOFF_FUNCTION, function ($retries) {
        return min(250 * (2 ** $retries), 5000);
    });

    return $redis;
}
?>
```

## Related Errors

- [Redis Connection Error]({{< relref "/languages/php/redis-connection-error" >}})
- [Redis Pipeline Error]({{< relref "/languages/php/redis-pipeline-error" >}})
- [Redis Command Error]({{< relref "/languages/php/redis-command-error" >}})
