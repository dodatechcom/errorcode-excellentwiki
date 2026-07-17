---
title: "Redis Lua - script execution error"
description: "Redis Lua script fails to execute due to syntax errors, runtime errors, or cross-slot violations"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A Redis Lua script execution error occurs when a Lua script loaded or executed via `EVAL`/`EVALSHA` encounters an error. This can be caused by Lua syntax errors, invalid Redis commands within the script, or cross-slot access violations in a cluster.

## Common Causes

- Lua syntax error in the script
- Redis command not allowed in Lua scripts (KEYS in wrong context)
- Cross-slot access in Redis Cluster (accessing keys from different slots)
- Script exceeds time limit (5 seconds default)
- Missing KEYS or ARGV arguments

## How to Fix

1. Test Lua scripts locally before deploying:

```lua
-- Test script locally
local current = tonumber(redis.call('GET', KEYS[1]) or 0)
local amount = tonumber(ARGV[1])
if current >= amount then
    redis.call('DECRBY', KEYS[1], amount)
    return 1
else
    return 0
end
```

2. Use hash tags for cluster-compatible scripts:

```lua
-- All keys must be in the same slot
-- Use hash tags: {user:123}:balance, {user:123}:history
local balance = redis.call('GET', KEYS[1])
local history = redis.call('RPUSH', KEYS[2], ARGV[1])
```

3. Increase script timeout for long operations:

```bash
redis-cli CONFIG SET lua-time-limit 10000
```

4. Handle script errors in application code:

```javascript
try {
  const result = await redis.evalsha(sha1, 1, 'key1', 'arg1');
} catch (error) {
  if (error.message.includes('NOSCRIPT')) {
    // Script not cached, load and execute again
    const sha1 = await redis.script('load', luaScript);
    const result = await redis.evalsha(sha1, 1, 'key1', 'arg1');
  } else {
    throw error;
  }
}
```

5. Debug scripts with `redis.log`:

```lua
redis.log(redis.LOG_DEBUG, "Processing key: " .. KEYS[1])
local result = redis.call('GET', KEYS[1])
redis.log(redis.LOG_DEBUG, "Result: " .. tostring(result))
```

## Examples

```bash
# Error: ERR Error running script (call to f_xxx): ...
> EVAL "redis.call('GET', KEYS[1])" 1 key1
# Works fine

> EVAL "redis.call('GET', KEYS[1], KEYS[2])" 1 key1
# Error: wrong number of arguments for 'get' command

# Fix: correct argument count
> EVAL "redis.call('GET', KEYS[1])" 1 key1
```

```bash
# Cross-slot error in cluster
> EVAL "redis.call('GET', 'slot1:key1'); redis.call('GET', 'slot2:key2')" 2 slot1:key1 slot2:key2
# Error: CROSSSLOT Keys in request don't hash to the same slot

# Fix: use hash tags
> EVAL "redis.call('GET', KEYS[1]); redis.call('GET', KEYS[2])" 2 {user:123}:name {user:123}:email
```

## Related Errors

- [Transaction error]({{< relref "/tools/redis/redis-transaction-error" >}})
- [Cluster error]({{< relref "/tools/redis/redis-cluster-error" >}})
