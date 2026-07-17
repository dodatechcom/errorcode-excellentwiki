---
title: "[Solution] Lua Metatable Error Fix"
description: "Fix Lua metatable errors. Learn why metatable operations fail and how to use metatables properly."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["metatable", "metamethod", "table", "lua"]
weight: 5
---

## What This Error Means

A Lua metatable error occurs when metatable operations like __index, __newindex, or __add fail. Metatables allow overriding default table behavior but require correct implementation.

## Common Causes

- Missing metamethod
- Wrong metamethod signature
- Infinite __index recursion
- Circular metatable references

## How to Fix

```lua
-- WRONG: Infinite __index recursion
local mt = {}
mt.__index = mt  -- Recursive lookup

-- CORRECT: Use function or separate table
local mt = {}
mt.__index = function(t, k)
    return rawget(t, k) or default_value
end
```

```lua
-- WRONG: Wrong __add signature
local mt = {}
mt.__add = function(a, b)
    return a + b  -- Recursive
end

-- CORRECT: Implement properly
local mt = {}
mt.__add = function(a, b)
    return setmetatable({value = a.value + b.value}, mt)
end
```

## Examples

```lua
-- Example 1: Basic metatable
local myTable = {}
local mt = {
    __index = function(t, k)
        return "Default: " .. tostring(k)
    end
}
setmetatable(myTable, mt)

print(myTable.anyKey)  -- "Default: anyKey"

-- Example 2: Class-like metatable
local Dog = {}
Dog.__index = Dog

function Dog.new(name)
    local self = setmetatable({}, Dog)
    self.name = name
    return self
end

function Dog:bark()
    print(self.name .. " barks!")
end

-- Example 3: Arithmetic metamethod
local Vec = {}
Vec.__add = function(a, b)
    return Vec.new(a.x + b.x, a.y + b.y)
end
```

## Related Errors

- [Lua nil error](lua-nil-error) - nil access
- [Lua type error](lua-type-error) - type mismatch
- [Lua runtime error](lua-runtime-error) - runtime issue
