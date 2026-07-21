---
title: "[Solution] Lua Hmac Error"
description: "Fix Lua HMAC authentication errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

HMAC errors occur when computing HMAC signatures.

## Common Causes

- Missing hmac module
- Wrong key
- Algorithm mismatch
- Verification failed

## How to Fix

### 1. Load hmac module

```lua
local hmac = require("hmac")
```

### 2. Handle errors

```lua
local function safeHmac(key, data, algo)
  local ok, result = pcall(hmac.hmac, key, data, algo)
  if ok then
    return result
  else
    return nil, result
  end
end
```

## Examples

```lua
-- Compute HMAC
local hmac = require("hmac")

local key = "secret-key"
local data = "message"
local signature = hmac.hmac(key, data, "sha256")
print(signature)

-- Verify HMAC
local function verifyHmac(key, data, expected, algo)
  local signature = hmac.hmac(key, data, algo)
  return signature == expected
end
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)
