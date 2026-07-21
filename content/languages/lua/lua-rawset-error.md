---
title: "[Solution] Lua Rawset Error"
description: "Fix Lua rawset errors when bypassing metamethods."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Rawset errors occur when rawset is called incorrectly.

## Common Causes

- Non-table first argument
- Setting nil key
- Using rawset on read-only table
- rawset with wrong types

## How to Fix

### 1. Validate arguments

```lua
local function safeRawSet(t, key, value)
  if type(t) ~= "table" then return false end
  if key == nil then return false end
  rawset(t, key, value)
  return true
end
```

### 2. Use rawset in __newindex

```lua
local mt = {
  __newindex = function(t, k, v)
    if k == "protected" then
      error("Cannot modify protected field")
    end
    rawset(t, k, v)
  end
}
```

## Examples

```lua
local protected = {}
setmetatable(protected, {
  __newindex = function(t, k, v)
    if type(v) ~= "string" then
      error("Values must be strings")
    end
    rawset(t, k, v)
  end
})

protected.name = "valid"  -- OK
protected.count = 123    -- Error
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Table newindex error](/languages/lua/lua-table-newindex-error)
