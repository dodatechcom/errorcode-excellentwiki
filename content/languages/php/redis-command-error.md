---
title: "[Solution] PHP REDIS_COMMAND_ERROR — Redis Command Failed"
description: "Fix PHP Redis WRONGTYPE and command execution errors. Handle key type mismatches and invalid command syntax."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 106
---

# PHP REDIS_COMMAND_ERROR — Redis Command Failed

A Redis command returned an error such as `WRONGTYPE Operation against a key holding the wrong kind of value`, `ERR unknown command`, or `ERR wrong number of arguments`. This happens when you operate on a key with the wrong data type or pass invalid arguments to a Redis command.

## Common Causes

### WRONGTYPE — operating on wrong key type

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$redis->set('mykey', 'string value');
$redis->lPush('mykey', 'item'); // WRONGTYPE: key is a string, not a list
?>
```

### Invalid command syntax

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$redis->rawCommand('SET'); // ERR wrong number of arguments for 'set' command
?>
```

### Wrong number of arguments

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$redis->hSet('hash_key'); // ERR wrong number of arguments for 'hset' command
?>
```

### Key deleted between check and use

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

if ($redis->exists('counter')) {
    $redis->incr('counter'); // may fail if key was deleted between calls
}
?>
```

### Using deprecated or removed commands

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$redis->rawCommand('SUBSCRIBE', 'channel', 'extra_arg');
// ERR wrong number of arguments for 'subscribe' command
?>
```

## How to Fix

### Fix 1: Check Key Type Before Operating

Verify the key type before performing type-specific operations.

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$redis->set('mykey', 'string value');

$type = $redis->type('mykey');
if ($type === Redis::REDIS_STRING) {
    $redis->set('mykey', 'new value');
} elseif ($type === Redis::REDIS_LIST) {
    $redis->lPush('mykey', 'item');
}
?>
```

### Fix 2: Use try-catch for Command Errors

Wrap Redis commands in try-catch blocks to handle WRONGTYPE and other errors gracefully.

```php
<?php
function safeLpush(Redis $redis, string $key, mixed $value): bool
{
    try {
        $redis->lPush($key, $value);
        return true;
    } catch (RedisException $e) {
        if (str_contains($e->getMessage(), 'WRONGTYPE')) {
            $redis->del($key);
            $redis->lPush($key, $value);
            return true;
        }
        throw $e;
    }
}
?>
```

### Fix 3: Use Atomic Operations

Use Redis transactions or Lua scripts to avoid race conditions.

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

// Atomic increment-or-set using SET with NX
$result = $redis->set('counter', 1, ['nx', 'ex' => 60]);
if (!$result) {
    $redis->incr('counter');
}
?>
```

### Fix 4: Validate Command Arguments

Check arguments before sending commands to Redis.

```php
<?php
function safeHset(Redis $redis, string $key, string $field, string $value): bool
{
    if ($field === '' || $value === '') {
        throw new InvalidArgumentException('Field and value must be non-empty');
    }
    return $redis->hSet($key, $field, $value);
}
?>
```

### Fix 5: Use Named Commands with Argument Count Checks

Use the PHPRedis wrapper methods instead of `rawCommand` for safer usage.

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

// Instead of rawCommand('SET', 'key', 'value'):
$redis->set('key', 'value');

// Instead of rawCommand('HSET', 'key'):
$redis->hSet('hash', 'field', 'value');
?>
```

## Examples

### Safe Type-Aware Key Writer

```php
<?php
class RedisTypeSafe
{
    private Redis $redis;

    public function __construct(Redis $redis)
    {
        $this->redis = $redis;
    }

    public function overwriteAsList(string $key, array $items): void
    {
        try {
            $this->redis->del($key);
            foreach ($items as $item) {
                $this->redis->lPush($key, $item);
            }
        } catch (RedisException $e) {
            error_log("Failed to overwrite key '{$key}' as list: " . $e->getMessage());
            throw $e;
        }
    }

    public function safeIncrement(string $key, int $value = 1): int|false
    {
        try {
            return $this->redis->incrBy($key, $value);
        } catch (RedisException $e) {
            if (str_contains($e->getMessage(), 'WRONGTYPE')) {
                $this->redis->del($key);
                return $this->redis->incrBy($key, $value);
            }
            throw $e;
        }
    }
}
?>
```

### Pipeline with Error Isolation

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$results = $redis->pipeline(function ($pipe) {
    $pipe->set('key1', 'value1');
    $pipe->set('key2', 'value2');
    $pipe->incr('key1'); // WRONGTYPE — but other commands succeed
});

// Check individual results for errors
foreach ($results as $index => $result) {
    if ($result === false) {
        error_log("Pipeline command {$index} failed");
    }
}
?>
```

## Related Errors

- [Redis Connection Error]({{< relref "/languages/php/redis-connection-error" >}})
- [Redis Pipeline Error]({{< relref "/languages/php/redis-pipeline-error" >}})
- [Redis Timeout Error]({{< relref "/languages/php/redis-timeout-error" >}})
