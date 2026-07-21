---
title: "[Solution] Lua Io Seek Error"
description: "Fix Lua io.seek errors when seeking in files."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Io seek errors occur when io.seek is called incorrectly.

## Common Causes

- Seeking in text mode
- Invalid whence argument
- Position out of bounds
- Seek on non-seekable file

## How to Fix

### 1. Use binary mode for seeking

```lua
local f = io.open(path, "rb")
if f then
  f:seek("set", 0)  -- Seek to beginning
  local data = f:read("*a")
  f:close()
end
```

### 2. Validate whence

```lua
local function safeSeek(f, whence, offset)
  if f then
    local validWhence = {set = true, cur = true, end = true}
    if validWhence[whence] then
      return f:seek(whence, offset)
    end
  end
  return nil
end
```

## Examples

```lua
-- Read file from middle
local function readFromMiddle(path)
  local f = io.open(path, "rb")
  if f then
    local size = f:seek("end")
    f:seek("set", math.floor(size / 2))
    local data = f:read("*a")
    f:close()
    return data
  end
  return nil
end
```

## Related Errors

- [Io open error](/languages/lua/lua-io-open-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
