---
title: "[Solution] Lua Bad Argument Error Fix"
description: "Fix Lua bad argument errors. Learn why argument validation fails and how to check function arguments."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["argument", "parameter", "type", "lua"]
weight: 5
---

## What This Error Means

A Lua bad argument error occurs when a function receives an argument of the wrong type or nil when a value is expected. Lua is dynamically typed but still validates argument types in many functions.

## Common Causes

- Nil passed to function expecting value
- Wrong type passed (string vs number)
- Missing required arguments
- Wrong number of arguments

## How to Fix

```lua
-- WRONG: Passing nil to string function
local name = nil
print(string.len(name))  -- bad argument #1

-- CORRECT: Check argument
local function safe_len(str)
    if type(str) ~= "string" then
        return 0
    end
    return string.len(str)
end
print(safe_len(name))
```

```lua
-- WRONG: Wrong type argument
local function add(a, b)
    return a + b
end
add("1", 2)  -- attempt to perform arithmetic on string

-- CORRECT: Validate types
local function add(a, b)
    assert(type(a) == "number", "a must be number")
    assert(type(b) == "number", "b must be number")
    return a + b
end
```

## Examples

```lua
-- Example 1: Argument validation
local function divide(a, b)
    assert(type(a) == "number", "First argument must be number")
    assert(type(b) == "number", "Second argument must be number")
    assert(b ~= 0, "Cannot divide by zero")
    return a / b
end

-- Example 2: Variable arguments
local function sum(...)
    local result = 0
    for i = 1, select("#", ...) do
        result = result + select(i, ...)
    end
    return result
end

-- Example 3: Optional arguments
local function greet(name, greeting)
    name = name or "World"
    greeting = greeting or "Hello"
    print(greeting .. ", " .. name .. "!")
end
```

## Related Errors

- [Lua type error](lua-type-error) - type mismatch
- [Lua nil error](lua-nil-error) - nil access
- [Lua runtime error](lua-runtime-error) - runtime issue
