---
title: "[Solution] Lua String Lower Error"
description: "Fix Lua string.lower errors when converting to lowercase."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

String lower errors occur when string.lower is called on non-strings.

## Common Causes

- Non-string input
- Missing argument
- Table or number passed
- Nil value passed

## How to Fix

### 1. Validate input

```lua
local function safeLower(s)
  if type(s) ~= "string" then return "" end
  return string.lower(s)
end
```

### 2. Use string.lower

```lua
print(string.lower("HELLO"))  -- "hello"
```

## Examples

```lua
-- Case insensitive comparison
local function equalsIgnoreCase(a, b)
  return string.lower(a) == string.lower(b)
end

print(equalsIgnoreCase("Hello", "hello"))  -- true
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)
