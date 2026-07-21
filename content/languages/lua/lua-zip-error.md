---
title: "[Solution] Lua Zip Error"
description: "Fix Lua zip/archive handling errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Zip errors occur when working with zip archives.

## Common Causes

- Corrupt archive
- Missing zip library
- Invalid file path
- Archive in use

## How to Fix

### 1. Load zip library

```lua
local zip = require("zip")
```

### 2. Handle zip errors

```lua
local function safeOpenZip(path)
  local ok, archive = pcall(zip.open, path)
  if ok then
    return archive
  else
    return nil, archive
  end
end
```

## Examples

```lua
-- Extract from zip
local function extractFile(zipPath, fileName)
  local zip = require("zip")
  local archive, err = zip.open(zipPath)
  if not archive then
    return nil, err
  end
  
  local file = archive:open(fileName)
  if not file then
    archive:close()
    return nil, "File not in archive"
  end
  
  local content = file:read("*a")
  file:close()
  archive:close()
  
  return content
end
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [File not found error](/languages/lua/lua-file-not-found-error)
- [Io open error](/languages/lua/lua-io-open-error)
