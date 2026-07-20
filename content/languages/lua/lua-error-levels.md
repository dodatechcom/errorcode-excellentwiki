---
title: "[Solution] Lua Error Level and Error Function Error Fix"
description: "Fix Lua error function level errors. Learn how to use error levels to control error location reporting."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1132
---

## What This Error Means

An error level error occurs when using the error function with the wrong level argument. The level parameter controls where Lua reports the error occurred, and incorrect values can hide the real error location.

## Common Causes

- Passing an invalid level value (0 or negative)
- Level too high for the current call stack
- Not using level=2 in wrapper functions
- Forgetting to set level in validation functions
- Confusing error level with error object

## How to Fix

```lua
-- WRONG: Level 0 is invalid
error("Something went wrong", 0)  -- Error: level out of range

-- CORRECT: Use level 1 (default, current function) or higher
error("Something went wrong")     -- Level 1 (same as error(msg, 1))
error("Something went wrong", 2)  -- Reports caller's location
```

```lua
-- WRONG: Validation function hiding error location
function check_positive(n)
    if n <= 0 then
        error("Must be positive")  -- Reports check_positive, not the caller!
    end
end

check_positive(-5)  -- Error says in 'check_positive'

-- CORRECT: Use level 2 to report caller
function check_positive(n)
    if n <= 0 then
        error("Must be positive", 2)  -- Reports the caller!
    end
end

check_positive(-5)  -- Error says at the line calling check_positive
```

```lua
-- WRONG: Level > stack depth
function deep()
    error("Too deep", 100)  -- Level beyond stack
end

deep()  -- Error: level out of range

-- CORRECT: Use reasonable level values
function deep()
    error("Error", 1)
end
```

```lua
-- Assert with proper levels
local function myassert(cond, msg)
    if not cond then
        error(msg or "assertion failed!", 2)  -- Reports assert caller
    end
end

local function process()
    myassert(false, "Processing failed")
end

process()  -- Reports process() line, not myassert()
```

```lua
-- Error level in nested wrappers
function validate(cond)
    if not cond then
        error("Validation failed", 3)  -- Skip validate AND caller
    end
end

function process()
    validate(false)  -- Error reports here (level 2)
end

-- Level 3 would report even higher up
```

## Examples

```lua
local function require_non_empty(str, name)
    if type(str) ~= "string" then
        error(name .. " must be a string", 2)
    end
    if str == "" then
        error(name .. " cannot be empty", 2)
    end
end

function create_user(name)
    require_non_empty(name, "name")
    print("Creating user:", name)
end

create_user("")  -- Error reports create_user line, not require_non_empty
```

## Related Errors

- [Lua runtime error](lua-runtime-error) - runtime issue
- [Lua pcall error](lua-capi-error) - pcall issue
- [Lua type error](lua-type-error) - type issue
