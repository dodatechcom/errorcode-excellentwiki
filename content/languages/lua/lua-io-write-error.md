---
title: "[Solution] Lua Io Write Error"
description: "Fix Lua io.write errors when writing to files."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Io write errors occur when writing to files incorrectly.

## Common Causes

- File not opened for writing
- Disk full
- Invalid file handle
- Permission denied

## How to Fix

### 1. Check file mode

```lua
local f = io.open(path, "w")
if f then
  f:write(data)
  f:close()
end
```

### 2. Handle write errors

```lua
local function safeWrite(f, data)
  if f then
    local ok, err = pcall(function() f:write(data) end)
    return ok, err
  end
  return false, "No file handle"
end
```

## Examples

```lua
-- Write data safely
local function writeFile(path, content)
  local f, err = io.open(path, "w")
  if f == nil then
    return false, err
  end
  
  local ok, writeErr = pcall(function() f:write(content) end)
  f:close()
  
  return ok, writeErr
end

local ok, err = writeFile("output.txt", "Hello World")
if not ok then
  print("Write failed: " .. tostring(err))
end
```

## Related Errors

- [Io open error](/languages/lua/lua-io-open-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Permission denied error](/languages/lua/lua-permission-denied-error)
