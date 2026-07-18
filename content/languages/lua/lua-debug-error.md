---
title: "[Solution] Lua Debug Getinfo Error Fix for Debug Library"
description: "Fix Lua debug.getinfo errors and debug library failures. Learn why debug introspection fails and how to use debug safely."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Lua debug.getinfo error occurs when the debug library's introspection functions receive invalid arguments or attempt to inspect a function that cannot be debugged. The debug library provides powerful reflection capabilities but has strict requirements for its parameters.

## Why It Happens

- Passing an invalid stack level to `debug.getinfo`
- Using a function reference that is no longer valid
- Calling debug functions in a coroutine with an invalid level
- Passing a non-function, non-integer argument to `debug.getinfo`
- The Lua build disables debug features with `LUAI_MAXCCALLS` or compile flags
- Attempting to inspect a C function with limited debug information

## How to Fix It

### Validate stack levels before calling getinfo

```lua
-- WRONG: Invalid stack level
local info = debug.getinfo(999)  -- level too deep

-- CORRECT: Check level bounds
local function safeGetInfo(level)
    local maxLevel = 0
    for i = 1, 100 do
        if not debug.getinfo(i) then
            maxLevel = i - 1
            break
        end
    end
    if level < 1 or level > maxLevel then
        return nil, "stack level out of range (max: " .. maxLevel .. ")"
    end
    return debug.getinfo(level)
end
```

### Use the correct argument format

```lua
-- WRONG: Wrong argument type
local info = debug.getinfo("invalid")  -- expects function or level number

-- CORRECT: Use numeric level or function reference
local info1 = debug.getinfo(1)  -- current function
local info2 = debug.getinfo(print)  -- specific function
```

### Check available debug fields before using them

```lua
-- WRONG: Assuming all fields are present
local info = debug.getinfo(1)
print(info.namewhat)  -- may be nil for anonymous functions

-- CORRECT: Check fields exist
local info = debug.getinfo(1)
if info then
    print("Function: " .. (info.name or "anonymous"))
    print("Source: " .. (info.source or "unknown"))
    print("Line: " .. tostring(info.linedefined))
end
```

### Handle C function limitations

```lua
-- WRONG: Trying to get line info for C functions
local info = debug.getinfo(print)
print(info.currentline)  -- nil for C functions

-- CORRECT: Check if function is Lua or C
local info = debug.getinfo(print)
if info.what == "C" then
    print("This is a C function, limited debug info available")
elseif info.what == "Lua" then
    print("Source: " .. info.source .. " line " .. info.linedefined)
end
```

### Use debug functions safely in production

```lua
-- WRONG: Using debug library in hot path
local function process()
    for i = 1, 100000 do
        local info = debug.getinfo(1)  -- very slow
    end
end

-- CORRECT: Cache debug info or use it only for diagnostics
local cachedInfo = debug.getinfo(1, "nS")
local function process()
    -- use cachedInfo for logging, not in loop
end
```

## Common Mistakes

- Using `debug.getinfo` with a negative level, which is not valid
- Not realizing that `debug.getinfo` returns `nil` for invalid levels instead of raising an error
- Passing `debug.getinfo` the string `"f"` expecting a function when a level number was intended
- Assuming all fields like `nups`, `nparams`, and `isvararg` are available for all function types
- Using the debug library for production logging instead of dedicated logging frameworks

## Related Pages

- [Lua Stack Overflow](lua-stack-overflow) - recursion too deep
- [Lua Nil Index Error](lua-nil-index-error) - indexing nil value
- [Lua Nil Call Error](lua-nil-call-error) - calling nil value
- [Lua Runtime Error](lua-runtime-error) - general runtime issue
