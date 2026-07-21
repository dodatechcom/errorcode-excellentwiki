---
title: "[Solution] Lua Coroutine Resume Error"
description: "Fix Lua coroutine resume errors when coroutine operations are misused or called incorrectly."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Coroutine resume errors occur when resuming a coroutine in an invalid state.

## Common Causes

- Resuming a dead coroutine
- Yielding from outside a coroutine
- Passing wrong arguments to coroutine.resume
- Nested resume from within coroutine

## How to Fix

### 1. Check coroutine status before resume

```lua
if coroutine.status(co) ~= "dead" then
  coroutine.resume(co)
end
```

### 2. Create new coroutine for reuse

```lua
local function createCoroutine()
  return coroutine.create(function()
    coroutine.yield("hello")
    return "done"
  end)
end
```

## Examples

```lua
local co = coroutine.create(function()
  for i = 1, 5 do
    coroutine.yield(i * 2)
  end
end

for i = 1, 5 do
  local success, value = coroutine.resume(co)
  if success then
    print(value)
  end
end
```

## Related Errors

- [Coroutine yield error](/languages/lua/lua-coroutine-yield-error)
- [Runtime error](/languages/lua/lua-nil-value)
- [Stack overflow error](/languages/lua/lua-stack-overflow)
