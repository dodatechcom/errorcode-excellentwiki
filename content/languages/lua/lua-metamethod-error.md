---
title: "[Solution] Lua Metamethod Error"
description: "Fix Lua metamethod errors when implementing custom type behaviors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Metamethod errors occur when metamethods are incorrectly implemented or called.

## Common Causes

- Missing metamethods
- Incorrect metamethod signatures
- Recursive metamethod calls
- Metamethod returning wrong type

## How to Fix

### 1. Implement complete metamethods

```lua
local mt = {
  __add = function(a, b)
    return {x = a.x + b.x, y = a.y + b.y}
  end,
  __tostring = function(t)
    return string.format("(%d, %d)", t.x, t.y)
  end
}
```

### 2. Use rawget/rawset to avoid recursion

```lua
local mt = {
  __newindex = function(t, k, v)
    rawset(t, k, v)
  end
}
```

## Examples

```lua
local Vector = {}
Vector.__index = Vector

function Vector.new(x, y)
  return setmetatable({x = x, y = y}, Vector)
end

function Vector.__add(a, b)
  return Vector.new(a.x + b.x, a.y + b.y)
end

function Vector:__tostring()
  return string.format("Vector(%d, %d)", self.x, self.y)
end

local v1 = Vector.new(1, 2)
local v2 = Vector.new(3, 4)
print(v1 + v2)  -- "Vector(4, 6)"
```

## Related Errors

- [Table newindex error](/languages/lua/lua-table-newindex-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Index error](/languages/lua/lua-table-index-error)
