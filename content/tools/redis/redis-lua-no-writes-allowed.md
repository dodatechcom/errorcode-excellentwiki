---
title: "[Solution] Redis Lua No Writes Allowed Error"
description: "How to fix Redis Lua script read-only mode errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Script uses redis.call() write commands in read-only replica
- Replica configured with `replica-read-only yes`

## Fix

Check replica read-only setting:

```bash
redis-cli CONFIG GET replica-read-only
```

Use redis.pcall() to handle errors gracefully:

```lua
local result = redis.pcall('SET', KEYS[1], ARGV[1])
if result.err then
    return {err = result.err}
end
return result
```

Run write scripts on master:

```bash
redis-cli -h master-host -p 6379 EVAL "..." 0
```

## Examples

```bash
# Check read-only mode
redis-cli CONFIG GET replica-read-only

# Disable read-only (not recommended for replicas)
redis-cli CONFIG SET replica-read-only no

# Run on master
redis-cli -h master-host EVAL "return redis.call('SET', KEYS[1], ARGV[1])" 1 mykey myvalue
```
