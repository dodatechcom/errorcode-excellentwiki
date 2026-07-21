---
title: "[Solution] Lua Coro Check Error"
description: "Fix Lua coroutine status check errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Coro check errors occur when coroutine status is checked incorrectly.

## Common Causes

- Non-coroutine argument
- Status check on nil
- Wrong status comparison
- Dead coroutine check

## How to Fix

### 1. Validate coroutine

```lua
local function safeStatus(co)
  if type(co) ~= "thread" then
    return nil, "Not a coroutine"
  end
  return coroutine.status(co)
end
```

### 2. Check status correctly

```lua
local function isAlive(co)
  local status = coroutine.status(co)
  return status ~= "dead"
end
```

## Examples

```lua
-- Coroutine lifecycle
local function demonstrate()
  local co = coroutine.create(function()
    coroutine.yield("step1")
    coroutine.yield("step2")
    return "done"
  end)
  
  print(coroutine.status(co))  -- "suspended"
  
  coroutine.resume(co)  -- "step1"
  print(coroutine.status(co))  -- "suspended"
  
  coroutine.resume(co)  -- "step2"
  print(coroutine.status(co))  -- "suspended"
  
  coroutine.resume(co)  -- "done"
  print(coroutine.status(co))  -- "dead"
end
```

## Related Errors

- [Coroutine resume error](/languages/lua/lua-coroutine-resume-error)
- [Coroutine status error](/languages/lua/lua-coroutine-status-error)
- [Runtime error](/languages/lua/lua-runtime-error)
