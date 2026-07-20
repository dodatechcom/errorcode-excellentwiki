---
title: "[Solution] Lua traceback / debug.traceback Error Fix"
description: "Fix Lua traceback errors when generating stack traces for debugging."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1134
---

## What This Error Means

A traceback error occurs when debug.traceback fails to generate a call stack trace. Common issues include requesting traceback for a non-existent level, or the error message formatting not meeting expectations.

## Common Causes

- Passing an invalid thread (coroutine) to traceback
- Requesting traceback with negative or zero level
- Not using traceback as an error handler
- Traceback truncation for deep stacks
- Confusing debug.traceback with luaL_traceback (C API)

## How to Fix

```lua
-- WRONG: Passing a non-coroutine
local tb = debug.traceback("not a thread", 1)  -- Error

-- CORRECT: Pass a coroutine or nothing
local co = coroutine.create(function()
    coroutine.yield()
end)
coroutine.resume(co)
local tb = debug.traceback(co)
print(tb)
```

```lua
-- WRONG: Negative level
local tb = debug.traceback("message", -1)  -- Invalid

-- CORRECT: Level 1 or higher
local tb = debug.traceback("Error message", 1)
print(tb)
```

```lua
-- WRONG: Not using traceback as error handler
local ok, err = pcall(function()
    error("Something failed")
end)
print(err)  -- Just "Something failed" without trace

-- CORRECT: Use debug.traceback as handler with xpcall
local ok, err = xpcall(function()
    error("Something failed")
end, debug.traceback)
print(err)  -- Full traceback with line numbers
```

```lua
-- Custom traceback formatting
local function custom_traceback(msg, level)
    level = level or 1
    local trace = {}
    table.insert(trace, tostring(msg))
    while true do
        local info = debug.getinfo(level, "nSl")
        if not info then break end
        local line = string.format("  [%d] %s (%s:%d)",
            level,
            info.name or "?",
            info.short_src or "?",
            info.currentline or 0)
        table.insert(trace, line)
        level = level + 1
    end
    return table.concat(trace, "\n")
end

print(custom_traceback("Error!", 2))
```

```lua
-- Traceback for deep stacks
local function recurse(n)
    if n <= 0 then
        error("Bottom of recursion")
    end
    recurse(n - 1)
end

local ok, err = xpcall(function()
    recurse(10)
end, debug.traceback)
print(err)  -- Shows 10 levels of recursion
```

## Examples

```lua
local function safe_call(fn, ...)
    local results = { xpcall(fn, debug.traceback, ...) }
    if not results[1] then
        -- Log full traceback
        io.stderr:write("Error: " .. results[2] .. "\n")
    end
    return table.unpack(results)
end

safe_call(function()
    error("test")
end)
```

## Related Errors

- [Lua debug error](lua-debug-error) - debug issue
- [Lua xpcall error](lua-xpcall-error) - xpcall issue
- [Lua runtime error](lua-runtime-error) - runtime issue
