---
title: "[Solution] Lua String Len Error"
description: "Fix Lua string.len errors when getting string length."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

String len errors occur when string.len is called on non-strings.

## Common Causes

- Non-string input
- Missing argument
- Table or number passed
- Nil value passed

## How to Fix

### 1. Validate input

```lua
local function safeLen(s)
  if type(s) ~= "string" then return 0 end
  return #s
end
```

### 2. Use operator # directly

```lua
local s = "Hello"
print(#s)  -- 5
```

## Examples

```lua
-- Get length safely
local function length(s)
  if s == nil then return 0 end
  if type(s) ~= "string" then return 0 end
  return #s
end

print(length("Hello"))  -- 5
print(length(nil))      -- 0
print(length(42))       -- 0
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)
