---
title: "[Solution] Lua Attempt to Perform Arithmetic on Nil"
description: "Fix Lua type errors when performing operations on wrong types. Handle nil values, type checking, and conversion."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The error `attempt to perform arithmetic on a nil value` occurs when you try to use arithmetic operators on `nil` or non-numeric values in Lua. Other type errors include `attempt to concatenate`, `attempt to compare`, etc.

## Common Causes

- Variable not assigned (nil by default)
- Wrong type for arithmetic operation
- Function returning nil unexpectedly
- Table value is nil
- Incorrect type conversion

## How to Fix

```lua
-- WRONG: Arithmetic on nil
local x = nil
local y = x + 1  -- attempt to perform arithmetic on nil

-- CORRECT: Provide default value
local x = x or 0
local y = x + 1
```

```lua
-- WRONG: Adding strings
local a = "5"
local b = "3"
local c = a + b  -- attempt to perform arithmetic on string

-- CORRECT: Convert first
local c = tonumber(a) + tonumber(b)
```

```lua
-- WRONG: Concatenating number with nil
local name = nil
print("Hello " .. name)  -- attempt to concatenate nil

-- CORRECT: Default or convert
name = name or "World"
print("Hello " .. name)
```

## Examples

```lua
-- Example 1: Type checking function
local function safe_add(a, b)
    if type(a) ~= "number" then a = tonumber(a) or 0 end
    if type(b) ~= "number" then b = tonumber(b) or 0 end
    return a + b
end

-- Example 2: Table value defaults
local config = {}
local timeout = config.timeout or 30
local retries = config.retries or 3

-- Example 3: Safe arithmetic with pcall
local function safe_arithmetic(func, ...)
    local ok, result = pcall(func, ...)
    if ok then return result end
    return nil, result  -- result is error message
end
```

## Related Errors

- [lua-index-error]({{< relref "/languages/lua/lua-index-error" >}}) — index nil value
- [lua-nil-error]({{< relref "/languages/lua/lua-nil-error" >}}) — call nil
- [lua-argument-error]({{< relref "/languages/lua/lua-argument-error" >}}) — argument error
