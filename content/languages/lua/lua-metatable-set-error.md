---
title: "[Solution] Lua Metatable setmetatable Error Fix"
description: "Fix Lua setmetatable errors when assigning or modifying metatables."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1101
---

## What This Error Means

A metatable error occurs when using setmetatable or getmetatable on values that don't support metatables, or when trying to set invalid metatable operations.

## Common Causes

- Trying to set a metatable on a non-table value (numbers, strings, booleans)
- Setting a nil metatable by mistake
- Circular metatable references
- Using getmetatable on a table without a metatable
- Modifying a locked/protected metatable

## How to Fix

```lua
-- WRONG: Setting metatable on a number
local n = 42
setmetatable(n, {})  -- error: cannot set metatable on number

-- CORRECT: Only tables can have metatables
local t = {}
setmetatable(t, {
    __tostring = function() return "my table" end
})
```

```lua
-- WRONG: Getting metatable from a primitive
local s = "hello"
local mt = getmetatable(s)  -- nil, or the string metatable

-- CORRECT: Check if metatable exists
local t = {}
local mt = getmetatable(t)
if mt then
    print("Has metatable")
else
    print("No metatable")
end
```

```lua
-- WRONG: Circular metatable
local a = {}
local b = {}
setmetatable(a, { __index = b })
setmetatable(b, { __index = a })  -- circular!

-- CORRECT: Avoid circular references
setmetatable(b, { __index = {} })
```

```lua
-- WRONG: Modifying a locked metatable
local t = {}
local mt = { __metatable = "locked" }
setmetatable(t, mt)
local r = getmetatable(t)  -- returns "locked", not mt
setmetatable(t, {})  -- error: cannot change protected metatable
```

## Examples

```lua
local Point = {}
Point.__index = Point

function Point.new(x, y)
    return setmetatable({ x = x, y = y }, Point)
end

function Point:__tostring()
    return "(" .. self.x .. ", " .. self.y .. ")"
end

local p = Point.new(3, 4)
print(p)  -- (3, 4)
```

## Related Errors

- [Lua metatable error](lua-metatable-error) - metatable issue
- [Lua nil index error](lua-nil-index-error) - nil index
- [Lua type error](lua-type-error) - type issue
