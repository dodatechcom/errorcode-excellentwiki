---
title: "[Solution] Lua Attempt to Call Nil as Function"
description: "Fix Lua 'attempt to call a nil value' error when trying to invoke nil. Check function definitions, module loading, and variable assignments."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nil", "call", "function", "invoke", "module", "lua"]
weight: 5
---

## What This Error Means

The error `attempt to call a nil value` occurs when you try to invoke a variable as a function but its value is `nil`. This commonly happens when a function is undefined or a module fails to load.

## Common Causes

- Function not defined before use
- Module require() returned nil
- Typo in function name
- Function assigned to wrong variable
- Circular module dependencies

## How to Fix

```lua
-- WRONG: Calling undefined function
my_function()  -- attempt to call a nil value

-- CORRECT: Define function first
function my_function()
    print("Hello!")
end
my_function()
```

```lua
-- WRONG: Module not loaded correctly
local json = require("json")
json.decode(input)  -- Error if require returned nil

-- CORRECT: Verify module loaded
local ok, json = pcall(require, "json")
if not ok then
    error("Failed to load json module: " .. tostring(json))
end
json.decode(input)
```

```lua
-- WRONG: Typo in function name
function calculate_total()
    return 42
end
local result = claculate_total()  -- Error: typo

-- CORRECT: Check function exists before calling
if type(calculate_total) == "function" then
    local result = calculate_total()
end
```

## Examples

```lua
-- Example 1: Safe require
local function safe_require(module_name)
    local ok, module = pcall(require, module_name)
    if ok then return module end
    return nil, "Module not found: " .. module_name
end

-- Example 2: Function table pattern
local M = {}
function M.hello()
    print("Hello from module!")
end
function M.goodbye()
    print("Goodbye!")
end
return M

-- Example 3: Check callable
local function safe_call(func, ...)
    if type(func) == "function" then
        return func(...)
    else
        return nil, "Value is not callable: " .. type(func)
    end
end
```

## Related Errors

- [lua-index-error]({{< relref "/languages/lua/lua-index-error" >}}) — index nil value
- [lua-type-error]({{< relref "/languages/lua/lua-type-error" >}}) — type error
- [lua-module-error]({{< relref "/languages/lua/lua-module-error" >}}) — module not found
