---
title: "[Solution] Lua String Sub Error"
description: "Fix Lua string.sub errors when extracting substrings."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

String sub errors occur when string.sub is called with invalid arguments.

## Common Causes

- Start position out of bounds
- End position less than start
- Non-string input
- Position is nil

## How to Fix

### 1. Validate positions

```lua
local function safeSub(s, i, j)
  if type(s) ~= "string" then return nil end
  i = math.max(1, i or 1)
  j = math.min(#s, j or #s)
  if i > j then return "" end
  return string.sub(s, i, j)
end
```

### 2. Use negative indexing

```lua
local s = "Hello, World!"
print(string.sub(s, -6, -2))  -- "World"
```

## Examples

```lua
local function extract(s, start, length)
  return string.sub(s, start, start + length - 1)
end

print(extract("Hello World", 7, 5))  -- "World"
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)
