---
title: "[Solution] Lua Cjson Error"
description: "Fix Lua cjson library errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Cjson errors occur when using the cjson library incorrectly.

## Common Causes

- Missing cjson module
- Invalid encode/decode
- Circular reference
- Large numbers

## How to Fix

### 1. Load cjson properly

```lua
local status, json = pcall(require, "cjson")
if not status then
  error("cjson not available")
end
```

### 2. Handle errors

```lua
local function safeJsonOp(fn, ...)
  local ok, result = pcall(fn, ...)
  if ok then
    return result
  else
    return nil, result
  end
end
```

## Examples

```lua
-- Safe cjson usage
local json = require("cjson")

local function encodeSafe(data)
  local ok, result = pcall(json.encode, data)
  if ok then
    return result
  else
    return nil, "Encode error: " .. tostring(result)
  end
end

local function decodeSafe(str)
  local ok, result = pcall(json.decode, str)
  if ok then
    return result
  else
    return nil, "Decode error: " .. tostring(result)
  end
end
```

## Related Errors

- [Json encode error](/languages/lua/lua-json-encode-error)
- [Json decode error](/languages/lua/lua-json-decode-error)
- [Runtime error](/languages/lua/lua-runtime-error)
