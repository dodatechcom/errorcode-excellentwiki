---
title: "[Solution] Redis BUSYKEY Script Running Error"
description: "How to fix Redis BUSYKEY error when a Lua script is blocking operations"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Lua script running for too long
- Script contains infinite loop
- Script performing too many operations
- `lua-time-limit` reached

## How to Fix

Check script timeout setting:

```bash
redis-cli CONFIG GET lua-time-limit
```

Kill the running script:

```bash
redis-cli SCRIPT KILL
```

Increase script time limit:

```bash
redis-cli CONFIG SET lua-time-limit 10000
```

Optimize the Lua script to be faster:

```lua
-- Instead of calling redis.call in a loop, use batch operations
local results = {}
for i, key in ipairs(ARGV) do
    results[i] = redis.call('GET', key)
end
return results
```

## Examples

```bash
# Kill running script
redis-cli SCRIPT KILL

# Check timeout
redis-cli CONFIG GET lua-time-limit

# Monitor script execution
redis-cli INFO stats | grep instantaneousops_per_sec
```
