---
title: "[Solution] Lua Module System Deprecation Error Fix"
description: "Fix Lua module system errors when using the deprecated module() function."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1114
---

## What This Error Means

A module system error occurs when using the deprecated module() function (removed in Lua 5.2) or when defining modules incorrectly. Modern Lua uses table-based module patterns instead.

## Common Causes

- Using module() function in Lua 5.2+ (it no longer exists)
- Not returning the module table from the module file
- Confusing module() with require
- Global namespace pollution from module definitions
- Incorrect module file structure

## How to Fix

```lua
-- WRONG: Using deprecated module() function
module("mymodule", package.seeall)  -- Not available in Lua 5.2+
function greet() print("Hello") end

-- CORRECT: Use table-based module pattern
local mymodule = {}
function mymodule.greet() print("Hello") end
return mymodule
```

```lua
-- WRONG: Not returning the module table
-- In mymodule.lua:
local M = {}
M.hello = function() print("hi") end
-- Forgot: return M

-- CORRECT: Always return the module
local M = {}
M.hello = function() print("hi") end
return M
```

```lua
-- WRONG: Global pollution
-- In mylib.lua:
function helper() print("helper") end  -- Global!
_G.public_func = function() print("public") end  -- Global!
local M = {}
M.do_stuff = function() helper() end
return M

-- CORRECT: Keep everything local
local function helper() print("helper") end
local M = {}
M.do_stuff = function() helper() end
return M
```

```lua
-- Modern module pattern with submodules
-- In lib/utils.lua:
local utils = {}

function utils.trim(s)
    return (s:gsub("^%s*(.-)%s*$", "%1"))
end

function utils.split(s, sep)
    sep = sep or ","
    local result = {}
    for part in s:gmatch("[^" .. sep .. "]+") do
        table.insert(result, part)
    end
    return result
end

return utils
```

```lua
-- Module with private state
local counter_module = {}

local counter = 0

function counter_module.next()
    counter = counter + 1
    return counter
end

function counter_module.reset()
    counter = 0
end

return counter_module
```

## Examples

```lua
-- mymath.lua
local mymath = {}

function mymath.add(a, b) return a + b end
function mymath.sub(a, b) return a - b end

local function validate(n)
    assert(type(n) == "number", "Expected number")
end

return mymath

-- Usage:
local m = require("mymath")
print(m.add(3, 4))  -- 7
```

## Related Errors

- [Lua module error](lua-module-error) - module issue
- [Lua module not found](lua-module-not-found) - module not found
- [Lua env error](lua-env-error) - environment issue
