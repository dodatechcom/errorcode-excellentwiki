---
title: "[Solution] Redis Lua redis.call Error"
description: "How to fix Redis Lua script errors from redis.call() failures"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- redis.call() returns error response
- Invalid command passed to redis.call()
- Wrong number of arguments to redis.call()

## Fix

Use redis.pcall() for error handling:

```lua
local result = redis.pcall('HGET', KEYS[1], ARGV[1])
if result then
    return result
else
    return nil
end
```

Check return type:

```lua
local result = redis.call('GET', KEYS[1])
if result == false then return nil end
if type(result) == 'table' and result.err then
    return {err = result.err}
end
return result
```

## Examples

```bash
# Script with error handling
redis-cli EVAL "
  local ok, result = pcall(redis.call, 'GET', KEYS[1])
  if not ok then return {err = result} end
  return result
" 1 mykey

# Check script error in slow log
redis-cli SLOWLOG GET 5
```
