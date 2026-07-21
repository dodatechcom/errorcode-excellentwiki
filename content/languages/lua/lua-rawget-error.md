---
title: "[Solution] Lua Rawget Error"
description: "Fix Lua rawget errors when bypassing metamethods."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Rawget errors occur when rawget is called incorrectly.

## Common Causes

- Non-table first argument
- Missing key argument
- Using rawget on nil
- rawget with wrong type

## How to Fix

### 1. Validate table

```lua
local function safeRawGet(t, key)
  if type(t) ~= "table" then return nil end
  return rawget(t, key)
end
```

### 2. Use rawget properly

```lua
local t = {name = "test"}
setmetatable(t, {__index = function() return "default" end})

print(rawget(t, "name"))    -- "test"
print(t.name)                -- "test"
print(t.missing)             -- "default"
```

## Examples

```lua
-- Check if key exists without triggering __index
local function hasKey(t, key)
  return rawget(t, key) ~= nil
end

local data = {x = 1}
print(hasKey(data, "x"))  -- true
print(hasKey(data, "y"))  -- false
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Table index error](/languages/lua/lua-table-index-error)
