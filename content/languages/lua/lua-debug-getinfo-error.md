---
title: "[Solution] Lua debug.getinfo Introspection Error Fix"
description: "Fix Lua debug.getinfo errors when inspecting function and stack frame information."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1130
---

## What This Error Means

A debug.getinfo error occurs when requesting debug information about a function or stack level. Common issues include invalid stack levels, requesting unsupported info fields, or passing wrong argument types.

## Common Causes

- Requesting a stack level that doesn't exist
- Passing an invalid what string (wrong field specifiers)
- Calling debug.getinfo on a non-function value
- Not understanding the returned table structure
- Performance impact of debug.getinfo in tight loops

## How to Fix

```lua
-- WRONG: Stack level out of range
local info = debug.getinfo(100)  -- Stack level doesn't exist

-- CORRECT: Check if info is valid
local info = debug.getinfo(2)
if info then
    print("Function:", info.name)
else
    print("No info at that level")
end
```

```lua
-- WRONG: Passing wrong field specifiers
-- Valid specifiers: 'n' (name), 'f' (function), 'l' (line),
-- 'L' (lines), 'S' (source), 'u' (nups), 't' (tailcall)
local info = debug.getinfo(1, "xyz")  -- Invalid! Only valid chars are kept

-- CORRECT: Use valid specifiers
local info = debug.getinfo(1, "nSl")  -- name, source, currentline
print(info.name)        -- function name
print(info.source)      -- source file
print(info.currentline) -- current line number
```

```lua
-- WRONG: Trying to get info from a non-function
local info = debug.getinfo("not a function")  -- Error

-- CORRECT: Ensure it's a function
local fn = function() end
local info = debug.getinfo(fn)
if info then
    print("Defined at line:", info.linedefined)
end
```

```lua
-- Practical debugging with getinfo
function trace()
    local level = 2
    local info = debug.getinfo(level, "nSl")
    if info then
        print(string.format("Called from %s (%s:%d)",
            info.name or "unknown",
            info.short_src,
            info.currentline))
    end
end

function foo()
    bar()
end

function bar()
    trace()  -- "Called from foo (debug.lua:22)"
end

foo()
```

```lua
-- Enumerate stack trace
local function stack_trace()
    local level = 1
    while true do
        local info = debug.getinfo(level, "nSl")
        if not info then break end
        print(string.format("[%d] %s in %s at line %d",
            level,
            info.name or "?",
            info.short_src or "?",
            info.currentline or 0))
        level = level + 1
    end
end
```

## Examples

```lua
local function get_caller_name()
    local info = debug.getinfo(3, "n")
    return info and info.name or "unknown"
end

function example()
    print("Called by:", get_caller_name())
end

example()  -- "Called by: unknown" (called from top-level)
```

## Related Errors

- [Lua debug error](lua-debug-error) - debug issue
- [Lua runtime error](lua-runtime-error) - runtime issue
- [Lua error](lua-runtime-error-v2) - runtime issue
