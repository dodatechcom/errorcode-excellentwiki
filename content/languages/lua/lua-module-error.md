---
title: "[Solution] Lua Module Error Fix"
description: "Fix Lua module errors. Learn why module loading fails and how to handle require properly."
languages: ["lua"]
severities: ["error"]
error-types: ["load-error"]
tags: ["module", "require", "load", "lua"]
weight: 5
---

## What This Error Means

A Lua module error occurs when the require function cannot find or load a module. This can happen due to missing files, wrong paths, or circular dependencies.

## Common Causes

- Module file not found
- Wrong module path
- Circular dependencies
- Module not returning value

## How to Fix

```lua
-- WRONG: Module not found
local mylib = require("nonexistent_module")  -- error

-- CORRECT: Check module exists
local ok, mylib = pcall(require, "my_module")
if ok then
    mylib.doSomething()
end
```

```lua
-- WRONG: Circular dependency
-- module_a.lua: local b = require("module_b")
-- module_b.lua: local a = require("module_a")

-- CORRECT: Break cycle with lazy loading
-- module_a.lua
local b
local function init()
    b = require("module_b")
end
```

## Examples

```lua
-- Example 1: Basic module
-- mymodule.lua
local M = {}
function M.greet(name)
    return "Hello, " .. name
end
return M

-- Usage
local mymodule = require("mymodule")
print(mymodule.greet("World"))

-- Example 2: Module with fallback
local ok, json = pcall(require, "cjson")
if not ok then
    json = require("dkjson")
end

-- Example 3: Custom require path
package.path = "./lib/?.lua;" .. package.path
local mylib = require("mylib")
```

## Related Errors

- [Lua file error](lua-file-error) - file not found
- [Lua runtime error](lua-runtime-error) - runtime issue
- [Lua stack overflow](lua-stack-overflow) - stack overflow
