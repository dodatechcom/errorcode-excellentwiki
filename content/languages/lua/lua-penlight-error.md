---
title: "[Solution] Lua Penlight Error"
description: "Fix Lua Penlight library errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Penlight errors occur when using the Penlight library incorrectly.

## Common Causes

- Missing module
- Wrong function signature
- File path error
- Table operation error

## How to Fix

### 1. Load penlight modules

```lua
local Path = require("pl.path")
local File = require("pl.file")
local Tablex = require("pl.tablex")
```

### 2. Handle penlight errors

```lua
local function safeReadFile(path)
  local ok, content = pcall(File.read, path)
  if ok then
    return content
  else
    return nil, content
  end
end
```

## Examples

```lua
-- Safe file operations with Penlight
local File = require("pl.file")
local Path = require("pl.path")

local function copyFile(src, dest)
  local content = File.read(src)
  if not content then
    return false, "Cannot read source"
  end
  
  local ok, err = File.write(dest, content)
  return ok, err
end

-- Table operations
local Tablex = require("pl.tablex")
local data = {1, 2, 3, 4, 5}
local filtered = Tablex.filter(function(x) return x > 2 end, data)
```

## Related Errors

- [File not found error](/languages/lua/lua-file-not-found-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Type error](/languages/lua/lua-type-error)
