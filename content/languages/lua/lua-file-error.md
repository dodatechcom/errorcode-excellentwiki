---
title: "[Solution] Lua File Error Fix"
description: "Fix Lua file errors. Learn why file operations fail and how to handle IO properly."
languages: ["lua"]
severities: ["error"]
error-types: ["io-error"]
tags: ["file", "io", "open", "lua"]
weight: 5
---

## What This Error Means

A Lua file error occurs when file operations like open, read, or write fail. This can happen due to missing files, permission issues, or wrong file modes.

## Common Causes

- File does not exist
- Permission denied
- Wrong file mode
- Disk full

## How to Fix

```lua
-- WRONG: Not handling file errors
local file = io.open("data.txt", "r")
local content = file:read("*a")  -- May fail if file nil

-- CORRECT: Check file opened
local file = io.open("data.txt", "r")
if file then
    local content = file:read("*a")
    file:close()
else
    print("Cannot open file")
end
```

```lua
-- WRONG: Wrong file mode
local file = io.open("data.txt", "w")  -- Overwrites file

-- CORRECT: Use correct mode
local file = io.open("data.txt", "a")  -- Append
```

## Examples

```lua
-- Example 1: Safe file reading
local function read_file(path)
    local file = io.open(path, "r")
    if not file then return nil end
    local content = file:read("*a")
    file:close()
    return content
end

-- Example 2: Write file
local function write_file(path, content)
    local file = io.open(path, "w")
    if file then
        file:write(content)
        file:close()
        return true
    end
    return false
end

-- Example 3: Check file existence
local function file_exists(path)
    local file = io.open(path, "r")
    if file then
        file:close()
        return true
    end
    return false
end
```

## Related Errors

- [Lua runtime error](lua-runtime-error) - runtime issue
- [Lua module error](lua-module-error) - module not found
- [Lua argument error](lua-argument-error) - wrong argument
