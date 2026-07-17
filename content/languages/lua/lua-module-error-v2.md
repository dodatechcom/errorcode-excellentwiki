---
title: "[Solution] Lua Module Not Found in package.path"
description: "Fix Lua module not found errors when require() fails. Configure package.path, check module names, and handle missing modules."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["module", "not-found", "require", "package", "path", "lua"]
weight: 5
---

## What This Error Means

The error `module 'X' not found` occurs when `require()` cannot locate a Lua module in the configured `package.path` or `package.cpath`.

## Common Causes

- Module not installed
- Incorrect module name
- Module not in package.path
- C module compilation failed
- Wrong Lua version

## How to Fix

```lua
-- WRONG: Module name typo
local json = require("jsno")  -- Error: module 'jsno' not found

-- CORRECT: Use correct module name
local json = require("json")
```

```lua
-- WRONG: Module not in path
local mymod = require("mymod")  -- Error if not in path

-- CORRECT: Add to package.path
package.path = package.path .. ";./modules/?.lua"
local mymod = require("mymod")
```

```lua
-- WRONG: C module path wrong
local ffi = require("ffi")  -- May need cpath

-- CORRECT: Set cpath for C modules
package.cpath = package.cpath .. ";./lib/?.so;./lib/?.dll"
local ffi = require("ffi")
```

## Examples

```lua
-- Example 1: Find where modules are searched
print(package.path)
print(package.cpath)

-- Example 2: Custom module loader
local function custom_require(name)
    local ok, module = pcall(require, name)
    if ok then return module end
    
    -- Try alternative paths
    local paths = {"./lib/?.lua", "./vendor/?.lua"}
    for _, path in ipairs(paths) do
        local full_path = path:gsub("?", name)
        local f = io.open(full_path)
        if f then
            f:close()
            return dofile(full_path)
        end
    end
    
    error("Module '" .. name .. "' not found")
end

-- Example 3: Conditional module loading
local function optional_require(name)
    local ok, module = pcall(require, name)
    return ok and module or nil
end

local json = optional_require("json")
if json then
    print("JSON available")
else
    print("JSON module not installed, using fallback")
end
```

## Related Errors

- [lua-file-error]({{< relref "/languages/lua/lua-file-error" >}}) — file not found
- [lua-runtime-error]({{< relref "/languages/lua/lua-runtime-error" >}}) — runtime error
- [lua-nil-error]({{< relref "/languages/lua/lua-nil-error" >}}) — nil call error
