---
title: "[Solution] Lua Coroutine Wrap Error"
description: "Fix Lua coroutine wrap function errors when using the coroutine.wrap API."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Corouwrap errors occur when coroutine.wrap is used incorrectly or the wrapped function behaves unexpectedly.

## Common Causes

- Calling wrap with non-function argument
- Not resuming wrapped coroutine
- Wrap function returning multiple values
- Error inside wrapped coroutine

## How to Fix

### 1. Validate wrap argument

```lua
local function safeWrap(fn)
  assert(type(fn) == "function", "Function expected")
  return coroutine.wrap(fn)
end
```

### 2. Handle wrapped coroutine errors

```lua
local iter = safeWrap(function()
  for i = 1, 5 do
    coroutine.yield(i)
  end
end)

for i = 1, 5 do
  local ok, val = pcall(iter)
  if ok then
    print(val)
  end
end
```

## Examples

```lua
local co = coroutine.wrap(function()
  for i = 1, 10 do
    coroutine.yield(i)
  end
end)

for i = 1, 10 do
  print(co())
end
```

## Related Errors

- [Coroutine resume error](/languages/lua/lua-coroutine-resume-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Function expected error](/languages/lua/lua-function-expected-error)
