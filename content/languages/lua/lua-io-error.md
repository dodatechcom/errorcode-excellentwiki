---
title: "[Solution] Lua I/O Error Reading Writing File Fix"
description: "Fix Lua I/O errors when reading or writing files. Learn why file operations fail and how to handle I/O errors gracefully."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Lua I/O error occurs when a file read or write operation fails at the operating system level. The `io` library wraps standard C file operations, and errors are reported as "I/O error" with an OS-specific error code. Common messages include "Permission denied", "No space left on device", and "Broken pipe".

## Why It Happens

- The file system is full or the disk quota is exceeded
- File permissions prevent reading or writing
- The file was deleted or moved while a handle was open
- A pipe or socket was closed by the remote end
- The file handle was closed twice or used after being closed
- Network file system (NFS/SMB) connectivity was lost
- The file is too large for the operating system to handle

## How to Fix It

### Check file handles before use

```lua
-- WRONG: Not checking if open succeeded
local f = io.open("data.txt", "r")
local content = f:read("*all")  -- crashes if f is nil

-- CORRECT: Validate handle
local f, err, errcode = io.open("data.txt", "r")
if not f then
    print("Open failed: " .. err .. " (code: " .. tostring(errcode) .. ")")
    return
end
local content = f:read("*all")
f:close()
```

### Handle disk space errors when writing

```lua
-- WRONG: No error handling for write operations
local f = io.open("output.txt", "w")
for i = 1, 1000000 do
    f:write(string.rep("x", 1000) .. "\n")  -- may fail mid-write
end
f:close()

-- CORRECT: Check write results
local f, err = io.open("output.txt", "w")
if not f then error("Cannot open: " .. err) end
local ok = true
for i = 1, 1000000 do
    local bytes, err = f:write(string.rep("x", 1000) .. "\n")
    if not bytes then
        print("Write failed at line " .. i .. ": " .. err)
        ok = false
        break
    end
end
f:close()
```

### Flush output buffers to catch errors early

```lua
-- WRONG: Not flushing, errors caught at close
local f = io.open("output.txt", "w")
f:write("important data")
f:close()  -- error here, may lose data

-- CORRECT: Flush after critical writes
local f = io.open("output.txt", "w")
f:write("important data")
local ok, err = f:flush()
if not ok then
    print("Flush failed: " .. err)
end
f:close()
```

### Handle binary file operations safely

```lua
-- WRONG: Reading binary in text mode
local f = io.open("image.bin", "r")  -- text mode
local data = f:read("*all")  -- may corrupt binary data
f:close()

-- CORRECT: Use binary mode on Windows
local mode = io.type(f) == "file" and "rb" or "r"
local f = io.open("image.bin", "rb")
local data = f:read("*a")
f:close()
```

### Use protected calls for critical I/O

```lua
-- WRONG: Single failure stops all processing
local function processFiles(files)
    for _, file in ipairs(files) do
        local f = io.open(file, "r")
        local data = f:read("*all")  -- crashes on first failure
        f:close()
        transform(data)
    end
end

-- CORRECT: Handle each file independently
local function processFiles(files)
    for _, file in ipairs(files) do
        local ok, data = pcall(function()
            local f = io.open(file, "r")
            if not f then return nil, "cannot open" end
            local data = f:read("*all")
            f:close()
            return data
        end)
        if ok and data then
            transform(data)
        else
            print("Skipping " .. file .. ": " .. tostring(data))
        end
    end
end
```

## Common Mistakes

- Not flushing before close, losing buffered data silently
- Using `io.read()` without first opening a file with `io.open`
- Not closing file handles, leading to resource exhaustion
- Assuming text mode handles binary data correctly on Windows
- Not distinguishing between error codes from `io.open` and `file:read`

## Related Pages

- [Lua File Not Found](lua-file-not-found-v2) - file does not exist
- [Lua Module Not Found](lua-module-not-found) - module loading failed
- [Lua Nil Call Error](lua-nil-call-error) - calling nil value
- [Lua Nil Index Error](lua-nil-index-error) - indexing nil value
