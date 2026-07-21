---
title: "[Solution] Lua String Split Error"
description: "Fix Lua string split errors when splitting strings."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

String split errors occur when splitting strings with incorrect patterns.

## Common Causes

- Lua has no built-in split
- Pattern not matching delimiter
- Split function returns nil
- Edge cases with empty strings

## How to Fix

### 1. Use standard split pattern

```lua
function string.split(s, sep)
  local parts = {}
  local pattern = "([^" .. sep .. "]+)"
  for part in s:gmatch(pattern) do
    parts[#parts + 1] = part
  end
  return parts
end
```

### 2. Use gmatch with separator

```lua
function string.split(s, sep)
  local parts = {}
  local pattern = string.format("([^%s]+)", sep)
  for match in s:gmatch(pattern) do
    parts[#parts + 1] = match
  end
  return parts
end
```

## Examples

```lua
local function split(s, sep)
  local parts = {}
  for part in s:gmatch("([^" .. sep .. "]+)") do
    parts[#parts + 1] = part
  end
  return parts
end

local words = split("hello,world,foo", ",")
for _, w in ipairs(words) do
  print(w)
end
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Pattern error](/languages/lua/lua-pattern-error)
- [String gmatch error](/languages/lua/lua-string-gmatch-error)
