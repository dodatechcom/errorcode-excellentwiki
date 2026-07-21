---
title: "[Solution] Lua Coroutine Yield Error"
description: "Fix Lua coroutine yield errors when yield is called in invalid contexts."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Coroutine yield errors occur when yield is called from a non-coroutine context or in an invalid way.

## Common Causes

- Calling yield from main thread
- Yielding across C function boundary
- Yielding from within xpcall handler
- Using coroutine.wrap incorrectly

## How to Fix

### 1. Ensure yield is called from coroutine

```lua
local co = coroutine.create(function()
  coroutine.yield(42)
end)
```

### 2. Use coroutine.wrap for function syntax

```lua
local iter = coroutine.wrap(function()
  for i = 1, 10 do
    coroutine.yield(i)
  end
end)

for i = 1, 10 do
  print(iter())
end
```

## Examples

```lua
local producer = coroutine.create(function()
  for i = 1, 10 do
    coroutine.yield(i * 2)
  end
end)

for i = 1, 10 do
  print(coroutine.resume(producer))
end
```

## Related Errors

- [Coroutine resume error](/languages/lua/lua-coroutine-resume-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Function expected error](/languages/lua/lua-function-expected-error)
