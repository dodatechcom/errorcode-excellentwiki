---
title: "[Solution] Lua Getmetatable Error"
description: "Fix Lua getmetatable errors when retrieving metatables."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Getmetatable errors occur when getmetatable is called incorrectly.

## Common Causes

- Non-table argument
- Missing argument
- getmetatable on nil
- Protected metatables

## How to Fix

### 1. Validate argument

```lua
local function safeGetmetatable(t)
  if type(t) ~= "table" then return nil end
  return getmetatable(t)
end
```

### 2. Use getmetatable correctly

```lua
local t = {}
setmetatable(t, {__index = function() return 42 end})

local mt = getmetatable(t)
print(mt.__index(nil))  -- 42
```

## Examples

```lua
-- Check if table has metatable
local function hasMetatable(t)
  return getmetatable(t) ~= nil
end

-- Get metatable safely
local function safeMetatable(t)
  local mt = getmetatable(t)
  if mt == nil then
    return {}
  end
  return mt
end

local data = {1, 2, 3}
setmetatable(data, {__len = function() return 10 end})

print(hasMetatable(data))  -- true
print(#data)               -- 10
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Setmetatable error](/languages/lua/lua-setmetatable-error)
