---
title: "[Solution] Lua Coroutine Yield Error Fix"
description: "Fix Lua coroutine yield errors. Learn when and how to yield from coroutines safely."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1103
---

## What This Error Means

A coroutine yield error occurs when attempting to yield from a coroutine in an invalid context, such as inside a pcall/xpcall protected call, or when trying to yield across a C-call boundary.

## Common Causes

- Yielding inside a pcall or xpcall block
- Yielding from within a C function that doesn't support yielding
- Yielding from the main thread (non-coroutine context)
- Yielding inside __gc, __tostring metamethods
- Confusing coroutine.yield with coroutine.resume

## How to Fix

```lua
-- WRONG: Yielding inside pcall
local co = coroutine.create(function()
    pcall(function()
        coroutine.yield()  -- error: cannot yield across pcall
    end)
end)
coroutine.resume(co)

-- CORRECT: Yield outside pcall
local co = coroutine.create(function()
    coroutine.yield()  -- OK
    pcall(function()
        print("inside pcall")
    end)
end)
coroutine.resume(co)
```

```lua
-- WRONG: Yielding inside __gc
local mt = { __gc = function() coroutine.yield() end }
-- error: cannot yield in garbage collection

-- CORRECT: Do not yield in __gc
local mt = { __gc = function() print("cleaning up") end }
```

```lua
-- WRONG: Yielding from main thread
coroutine.yield()  -- error outside coroutine

-- CORRECT: Create a coroutine first
local co = coroutine.create(function()
    coroutine.yield("hello")
end)
local success, result = coroutine.resume(co)
print(result)  -- hello
```

```lua
-- Safe yielding pattern
local co = coroutine.create(function()
    for i = 1, 5 do
        coroutine.yield(i)
    end
end)

while coroutine.status(co) ~= "dead" do
    local ok, val = coroutine.resume(co)
    if ok then
        print("Got:", val)
    end
end
```

## Examples

```lua
function create_range(from, to)
    return coroutine.wrap(function()
        for i = from, to do
            coroutine.yield(i)
        end
    end)
end

for num in create_range(1, 5) do
    print(num)
end
```

## Related Errors

- [Lua coroutine error](lua-coroutine-error) - coroutine issue
- [Lua runtime error](lua-runtime-error) - runtime issue
- [Lua nil call error](lua-nil-call-error) - nil call
