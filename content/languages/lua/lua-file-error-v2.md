---
title: "[Solution] Lua No Such File or Directory Error"
description: "Fix Lua file not found errors. Handle missing files, incorrect paths, and file operation failures."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The error `No such file or directory` occurs when Lua cannot open a file at the specified path. This happens with `io.open`, `dofile`, `loadfile`, and `require`.

## Common Causes

- File path does not exist
- Incorrect relative path
- Working directory changed
- File permissions prevent access
- Filename typo

## How to Fix

```lua
-- WRONG: No existence check
local f = io.open("data.txt", "r")  -- Returns nil if not found
local content = f:read("*a")  -- Error: attempt to index nil

-- CORRECT: Check if file opened
local f, err = io.open("data.txt", "r")
if not f then
    print("Error opening file: " .. err)
    return
end
local content = f:read("*a")
f:close()
```

```lua
-- WRONG: Hardcoded path
dofile("/home/user/data/config.lua")  -- Fails on other machines

-- CORRECT: Use relative paths or find script directory
local script_dir = arg[0]:match("(.*/)")  or "./"
dofile(script_dir .. "config.lua")
```

```lua
-- WRONG: Not checking require path
local config = require("config")  -- Error if module path wrong

-- CORRECT: Set package.path
package.path = package.path .. ";./scripts/?.lua;./lib/?.lua"
local config = require("config")
```

## Examples

```lua
-- Example 1: Safe file read
function read_file(path)
    local f, err = io.open(path, "r")
    if not f then
        return nil, err
    end
    local content = f:read("*a")
    f:close()
    return content
end

-- Example 2: File existence check
function file_exists(path)
    local f = io.open(path, "r")
    if f then
        f:close()
        return true
    end
    return false
end

-- Example 3: Write file safely
function write_file(path, content)
    local f, err = io.open(path, "w")
    if not f then
        return false, err
    end
    f:write(content)
    f:close()
    return true
end
```

## Related Errors

- [lua-module-error]({{< relref "/languages/lua/lua-module-error" >}}) — module not found
- [lua-runtime-error]({{< relref "/languages/lua/lua-runtime-error" >}}) — runtime error
- [lua-index-error]({{< relref "/languages/lua/lua-index-error" >}}) — index nil
