---
title: "[Solution] Lua pcall Nil Function Call Error Fix"
description: "Fix Lua pcall errors when calling nil or invalid functions in protected mode."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1140
---

## What This Error Means

A pcall error occurs when trying to call a nil or invalid value in protected mode. While pcall itself catches errors, passing a nil as the function argument still produces an error.

## Common Causes

- Passing nil as the function to pcall
- Function reference becomes nil between check and call
- Calling a method on a nil object
- Function removed from table between assignment and call

## How to Fix

```lua
-- WRONG: Calling pcall with nil
local ok, result = pcall(nil)  -- Error: attempt to call a nil value

-- CORRECT: Check function exists
local fn = nil
if fn then
    local ok, result = pcall(fn)
end
```

```lua
-- WRONG: Method call on nil
local obj = nil
pcall(obj.method, obj)  -- Error

-- CORRECT: Check for nil first
local obj = nil
if obj then
    pcall(obj.method, obj)
end
```

```lua
local function safe_call(fn, ...)
    if type(fn) ~= "function" then
        return false, "not a function: " .. type(fn)
    end
    return pcall(fn, ...)
end
```

## Related Errors

- [Lua nil call error](lua-nil-call-error) - nil call
- [Lua xpcall error](lua-xpcall-error) - xpcall issue
- [Lua runtime error](lua-runtime-error) - runtime issue
