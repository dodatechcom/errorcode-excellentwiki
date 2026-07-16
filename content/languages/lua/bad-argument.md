---
title: "bad argument #1"
description: "A bad argument error occurs when a function receives an argument of the wrong type or invalid value."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["argument", "type", "invalid", "lua"]
weight: 5
---

## What This Error Means

A `bad argument #1` error is raised when a function receives an argument that doesn't match the expected type or value. This is common with built-in functions that have strict type requirements.

## Common Causes

- Wrong type passed to built-in function
- Passing nil where a value is expected
- Invalid string format
- Wrong number of arguments

## How to Fix

```lua
-- WRONG: Wrong type to function
local n = tonumber(true)  -- bad argument #1

-- CORRECT: Ensure correct type
local n = tonumber("123")  -- 123
```

```lua
-- WRONG: Passing nil
local len = string.len(nil)  -- bad argument #1

-- CORRECT: Check for nil first
local str = "hello"
if str then
    local len = string.len(str)
end
```

## Examples

```lua
-- Example 1: Wrong type
local n = tonumber({})  -- bad argument #1

-- Example 2: Nil argument
local s = string.gsub(nil, "a", "b")  -- bad argument #1

-- Example 3: Invalid format
local n = string.format("%d", "not a number")  -- bad argument #2
```

## Related Errors

- [attempt to index nil](/languages/lua/nil-index)
- [attempt to perform arithmetic on nil](/languages/lua/arithmetic-nil)
