---
title: "[Solution] Lua Global Variable Error Fix"
description: "Fix Lua global variable errors. Learn why global variables cause issues and how to use locals properly."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Lua global variable error occurs when code relies on implicit globals or when globals collide. Lua globals are accessible everywhere and can cause unexpected behavior.

## Common Causes

- Accidental global creation
- Name collision between modules
- Missing local keyword
- Global pollution

## How to Fix

```lua
-- WRONG: Accidental global
function process()
    result = 42  -- Global variable created!
end

-- CORRECT: Use local
function process()
    local result = 42  -- Local variable
end
```

```lua
-- WRONG: Accessing undefined global
print(undefined_var)  -- nil, may cause issues

-- CORRECT: Use local with default
local value = undefined_var or "default"
```

## Examples

```lua
-- Example 1: Strict mode
local function strict()
    setmetatable(_G, {
        __index = function(t, k)
            error("Undefined global: " .. k, 2)
        end,
        __newindex = function(t, k, v)
            error("Assignment to undefined global: " .. k, 2)
        end
    })
end

-- Example 2: Module pattern
local M = {}
local private_var = "secret"

function M.public_function()
    return private_var
end

return M

-- Example 3: Local scope
do
    local temp = compute_value()
    use_value(temp)
end  -- temp is garbage collected
```

## Related Errors

- [Lua nil error](lua-nil-error) - nil access
- [Lua runtime error](lua-runtime-error) - runtime issue
- [Lua env error](lua-env-error) - environment error
