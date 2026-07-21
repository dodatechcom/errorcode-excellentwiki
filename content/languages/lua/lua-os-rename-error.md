---
title: "[Solution] Lua Os Rename Error"
description: "Fix Lua os.rename errors when renaming files."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Os rename errors occur when os.rename fails.

## Common Causes

- Source does not exist
- Destination already exists
- Permission denied
- Different filesystems

## How to Fix

### 1. Check source exists

```lua
local function fileExists(path)
  local f = io.open(path, "r")
  if f then
    f:close()
    return true
  end
  return false
end
```

### 2. Handle rename safely

```lua
local function safeRename(old, new)
  if not fileExists(old) then
    return false, "Source not found"
  end
  local ok, err = os.rename(old, new)
  return ok, err
end
```

## Examples

```lua
-- Move file
local function moveFile(oldPath, newPath)
  local ok, err = os.rename(oldPath, newPath)
  if not ok then
    -- Try copy and delete
    local content = readFile(oldPath)
    if content then
      writeFile(newPath, content)
      os.remove(oldPath)
      return true
    end
  end
  return ok, err
end
```

## Related Errors

- [File not found error](/languages/lua/lua-file-not-found-error)
- [Permission denied error](/languages/lua/lua-permission-denied-error)
- [Runtime error](/languages/lua/lua-runtime-error)
