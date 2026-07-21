---
title: "[Solution] Lua Os Remove Error"
description: "Fix Lua os.remove errors when deleting files."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Os remove errors occur when os.remove fails.

## Common Causes

- File does not exist
- Permission denied
- Directory not empty
- File in use

## How to Fix

### 1. Check file exists

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

### 2. Handle removal safely

```lua
local function safeRemove(path)
  if not fileExists(path) then
    return false, "File not found"
  end
  local ok, err = os.remove(path)
  return ok, err
end
```

## Examples

```lua
-- Remove with confirmation
local function removeIfExists(path)
  if fileExists(path) then
    local ok, err = os.remove(path)
    if ok then
      print("Removed:", path)
    else
      print("Error removing:", err)
    end
  end
end
```

## Related Errors

- [File not found error](/languages/lua/lua-file-not-found-error)
- [Permission denied error](/languages/lua/lua-permission-denied-error)
- [Runtime error](/languages/lua/lua-runtime-error)
