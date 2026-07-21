---
title: "[Solution] Lua Table New Index Error"
description: "Fix Lua table __newindex metamethod errors when table fields are assigned."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

__newindex errors occur when assigning to table fields and the metamethod is misconfigured.

## Common Causes

- __newindex metamethod returning unexpected value
- Infinite recursion in __newindex
- __newindex on read-only table
- Missing rawset in __newindex

## How to Fix

### 1. Use rawset to avoid recursion

```lua
local mt = {
  __newindex = function(t, k, v)
    rawset(t, k, v)
  end
}
```

### 2. Implement read-only table

```lua
local function readOnly(t)
  return setmetatable({}, {
    __index = t,
    __newindex = function()
      error("attempt to update a read-only table", 2)
    end
  })
end
```

## Examples

```lua
local protected = {}
local mt = {
  __newindex = function(t, k, v)
    if type(v) ~= "string" then
      error("Values must be strings")
    end
    rawset(t, k, v)
  end
}

setmetatable(protected, mt)
protected.name = "valid"
protected.count = 123  -- Error: Values must be strings
```

## Related Errors

- [Table index error](/languages/lua/lua-table-index-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Metatable error](/languages/lua/lua-metamethod-error)
