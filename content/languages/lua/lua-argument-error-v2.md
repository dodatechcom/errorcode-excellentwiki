---
title: "[Solution] Lua Bad Argument Error"
description: "Fix Lua bad argument errors when functions receive wrong number or type of arguments. Validate inputs and use optional arguments."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `bad argument` error occurs when a Lua function receives an argument of the wrong type or wrong number of arguments. This is common with C API functions and standard library calls.

## Common Causes

- Wrong argument type (e.g., passing number to string function)
- Wrong number of arguments
- nil where value expected
- Passing table where string expected

## How to Fix

```lua
-- WRONG: Wrong type argument
local n = tonumber("hello")  -- Returns nil, not error

-- WRONG: Type mismatch with C functions
string.rep("x", "5")  -- bad argument #2 to 'rep' (number expected, got string)

-- CORRECT: Ensure correct types
local n = tonumber("42") or 0
string.rep("x", 5)  -- "xxxxx"
```

```lua
-- WRONG: Wrong number of arguments
local function add(a, b)
    return a + b
end
add(1)  -- bad argument #2 (nil)

-- CORRECT: Provide default values
local function add(a, b)
    a = a or 0
    b = b or 0
    return a + b
end
add(1)  -- 1
```

```lua
-- WRONG: nil argument where value expected
print(nil)  -- Works but prints "nil"
string.len(nil)  -- bad argument #1

-- CORRECT: Check for nil
local function safe_len(s)
    if type(s) ~= "string" then
        error("Expected string, got " .. type(s))
    end
    return string.len(s)
end
```

## Examples

```lua
-- Example 1: Argument validation
local function divide(a, b)
    assert(type(a) == "number", "a must be a number")
    assert(type(b) == "number", "b must be a number")
    assert(b ~= 0, "division by zero")
    return a / b
end

-- Example 2: Variadic arguments
local function sum(...)
    local args = {...}
    local total = 0
    for _, v in ipairs(args) do
        total = total + v
    end
    return total
end
print(sum(1, 2, 3, 4))  -- 10

-- Example 3: Named arguments via table
local function greet(opts)
    opts = opts or {}
    local name = opts.name or "World"
    local greeting = opts.greeting or "Hello"
    return greeting .. ", " .. name .. "!"
end
print(greet({name = "Lua", greeting = "Hi"}))
```

## Related Errors

- [lua-type-error]({{< relref "/languages/lua/lua-type-error" >}}) — type error
- [lua-nil-error]({{< relref "/languages/lua/lua-nil-error" >}}) — nil call error
- [lua-runtime-error]({{< relref "/languages/lua/lua-runtime-error" >}}) — runtime error
