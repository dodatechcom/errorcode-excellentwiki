---
title: "[Solution] Lua Argument Type Error Fix - Bad Argument to Function"
description: "Fix Lua 'bad argument #N to function' type errors. Learn why argument type checks fail and how to validate inputs."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

The `bad argument #N to function_name (type expected, got type)` error in Lua occurs when a function receives an argument of the wrong type. Lua is dynamically typed, but many built-in functions and C API functions perform strict type checking on their arguments.

## Why It Happens

- Passing a string where a number is expected
- Passing `nil` to a function that requires a non-nil value
- Passing a table where a string is expected, or vice versa
- Wrong number of arguments to a variadic function
- Passing a non-function where a callback is expected
- Accidentally passing the wrong variable due to variable shadowing

## How to Fix It

### Validate argument types explicitly

```lua
-- WRONG: Passing string to math function
local result = string.rep("a", "5")  -- bad argument #2 (number expected)

-- CORRECT: Ensure correct types
local count = tonumber("5") or 0
local result = string.rep("a", count)
```

### Use assert for preconditions

```lua
-- WRONG: No validation before use
local function add(a, b)
    return a + b
end
add("one", 2)  -- bad argument #1

-- CORRECT: Validate with assert
local function add(a, b)
    assert(type(a) == "number", "expected number for a, got " .. type(a))
    assert(type(b) == "number", "expected number for b, got " .. type(b))
    return a + b
end
add("one", 2)  -- clear error message
```

### Guard against nil arguments

```lua
-- WRONG: Function cannot handle nil
local function greet(name)
    return "Hello, " .. name  -- crashes if name is nil
end

-- CORRECT: Handle nil gracefully
local function greet(name)
    if name == nil then
        return "Hello, stranger"
    end
    return "Hello, " .. tostring(name)
end
```

### Check argument count for variadic functions

```lua
-- WRONG: Not enough arguments
local function connect(host, port, timeout)
    -- ...
end
connect("localhost")  -- port is nil, may cause issues downstream

-- CORRECT: Provide defaults or validate
local function connect(host, port, timeout)
    port = port or 80
    timeout = timeout or 30
end
connect("localhost")
```

### Use type checking helper functions

```lua
-- WRONG: Direct use without type safety
local function process(data)
    return data.items[1].name
end

-- CORRECT: Validate nested types
local function process(data)
    assert(type(data) == "table", "data must be a table")
    assert(type(data.items) == "table", "data.items must be a table")
    assert(#data.items > 0, "data.items must not be empty")
    return data.items[1].name
end
```

## Common Mistakes

- Not converting string input to number before arithmetic operations
- Passing a `nil` value where a table is expected, especially from failed `require` calls
- Forgetting that `tostring(nil)` returns the string `"nil"`, not an empty string
- Mixing up argument order, especially with multiple optional parameters
- Not checking the return type of a function before passing it as an argument

## Related Pages

- [Lua Nil Index Error](lua-nil-index-error) - indexing nil value
- [Lua Nil Call Error](lua-nil-call-error) - calling nil value
- [Lua String Concat Nil](lua-string-concat-nil) - concatenating nil
- [Lua Metatable Error](lua-metatable-error) - metamethod argument error
