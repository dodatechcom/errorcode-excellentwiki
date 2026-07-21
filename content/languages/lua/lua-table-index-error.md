---
title: "[Solution] Lua Table Index Error"
description: "Fix Lua table indexing errors when table fields are accessed or assigned."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Table index errors occur when accessing or assigning non-existent table fields.

## Common Causes

- Accessing nil table field
- Indexing with wrong data type
- Missing table key
- Table field type mismatch

## How to Fix

### 1. Check if key exists

```lua
if t[key] ~= nil then
  return t[key]
end
```

### 2. Use default values

```lua
local function getOrDefault(t, key, default)
  return t[key] or default
end
```

## Examples

```lua
local user = { name = "Alice", age = 30 }

-- Safe access
local function safeGet(t, key)
  local val = t[key]
  if val == nil then
    error("Key '" .. tostring(key) .. "' not found")
  end
  return val
end

print(safeGet(user, "name"))
```

## Related Errors

- [Nil value error](/languages/lua/lua-nil-value)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Type error](/languages/lua/lua-type-error)
