---
title: "[Solution] Lua Type Error Fix"
description: "Fix Lua type errors. Learn why type mismatches occur and how to handle Lua types properly."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["type", "mismatch", "conversion", "lua"]
weight: 5
---

## What This Error Means

A Lua type error occurs when you try to perform an operation on a value of the wrong type. Lua is dynamically typed but still enforces type constraints for operations.

## Common Causes

- Arithmetic on strings
- Indexing non-table values
- Calling non-functions
- Concatenating nil

## How to Fix

```lua
-- WRONG: Arithmetic on string
local result = "5" + 3  -- attempt to perform arithmetic on string

-- CORRECT: Convert type
local result = tonumber("5") + 3
```

```lua
-- WRONG: Indexing non-table
local str = "hello"
print(str[1])  -- attempt to index a string value

-- CORRECT: Use string functions
print(string.sub(str, 1, 1))
```

## Examples

```lua
-- Example 1: Type checking
local function process(value)
    if type(value) == "number" then
        return value * 2
    elseif type(value) == "string" then
        return value .. value
    else
        return nil
    end
end

-- Example 2: Safe type conversion
local function to_number(value)
    if type(value) == "number" then
        return value
    elseif type(value) == "string" then
        return tonumber(value)
    end
    return nil
end

-- Example 3: Type assertions
local function assert_string(value)
    assert(type(value) == "string", "Expected string, got " .. type(value))
    return value
end
```

## Related Errors

- [Lua nil error](lua-nil-error) - nil access
- [Lua argument error](lua-argument-error) - wrong argument
- [Lua runtime error](lua-runtime-error) - runtime issue
