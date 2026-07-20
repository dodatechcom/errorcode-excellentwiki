---
title: "[Solution] Lua xpcall Protected Call Error Fix"
description: "Fix Lua xpcall errors when using protected calls with custom error handlers."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1133
---

## What This Error Means

An xpcall error occurs when using xpcall for protected function calls with a custom error handler. Common issues include the error handler itself failing, wrong argument order, or confusion with pcall.

## Common Causes

- Error handler function raising its own errors
- Wrong argument order (xpcall uses fn, msghandler, ...args)
- Confusing xpcall with pcall (pcall uses fn, ...args)
- Not returning the error handler's result
- Error handler consuming the error message

## How to Fix

```lua
-- WRONG: Error handler that fails
local function handler(err)
    error("Handler failed: " .. err)  -- This itself errors!
end

local ok, result = xpcall(function()
    error("Original error")
end, handler)
-- "Handler failed: Original error" is the new error

-- CORRECT: Safe error handler
local function handler(err)
    if type(err) == "string" then
        return "Error: " .. err
    end
    return "Error: " .. tostring(err)
end

local ok, result = xpcall(function()
    error("Original error")
end, handler)
print(result)  -- "Error: Original error"
```

```lua
-- WRONG: Confusing pcall and xpcall argument order
-- pcall(fn, ...) - error handling is implicit
-- xpcall(fn, msghandler, ...) - explicit error handler

-- CORRECT: xpcall with proper arguments
local results = { xpcall(
    function(a, b) return a / b end,  -- fn
    debug.traceback,                   -- msghandler
    10, 0                              -- ...args
)}

if results[1] then
    print("Result:", results[2])
else
    print("Error:", results[2])  -- Includes traceback
end
```

```lua
-- WRONG: Not using error handler result
local function my_handler(err)
    return "CUSTOM: " .. tostring(err)
end

local ok, msg = xpcall(function()
    error("test error")
end, my_handler)

print(msg)  -- "CUSTOM: test error" (handler result)
```

```lua
-- Using debug.traceback in xpcall
local function risky(a, b)
    if b == 0 then
        error("Division by zero")
    end
    return a / b
end

local ok, result = xpcall(risky, debug.traceback, 10, 0)
if not ok then
    print("Full traceback:")
    print(result)  -- Includes line numbers and call stack
end
```

```lua
-- Custom error handler with context
local function error_logger(err)
    local info = debug.getinfo(2, "nS")
    local location = string.format("%s:%d",
        info.short_src or "?",
        info.currentline or 0)
    return string.format("[%s] %s", location, tostring(err))
end

local ok, err = xpcall(function()
    error("Something broke")
end, error_logger)

if not ok then
    print(err)  -- "[@script.lua:10] Something broke"
end
```

## Examples

```lua
local function safe_divide(a, b)
    local ok, result = xpcall(
        function()
            if b == 0 then error("division by zero") end
            return a / b
        end,
        debug.traceback
    )
    if ok then
        return result
    else
        return nil, result  -- Error with traceback
    end
end

local res, err = safe_divide(10, 0)
if err then print(err) end
```

## Related Errors

- [Lua runtime error](lua-runtime-error) - runtime issue
- [Lua nil call error](lua-nil-call-error) - nil call
- [Lua error](lua-runtime-error-v2) - runtime issue
