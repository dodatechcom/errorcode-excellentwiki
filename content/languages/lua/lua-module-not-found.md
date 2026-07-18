---
title: "[Solution] Lua Module Not Found Require Failed Fix"
description: "Fix Lua 'module not found' errors when require fails. Learn why module loading fails and how to configure package.path correctly."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

The `module not found` error in Lua occurs when `require` cannot locate a Lua module file. Lua searches for modules using `package.path` for Lua files and `package.cpath` for C shared libraries. If the module is not found in any search path, `require` raises an error listing every location it checked.

## Why It Happens

- The module is not installed in any directory on `package.path`
- `package.path` does not include the directory where the module resides
- The module file name does not match the `require` argument
- The module is a C library and `package.cpath` is misconfigured
- The current working directory changed after module paths were set
- A custom loader was registered that fails to find the module
- The module is in a subdirectory that is not reflected in the path pattern

## How to Fix It

### Check and update package.path

```lua
-- WRONG: Module not in default path
local json = require("json")  -- module not found

-- CORRECT: Add the module directory to package.path
package.path = "/usr/local/lib/lua/?.lua;" .. package.path
local json = require("json")
```

### Use pcall to handle missing modules gracefully

```lua
-- WRONG: require throws an error on failure
local ok, lfs = pcall(require, "lfs")
if not ok then
    error("lfs is required")  -- ungraceful exit
end

-- CORRECT: Provide a fallback or clear message
local ok, lfs = pcall(require, "lfs")
if not ok then
    print("Warning: lfs not found, using fallback directory listing")
    lfs = nil
end
```

### Verify the module search path

```lua
-- WRONG: Not checking where Lua searches
local result = require("mylib")  -- error

-- CORRECT: Inspect package.path to debug
print(package.path)
for path in package.path:gmatch("[^;]+") do
    print("Checking: " .. path)
end
```

### Use package.searchpath for explicit lookup

```lua
-- WRONG: Blind require without knowing the path
local mod = require("mylib")

-- CORRECT: Find the module file path first
local filepath, err = package.searchpath("mylib", package.path)
if filepath then
    print("Module found at: " .. filepath)
    local mod = require("mylib")
else
    print("Module not found: " .. tostring(err))
end
```

### Handle C modules with package.cpath

```lua
-- WRONG: C module not in cpath
local ffi = require("mylib")  -- fails if .so/.dll not found

-- CORRECT: Configure cpath for your platform
package.cpath = "/usr/local/lib/lua/5.4/?.so;" .. package.cpath
local ok, mylib = pcall(require, "mylib")
if ok then
    -- use mylib
end
```

## Common Mistakes

- Not understanding that `require` caches modules, so changing `package.path` after the first failed require does not retry
- Using the wrong module name (case-sensitive on Linux, case-insensitive on Windows)
- Forgetting that `require("a.b")` looks for file `a/b.lua`, not `a.b.lua`
- Installing a Lua module with LuaRocks but running the script with a different Lua version
- Setting `package.path` with relative paths that break when the working directory changes

## Related Pages

- [Lua File Not Found](lua-file-not-found-v2) - file open failed
- [Lua Nil Call Error](lua-nil-call-error) - calling nil function
- [Lua Nil Index Error](lua-nil-index-error) - indexing nil value
- [Lua I/O Error](lua-io-error) - file read/write error
