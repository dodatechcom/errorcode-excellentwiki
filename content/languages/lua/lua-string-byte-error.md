---
title: "[Solution] Lua String Byte Error"
description: "Fix Lua string.byte errors when converting characters to bytes."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

String byte errors occur when string.byte is called incorrectly.

## Common Causes

- Position out of range
- Non-string input
- Start greater than end
- Missing arguments

## How to Fix

### 1. Validate positions

```lua
local function safeByte(s, i, j)
  if type(s) ~= "string" then return nil end
  i = i or 1
  j = j or i
  if i < 1 or i > #s then return nil end
  return string.byte(s, i, j)
end
```

### 2. Get byte of first character

```lua
local s = "Hello"
local byte = string.byte(s)
print(byte)  -- 72 (ASCII for 'H')
```

## Examples

```lua
-- Get all bytes
local s = "abc"
local b1, b2, b3 = string.byte(s, 1, 3)
print(b1, b2, b3)  -- 97 98 99

-- Check character
local function isUpperCase(c)
  local b = string.byte(c)
  return b >= 65 and b <= 90
end
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)
