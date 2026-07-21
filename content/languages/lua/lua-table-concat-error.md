---
title: "[Solution] Lua Table Concatenation Error"
description: "Fix Lua table concatenation errors when tables cannot be concatenated."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Table concatenation errors occur when attempting to concatenate a table directly.

## Common Causes

- Concatenating table with string using ..
- Missing table concatenation function
- Table contains nil values
- Using .. on non-string values

## How to Fix

### 1. Create table.concat wrapper

```lua
local function concat(t, sep)
  return table.concat(t, sep or "")
end
```

### 2. Use table.concat properly

```lua
local t = {"a", "b", "c"}
print(table.concat(t, ", "))
```

## Examples

```lua
local function join(t, sep)
  local result = {}
  for i, v in ipairs(t) do
    result[i] = tostring(v)
  end
  return table.concat(result, sep)
end

local nums = {1, 2, 3}
print(join(nums, ", "))  -- "1, 2, 3"
```

## Related Errors

- [Type error](/languages/lua/lua-type-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
