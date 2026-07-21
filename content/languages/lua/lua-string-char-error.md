---
title: "[Solution] Lua String Char Error"
description: "Fix Lua string.char errors when converting bytes to characters."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

String char errors occur when string.char receives invalid byte values.

## Common Causes

- Byte value out of range (0-255)
- Non-integer argument
- Missing arguments
- Negative byte value

## How to Fix

### 1. Validate byte values

```lua
local function safeChar(...)
  local bytes = {...}
  local result = {}
  for _, b in ipairs(bytes) do
    if b >= 0 and b <= 255 then
      result[#result + 1] = string.char(b)
    end
  end
  return table.concat(result)
end
```

### 2. Convert byte to character

```lua
print(string.char(72))  -- "H"
print(string.char(72, 101, 108, 108, 111))  -- "Hello"
```

## Examples

```lua
-- Build string from bytes
local function fromBytes(bytes)
  local chars = {}
  for _, b in ipairs(bytes) do
    chars[#chars + 1] = string.char(b)
  end
  return table.concat(chars)
end

print(fromBytes({72, 101, 108, 108, 111}))  -- "Hello"
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)
