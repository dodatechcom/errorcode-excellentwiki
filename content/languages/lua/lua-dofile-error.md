---
title: "[Solution] Lua Dofile Dostring Error"
description: "Fix Lua dofile/dostring errors when executing files or strings."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Dofile/dostring errors occur when executing files or code strings.

## Common Causes

- File not found
- Syntax error in file
- Missing dostring function
- Non-string argument to dostring

## How to Fix

### 1. Check file exists before dofile

```lua
local function safeDofile(path)
  local f = io.open(path, "r")
  if f then
    f:close()
    return dofile(path)
  else
    return nil, "File not found: " .. path
  end
end
```

### 2. Use loadstring with error handling

```lua
local function safeDostring(code)
  local fn, err = loadstring(code)
  if fn then
    return fn()
  else
    return nil, err
  end
end
```

## Examples

```lua
-- Safe file execution
local function loadConfig(path)
  local ok, result = pcall(dofile, path)
  if ok then
    return result
  else
    print("Error loading config: " .. tostring(result))
    return {}
  end
end

local config = loadConfig("config.lua")
```

## Related Errors

- [Load error](/languages/lua/lua-load-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [File not found error](/languages/lua/lua-file-not-found-error)
