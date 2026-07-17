---
title: "Redis Lua Script Error"
description: "Redis EVAL Lua script execution encounters errors."
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
tags: ["redis", "lua", "script", "eval", "atomic"]
weight: 5
---

# Redis Lua Script Error

A Redis Lua script error occurs when an EVAL or EVALSHA script execution fails. Redis uses Lua scripting for atomic multi-step operations.

## Common Causes

- Lua syntax errors in script
- Script accesses non-existent keys
- Script exceeds execution time limit
- Script memory limit exceeded

## How to Fix

### Check Script Syntax

```bash
redis-cli EVAL "return 1" 0
```

### Use Script Debugging

```bash
redis-cli --ldb --eval script.lua key1 key2, arg1 arg2
```

### Fix Common Lua Errors

```lua
-- Access Redis keys
local val = redis.call('GET', KEYS[1])
redis.call('SET', KEYS[2], ARGV[1])

-- Handle nil values
if val then
    return val
else
    return nil
end
```

### Set Script Time Limit

```conf
# /etc/redis/redis.conf
lua-time-limit 5000
```

### Load Script

```bash
redis-cli SCRIPT LOAD "return redis.call('GET', KEYS[1])"
# Returns SHA1 hash
redis-cli EVALSHA <sha1> 1 mykey
```

### Debug Lua Scripts

```bash
redis-cli --ldb --eval script.lua key1, arg1
# Use 's' to step, 'n' for next, 'p' for print
```

## Examples

```bash
# Basic Lua script
redis-cli EVAL "return redis.call('SET', KEYS[1], ARGV[1])" 1 mykey myvalue

# With error handling
redis-cli EVAL "
local val = redis.call('GET', KEYS[1])
if val then return val else return 'not found' end
" 1 mykey
```

## Related Errors

- [Transaction Error]({{< relref "/tools/redis/redis-transaction-error" >}}) — transaction failure
- [Timeout Error]({{< relref "/tools/redis/redis-timeout-error" >}}) — operation timeout
