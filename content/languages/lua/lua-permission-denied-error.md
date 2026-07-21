---
title: "[Solution] Lua Permission Denied Error"
description: "Fix Lua permission denied errors when accessing files."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Permission denied errors occur when file operations fail due to permissions.

## Common Causes

- Insufficient permissions
- File owned by another user
- Read-only filesystem
- File locked by process

## How to Fix

### 1. Check permissions

```lua
local function canRead(path)
  local f = io.open(path, "r")
  if f then
    f:close()
    return true
  end
  return false
end

local function canWrite(path)
  local f = io.open(path, "a")
  if f then
    f:close()
    return true
  end
  return false
end
```

### 2. Handle gracefully

```lua
local function safeRead(path)
  if not canRead(path) then
    return nil, "Permission denied"
  end
  local f = io.open(path, "r")
  local content = f:read("*a")
  f:close()
  return content
end
```

## Examples

```lua
-- Try with different paths
local function findWritablePath(paths)
  for _, path in ipairs(paths) do
    local f = io.open(path, "w")
    if f then
      f:close()
      return path
    end
  end
  return nil
end

local paths = {"/tmp/data.txt", "./data.txt", "../data.txt"}
local writable = findWritablePath(paths)
```

## Related Errors

- [Io open error](/languages/lua/lua-io-open-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [File not found error](/languages/lua/lua-file-not-found-error)
