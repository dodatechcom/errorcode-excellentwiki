---
title: "[Solution] Lua Runtime Error in Function Call"
description: "Fix Lua runtime errors during function execution. Handle nil access, type mismatches, and calling errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["runtime", "function", "error", "exception", "lua"]
weight: 5
---

## What This Error Means

A Lua runtime error occurs when a Lua script fails during execution. This can happen due to nil access, type errors, calling non-function values, or other runtime issues.

## Common Causes

- Nil value access (indexing or calling nil)
- Wrong type operations (e.g., arithmetic on string)
- Calling non-function values
- Index out of range
- Missing required arguments

## How to Fix

```lua
-- WRONG: Nil access
local value = nil
print(value.field)  -- attempt to index nil

-- CORRECT: Check for nil
if value then
    print(value.field)
else
    print("Value is nil")
end
```

```lua
-- WRONG: Calling non-function
local not_a_function = "hello"
not_a_function()  -- attempt to call a string value

-- CORRECT: Verify type
if type(not_a_function) == "function" then
    not_a_function()
end
```

```lua
-- WRONG: Arithmetic on nil
local a = nil
local b = a + 1  -- attempt to perform arithmetic on nil

-- CORRECT: Default value
local a = a or 0
local b = a + 1
```

## Examples

```lua
-- Example 1: pcall for error handling
local ok, result = pcall(function()
    error("Something went wrong")
end)
if not ok then
    print("Error: " .. result)
end

-- Example 2: Type checking
local function process(value)
    if type(value) == "string" then
        print(value)
    else
        print("Expected string, got " .. type(value))
    end
end

-- Example 3: Safe function call
local function safe_call(func, ...)
    if type(func) == "function" then
        return func(...)
    else
        return nil, "Not a function"
    end
end
```

## Related Errors

- [lua-nil-error]({{< relref "/languages/lua/lua-nil-error" >}}) — call nil as function
- [lua-type-error]({{< relref "/languages/lua/lua-type-error" >}}) — type error
- [lua-argument-error]({{< relref "/languages/lua/lua-argument-error" >}}) — argument error
