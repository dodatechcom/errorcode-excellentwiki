---
title: "[Solution] Lua Userdata Error Fix"
description: "Fix Lua userdata errors. Learn why userdata operations fail and how to handle userdata properly."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Lua userdata error occurs when operations on userdata (C data exposed to Lua) fail. Userdata can only be accessed through metatables and specific API functions.

## Common Causes

- Accessing userdata fields directly
- Wrong userdata type
- Missing metatable
- GC collecting active userdata

## How to Fix

```lua
-- WRONG: Accessing userdata directly
local ud = create_userdata()
print(ud.field)  -- Cannot access userdata fields

-- CORRECT: Use metamethods
local mt = {
    __index = function(t, k)
        return userdata_get(t, k)
    end
}
setmetatable(ud, mt)
```

```lua
-- WRONG: Wrong type check
local ud = create_userdata()
print(type(ud))  -- "userdata", not specific type

-- CORRECT: Use metatable name
local mt_name = getmetatable(ud)
if mt_name == expected_mt then
    -- Correct type
end
```

## Examples

```lua
-- Example 1: Basic userdata
local ffi = require("ffi")
ffi.cdef[[
    typedef struct { int x, y; } Point;
]]

local p = ffi.new("Point", 10, 20)
print(p.x, p.y)

-- Example 2: Userdata with metatable
local mt = {}
mt.__index = mt
function mt:tostring()
    return string.format("Point(%d, %d)", self.x, self.y)
end

-- Example 3: Finalizer
local mt = {}
mt.__gc = function(ud)
    userdata_cleanup(ud)
end
```

## Related Errors

- [Lua C API error](lua-capi-error) - C API issue
- [Lua FFI error](lua-ffi-error) - FFI error
- [Lua metatable error](lua-metatable-error) - metatable issue
