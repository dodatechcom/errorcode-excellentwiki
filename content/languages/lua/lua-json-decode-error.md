---
title: "[Solution] Lua Json Decode Error"
description: "Fix Lua JSON decoding errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

JSON decoding errors occur when parsing JSON strings.

## Common Causes

- Invalid JSON syntax
- Missing quotes
- Trailing comma
- Unclosed brackets

## How to Fix

### 1. Validate before decoding

```lua
local function safeDecode(str)
  local json = require("cjson")
  local ok, result = pcall(json.decode, str)
  if ok then
    return result
  else
    return nil, result
  end
end
```

### 2. Handle decode errors

```lua
local json = require("cjson")
local data, err = json.decode('[{"name": "test"}, {"name": "test2"}]')
if data then
  for _, item in ipairs(data) do
    print(item.name)
  end
end
```

## Examples

```lua
-- Parse JSON safely
local function parseJson(str)
  if type(str) ~= "string" then
    return nil, "Not a string"
  end
  
  local json = require("cjson")
  local ok, result = pcall(json.decode, str)
  
  if not ok then
    return nil, "Invalid JSON: " .. tostring(result)
  end
  
  return result
end

local data, err = parseJson('{"key": "value"}')
```

## Related Errors

- [Json encode error](/languages/lua/lua-json-encode-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Syntax error](/languages/lua/lua-syntax-error)
