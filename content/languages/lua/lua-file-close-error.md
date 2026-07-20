---
title: "[Solution] Lua file:close Handle Error Fix"
description: "Fix Lua file:close errors when closing file handles. Learn proper file lifecycle management."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1127
---

## What This Error Means

A file:close error occurs when closing a file handle that is already closed, invalid, or has pending buffered writes that fail. Proper file handle management prevents data corruption and resource leaks.

## Common Causes

- Closing a file handle that is already closed
- Trying to close the default I/O handles (io.stdin, io.stdout, io.stderr)
- Buffered write data lost when file closed due to errors
- Using a file handle after closing it
- File handle garbage collection before explicit close

## How to Fix

```lua
-- WRONG: Closing a file twice
local f = io.open("test.txt", "w")
f:write("data")
f:close()
f:close()  -- Error: attempt to use a closed file

-- CORRECT: Check if handle is valid
local f = io.open("test.txt", "w")
if f then
    f:write("data")
    f:close()
    if f:close() then
        -- Already closed
    end
end
```

```lua
-- WRONG: Using file after closing
local f = io.open("test.txt", "r")
local content = f:read("*a")
f:close()
print(f:read("*a"))  -- Error: closed file

-- CORRECT: Read all data before closing
local f = io.open("test.txt", "r")
local content = f:read("*a")
f:close()
-- Use content after close
print(content)
```

```lua
-- WRONG: Not closing files in error paths
local f = io.open("test.txt", "w")
f:write("data")
-- Error occurs before close
if some_condition then
    error("Something went wrong")  -- File left open!
end
f:close()

-- CORRECT: Use xpcall or explicit cleanup
local f, err = io.open("test.txt", "w")
if f then
    local ok, save_err = xpcall(function()
        f:write("data")
        if some_condition then
            error("Something went wrong")
        end
    end, function(e)
        f:close()
        return e
    end)
    if ok then
        f:close()
    end
end
```

```lua
-- Safe file:close pattern
local function safe_close(f)
    if f then
        local ok, err = f:close()
        if not ok then
            warn("Failed to close file: " .. tostring(err))
        end
    end
end

local f = io.open("test.txt", "w")
-- ... write to file ...
safe_close(f)
```

```lua
-- Automatic close pattern
local function with_file(path, mode, fn)
    local f, err = io.open(path, mode)
    if not f then
        return nil, err
    end
    local ok, result = pcall(fn, f)
    f:close()
    if ok then
        return result
    else
        error(result)
    end
end

with_file("test.txt", "w", function(f)
    f:write("Hello, World!\n")
end)
```

## Examples

```lua
local function read_file_safe(path)
    local f, err = io.open(path, "r")
    if not f then return nil, err end
    local content = f:read("*a")
    f:close()
    return content
end

local content, err = read_file_safe("data.txt")
if content then
    print(content)
else
    print("Error:", err)
end
```

## Related Errors

- [Lua IO error](lua-io-error) - IO issue
- [Lua file error](lua-file-error) - file issue
- [Lua runtime error](lua-runtime-error) - runtime issue
