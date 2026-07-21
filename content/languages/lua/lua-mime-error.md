---
title: "[Solution] Lua Mime Error"
description: "Fix Lua MIME encoding/decoding errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

MIME errors occur when encoding or decoding MIME data.

## Common Causes

- Wrong encoding format
- Invalid base64 input
- Missing mime module
- Line length error

## How to Fix

### 1. Use mime module correctly

```lua
local mime = require("mime")
local encoded = mime.b64("Hello World")
local decoded = mime.unb64(encoded)
```

### 2. Handle errors

```lua
local function safeEncode(data)
  local ok, result = pcall(mime.b64, data)
  if ok then
    return result
  else
    return nil, result
  end
end
```

## Examples

```lua
-- Base64 encoding
local mime = require("mime")

local original = "Hello, World!"
local encoded = mime.b64(original)
local decoded = mime.unb64(encoded)

print("Original:", original)
print("Encoded:", encoded)
print("Decoded:", decoded)
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)
