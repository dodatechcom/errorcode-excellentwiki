---
title: "[Solution] PHP REDIS_PIPELINE_ERROR — Redis Pipeline/Transaction Failure"
description: "Fix PHP Redis pipeline and MULTI/EXEC transaction failures. Handle optimistic locking and command errors in pipelines."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 110
---

# PHP REDIS_PIPELINE_ERROR — Redis Pipeline/Transaction Failure

Redis pipelines or MULTI/EXEC transactions failed because one or more commands returned an error, the connection was lost mid-transaction, or optimistic locking via `WATCH` detected a conflict. Pipelines send multiple commands without waiting for individual responses, so a failure in one command may not be detected until `exec()` or when processing results.

## Common Causes

### WRONGTYPE inside a pipeline

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$redis->set('counter', 'not_a_number');
$results = $redis->pipeline(function ($pipe) {
    $pipe->get('counter');
    $pipe->incr('counter'); // WRONGTYPE — error returned in results
});
// $results[1] is false — error not thrown
?>
```

### Connection lost during MULTI/EXEC

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$redis->multi();
$redis->set('key1', 'value1');
$redis->set('key2', 'value2');
// network interruption happens here
$redis->exec(); // RedisException: Connection lost
?>
```

### WATCH lock conflict in optimistic transactions

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$redis->watch('counter');
$value = (int) $redis->get('counter');
// another process modifies 'counter' here
$redis->multi();
$redis->set('counter', $value + 1);
$redis->exec(); // false — WATCH detected the conflict
?>
```

### Pipeline with too many commands

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$redis->pipeline(function ($pipe) {
    for ($i = 0; $i < 1000000; $i++) {
        $pipe->set("key:{$i}", "value:{$i}");
    }
});
// RedisException: read/write timeout or out of memory
?>
```

### Syntax error in pipelined command

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$results = $redis->pipeline(function ($pipe) {
    $pipe->set('key', 'value');
    $pipe->expire('key'); // missing TTL argument
    // ERR wrong number of arguments for 'expire' command
});
?>
```

## How to Fix

### Fix 1: Check Pipeline Results for Errors

Always inspect the results array — pipelined errors do not throw exceptions automatically.

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$results = $redis->pipeline(function ($pipe) {
    $pipe->set('a', '1');
    $pipe->incr('a');
    $pipe->incr('a');
});

foreach ($results as $index => $result) {
    if ($result === false) {
        error_log("Pipeline command {$index} failed — check command and key types");
    }
}

// All results: [true, '2', '3']
?>
```

### Fix 2: Use MULTI/EXEC with Error Handling

Wrap transactions in try-catch and check the exec return value.

```php
<?php
function safeTransaction(Redis $redis, callable $callback): bool
{
    try {
        $redis->multi();
        $callback($redis);
        $result = $redis->exec();

        if ($result === false) {
            error_log('Transaction failed or was discarded');
            return false;
        }

        return true;
    } catch (RedisException $e) {
        $redis->discard();
        error_log('Transaction exception: ' . $e->getMessage());
        throw $e;
    }
}

$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$safeTransaction($redis, function (Redis $pipe) {
    $pipe->set('key1', 'value1');
    $pipe->set('key2', 'value2');
});
?>
```

### Fix 3: Implement Optimistic Locking with Retry

Use WATCH with a retry loop to handle concurrent modifications.

```php
<?php
function optimisticIncrement(Redis $redis, string $key, int $maxRetries = 5): int|false
{
    for ($attempt = 0; $attempt < $maxRetries; $attempt++) {
        $redis->watch($key);
        $current = $redis->get($key);

        if ($current === false) {
            $redis->unwatch();
            return false;
        }

        $redis->multi();
        $redis->set($key, (int) $current + 1);
        $result = $redis->exec();

        if ($result !== false) {
            return (int) $current + 1;
        }

        // Exec failed — another process modified the key
        usleep(1000 * (2 ** $attempt)); // exponential backoff
    }

    return false;
}

$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->set('counter', 0);

$newValue = optimisticIncrement($redis, 'counter');
echo 'New value: ' . $newValue;
?>
```

### Fix 4: Chunk Large Pipelines

Break huge pipelines into smaller batches to avoid timeouts and memory issues.

```php
<?php
function chunkedPipeline(Redis $redis, array $data, int $chunkSize = 1000): array
{
    $allResults = [];
    $chunks = array_chunk($data, $chunkSize, true);

    foreach ($chunks as $chunkIndex => $chunk) {
        $results = $redis->pipeline(function ($pipe) use ($chunk) {
            foreach ($chunk as $key => $value) {
                $pipe->set($key, $value);
            }
        });

        foreach ($results as $i => $result) {
            if ($result === false) {
                error_log("Chunk {$chunkIndex} command {$i} failed");
            }
        }

        $allResults = array_merge($allResults, $results);
    }

    return $allResults;
}

$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$data = [];
for ($i = 0; $i < 50000; $i++) {
    $data["batch:{$i}"] = "value:{$i}";
}

$results = chunkedPipeline($redis, $data, 5000);
echo 'Set ' . count($results) . ' keys';
?>
```

### Fix 5: Handle Transaction Failures in Lua Scripts

Use Lua scripts as a more reliable alternative to MULTI/EXEC for complex operations.

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

// Atomic transfer: debit one account, credit another
$luaScript = <<<LUA
    local current = tonumber(redis.call('GET', KEYS[1]))
    if current == nil or current < tonumber(ARGV[1]) then
        return -1
    end
    redis.call('DECRBY', KEYS[1], ARGV[1])
    redis.call('INCRBY', KEYS[2], ARGV[1])
    return 1
LUA;

$result = $redis->eval($luaScript, ['account:A', 'account:B'], [100]);

if ($result === -1) {
    echo 'Insufficient balance';
} else {
    echo 'Transfer completed';
}
?>
```

## Examples

### Reliable Multi-Command Writer

```php
<?php
class RedisBatchWriter
{
    private Redis $redis;
    private int $chunkSize;

    public function __construct(Redis $redis, int $chunkSize = 500)
    {
        $this->redis = $redis;
        $this->chunkSize = $chunkSize;
    }

    public function writeMany(array $pairs): array
    {
        $results = [];
        $chunks = array_chunk($pairs, $this->chunkSize, true);

        foreach ($chunks as $chunk) {
            $pipelineResults = $this->redis->pipeline(function ($pipe) use ($chunk) {
                foreach ($chunk as $key => $value) {
                    $pipe->set($key, $value);
                }
            });

            foreach ($pipelineResults as $i => $result) {
                if ($result === false) {
                    $keys = array_keys($chunk);
                    error_log("Failed to write key: " . $keys[$i]);
                }
            }

            $results = array_merge($results, $pipelineResults);
        }

        return $results;
    }
}

$writer = new RedisBatchWriter($redis);
$results = $writer->writeMany(['a' => '1', 'b' => '2', 'c' => '3']);
?>
```

### Multi-Exec with Rollback

```php
<?php
function transferFunds(Redis $redis, string $from, string $to, int $amount): bool
{
    $redis->watch([$from, $to]);

    $fromBalance = (int) $redis->get($from);
    $toBalance = (int) $redis->get($to);

    if ($fromBalance < $amount) {
        $redis->unwatch();
        return false;
    }

    $redis->multi();
    $redis->decrBy($from, $amount);
    $redis->incrBy($to, $amount);

    $result = $redis->exec();
    return $result !== false;
}

$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->set('user:1:balance', 1000);
$redis->set('user:2:balance', 500);

if (transferFunds($redis, 'user:1:balance', 'user:2:balance', 200)) {
    echo 'Transfer successful';
} else {
    echo 'Transfer failed — concurrent modification detected';
}
?>
```

## Related Errors

- [Redis Connection Error]({{< relref "/languages/php/redis-connection-error" >}})
- [Redis Command Error]({{< relref "/languages/php/redis-command-error" >}})
- [Redis Timeout Error]({{< relref "/languages/php/redis-timeout-error" >}})
