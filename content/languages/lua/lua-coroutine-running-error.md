---
title: "[Solution] Lua Coroutine Running Error"
description: "Fix Lua coroutine.running() errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Coroutine running errors occur when coroutine.running() is used incorrectly.

## Common Causes

- Called from main thread
- Wrong return value check
- Not checking if running
- Missing coroutine context

## How to Fix

### 1. Check running state

```lua
local function inCoroutine()
  return coroutine.running() ~= nil
end
```

### 2. Use running correctly

```lua
local function example()
  if coroutine.running() then
    print("Running in coroutine")
  else
    print("Running in main thread")
  end
end
```

## Examples

```lua
-- Conditional code based on context
local function createContextAware()
  local co = coroutine.create(function()
    print("In coroutine:", coroutine.running() ~= nil)
  end)
  
  coroutine.resume(co)
  print("In main:", coroutine.running() == nil)
end
```

## Related Errors

- [Coroutine resume error](/languages/lua/lua-coroutine-resume-error)
- [Coroutine status error](/languages/lua/lua-coroutine-status-error)
- [Runtime error](/languages/lua/lua-runtime-error)
