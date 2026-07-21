---
title: "[Solution] Lua Json Encode Error"
description: "Fix Lua JSON encoding errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

JSON encoding errors occur when converting Lua tables to JSON.

## Common Causes

- Circular references
- Unsupported types
- Invalid table structure
- Function values

## How to Fix

### 1. Use json library correctly

```lua
local json = require("cjson")
local str = json.encode({name = "test", value = 42})
```

### 2. Handle errors

```lua
local function safeEncode(data)
  local ok, result = pcall(json.encode, data)
  if ok then
    return result
  else
    return nil, result
  end
end
```

## Examples

```lua
-- Encode with options
local json = require("cjson")
json.encode_sparse_array(true)

local data = {
  name = "test",
  numbers = {1, 2, 3},
  nested = {key = "value"}
}

local encoded = json.encode(data)
print(encoded)
```

## Related Errors

- [Json decode error](/languages/lua/lua-json-decode-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Type error](/languages/lua/lua-type-error)
