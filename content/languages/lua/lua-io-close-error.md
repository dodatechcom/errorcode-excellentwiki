---
title: "[Solution] Lua Io Close Error"
description: "Fix Lua io.close errors when closing files."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Io close errors occur when io.close is called on invalid file handles.

## Common Causes

- File already closed
- Invalid file handle
- io.close on stdin/stdout
- Double close

## How to Fix

### 1. Check if file is open

```lua
local function safeClose(f)
  if f and f.close then
    f:close()
  end
end
```

### 2. Use pcall for safety

```lua
local function closeFile(f)
  if f then
    pcall(function() f:close() end)
  end
end
```

## Examples

```lua
-- Safe file operations
local function processFile(path)
  local f = io.open(path, "r")
  if not f then
    return nil, "Cannot open file"
  end
  
  local content = f:read("*a")
  f:close()  -- Close immediately after reading
  
  return content
end
```

## Related Errors

- [Io open error](/languages/lua/lua-io-open-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
