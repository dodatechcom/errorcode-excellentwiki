---
title: "script error"
description: "A script error occurs when a Lua script encounters an unhandled error during execution."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["script", "runtime", "error", "lua"]
weight: 5
---

## What This Error Means

A script error is a general term for runtime errors that occur during Lua script execution. This can encompass various error types including syntax errors, runtime errors, and unhandled exceptions.

## Common Causes

- Unhandled errors in script logic
- Missing error handling with pcall/xpcall
- External resource failures
- Invalid input to script

## How to Fix

```lua
-- WRONG: No error handling
local result = risky_operation()  -- may throw

-- CORRECT: Use pcall for error handling
local ok, result = pcall(risky_operation)
if ok then
    print("Success:", result)
else
    print("Error:", result)
end
```

```lua
-- WRONG: Not validating input
function process(data)
    return data.field  -- may crash
end

-- CORRECT: Validate input
function process(data)
    if type(data) ~= "table" then
        return nil, "Invalid data"
    end
    return data.field
end
```

## Examples

```lua
-- Example 1: Unhandled error
function divide(a, b)
    return a / b
end
divide(10, 0)  -- script error

-- Example 2: Missing error handling
local f = io.open("nonexistent.txt", "r")
local content = f:read("*all")  -- f is nil

-- Example 3: Assertion failure
assert(false, "This should not happen")  -- script error
```

## Related Errors

- [stack overflow](/languages/lua/stack-overflow4)
- [attempt to index nil](/languages/lua/nil-index)
