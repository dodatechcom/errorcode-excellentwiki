---
title: "[Solution] Lua Md5 Error"
description: "Fix Lua MD5 hashing errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

MD5 errors occur when computing MD5 hashes.

## Common Causes

- Missing md5 module
- Wrong input type
- Encoding error
- Hash verification failed

## How to Fix

### 1. Load md5 module

```lua
local md5 = require("md5")
```

### 2. Handle errors

```lua
local function safeMd5(data)
  local ok, hash = pcall(md5.hex, data)
  if ok then
    return hash
  else
    return nil, hash
  end
end
```

## Examples

```lua
-- Compute MD5 hash
local md5 = require("md5")

local data = "Hello, World!"
local hash = md5.hex(data)
print(hash)

-- Verify hash
local function verify(data, expectedHash)
  local hash = md5.hex(data)
  return hash == expectedHash
end
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)
