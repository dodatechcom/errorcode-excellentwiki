---
title: "[Solution] Lua require Module Path Error Fix"
description: "Fix Lua require errors when module path resolution fails."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1113
---

## What This Error Means

A require path error occurs when Lua cannot find a module because the module is not in package.path or package.cpath. Lua searches for modules in the paths specified by package.searchers.

## Common Causes

- Module not installed in any search path
- Incorrect module name (wrong case, wrong separator)
- package.path not including the correct directory
- Using . instead of / as path separator for module names
- C modules not found in package.cpath

## How to Fix

```lua
-- WRONG: requiring a non-existent module
local m = require("non_existent_module")  -- module 'non_existent_module' not found

-- CORRECT: Check if module is available
local ok, mod = pcall(require, "non_existent_module")
if ok then
    -- use mod
else
    print("Module not found:", mod)
end
```

```lua
-- WRONG: Wrong module name case
local json = require("JSON")  -- May be lowercase 'json'

-- CORRECT: Check the actual module name
-- On Linux, filenames are case-sensitive
local json = require("json")
```

```lua
-- WRONG: Using nested module with wrong separator
require("my.module.sub")  -- Looks for my/module/sub.lua

-- CORRECT: Use dots for directory separators
require("my.module")  -- Looks for my/module.lua
```

```lua
-- WRONG: Not adding custom paths
local mylib = require("mylib")  -- Not in default paths

-- CORRECT: Add path before requiring
package.path = package.path .. ";/path/to/?.lua"
package.path = package.path .. ";/path/to/?/init.lua"
require("mylib")  -- Now found
```

```lua
-- Check and modify search paths
print("Lua search paths:")
for path in package.path:gmatch("[^;]+") do
    print("  " .. path)
end

-- Add current directory
package.path = "./?.lua;" .. package.path
```

## Examples

```lua
local function require_safe(name)
    local ok, result = pcall(require, name)
    if ok then
        return result
    end
    print("Could not load module:", name)
    print("Reason:", result)
    return nil
end

local json = require_safe("json")
```

## Related Errors

- [Lua module error](lua-module-error) - module issue
- [Lua module not found](lua-module-not-found) - module not found
- [Lua runtime error](lua-runtime-error) - runtime issue
