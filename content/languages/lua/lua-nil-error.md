---
title: "[Solution] Lua Nil Error Fix"
description: "Fix Lua nil errors. Learn why nil access causes crashes and how to handle nil values."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["nil", "null", "access", "lua"]
weight: 5
---

## What This Error Means

A Lua nil error occurs when you try to index, call, or perform operations on a nil value. Nil represents the absence of a value in Lua and cannot be used directly.

## Common Causes

- Accessing undefined variables
- Missing table fields
- Failed function returns
- Uninitialized variables

## How to Fix

```lua
-- WRONG: Accessing nil
local value = nil
print(value.field)  -- attempt to index nil

-- CORRECT: Check for nil first
if value then
    print(value.field)
end
```

```lua
-- WRONG: Not checking require result
local mylib = require("nonexistent")
print(mylib.func())  -- attempt to index nil

-- CORRECT: Check require result
local ok, mylib = pcall(require, "my_module")
if ok and mylib then
    mylib.doSomething()
end
```

## Examples

```lua
-- Example 1: Nil checks
local function safe_call(func, ...)
    if type(func) == "function" then
        return func(...)
    end
    return nil
end

-- Example 2: Default values
local function with_default(value, default)
    return value ~= nil and value or default
end

-- Example 3: Safe navigation
local config = {}
local host = config.database and config.database.host or "localhost"
```

## Related Errors

- [Lua type error](lua-type-error) - type mismatch
- [Lua index error](lua-index-error) - index out of range
- [Lua runtime error](lua-runtime-error) - runtime issue
