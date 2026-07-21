---
title: "[Solution] Lua File Not Found Error"
description: "Fix Lua file not found errors when accessing non-existent files."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

File not found errors occur when attempting to access files that don't exist.

## Common Causes

- File path incorrect
- File deleted
- Wrong working directory
- Case sensitivity

## How to Fix

### 1. Check file exists first

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

### 2. Create default file

```lua
local function ensureFile(path, defaultContent)
  if not fileExists(path) then
    local f = io.open(path, "w")
    if f then
      f:write(defaultContent or "")
      f:close()
    end
  end
end
```

## Examples

```lua
-- Load file with fallback
local function loadWithFallback(path, fallback)
  if fileExists(path) then
    return dofile(path)
  end
  return fallback
end

local config = loadWithFallback("config.lua", {debug = false})
```

## Related Errors

- [Io open error](/languages/lua/lua-io-open-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Permission denied error](/languages/lua/lua-permission-denied-error)
