---
title: "[Solution] Redis Lua Script Timeout Error"
description: "How to fix Redis Lua script timeout when scripts exceed the configured time limit"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Script doing heavy computation
- Script making too many redis.call() invocations
- Script accessing large datasets
- `lua-time-limit` too low

## How to Fix

Check current timeout:

```bash
redis-cli CONFIG GET lua-time-limit
```

Increase timeout:

```bash
redis-cli CONFIG SET lua-time-limit 10000
```

Rewrite script to be efficient:

```lua
-- Bad: calling EVALSHA multiple times in loop
-- Good: single script with KEYS
local results = {}
for i = 1, #KEYS do
    results[i] = redis.call('GET', KEYS[i])
end
return results
```

Monitor slow scripts:

```bash
redis-cli SLOWLOG GET 10
```

## Examples

```bash
# Increase timeout
redis-cli CONFIG SET lua-time-limit 10000

# Check slow log
redis-cli SLOWLOG GET 5

# Test script execution time
time redis-cli EVAL "return redis.call('PING')" 0
```
