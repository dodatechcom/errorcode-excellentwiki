---
title: "[Solution] Lua Redis Error"
description: "Fix Lua Redis connection errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Redis errors occur when Redis operations fail.

## Common Causes

- Connection refused
- Command error
- Wrong database number
- Timeout

## How to Fix

### 1. Handle Redis connection

```lua
local redis = require("redis")
local client = redis.connect("127.0.0.1", 6379)
```

### 2. Handle Redis errors

```lua
local function safeRedisOp(client, cmd, ...)
  local ok, result = pcall(client[cmd], client, ...)
  if ok then
    return result
  else
    return nil, result
  end
end
```

## Examples

```lua
-- Safe Redis operations
local function setKey(client, key, value, ttl)
  local ok, err = client:set(key, value)
  if not ok then
    return false, err
  end
  
  if ttl then
    client:expire(key, ttl)
  end
  
  return true
end

local function getKey(client, key)
  return client:get(key)
end
```

## Related Errors

- [Socket error](/languages/lua/lua-socket-error)
- [Connection error](/languages/lua/lua-connection-error)
- [Runtime error](/languages/lua/lua-runtime-error)
