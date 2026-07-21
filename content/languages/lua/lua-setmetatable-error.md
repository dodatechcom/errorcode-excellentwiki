---
title: "[Solution] Lua Setmetatable Error"
description: "Fix Lua setmetatable errors when setting metatables."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Setmetatable errors occur when setmetatable is called incorrectly.

## Common Causes

- Non-table first argument
- Non-table or nil second argument
- Setting metatable on nil
- Circular metatable references

## How to Fix

### 1. Validate arguments

```lua
local function safeSetmetatable(t, mt)
  if type(t) ~= "table" then return nil end
  if mt ~= nil and type(mt) ~= "table" then return nil end
  return setmetatable(t, mt)
end
```

### 2. Use setmetatable correctly

```lua
local MyClass = {}
MyClass.__index = MyClass

function MyClass.new(value)
  return setmetatable({value = value}, MyClass)
end
```

## Examples

```lua
-- Create a class
local Animal = {}
Animal.__index = Animal

function Animal.new(name, sound)
  return setmetatable({name = name, sound = sound}, Animal)
end

function Animal:speak()
  return self.name .. " says " .. self.sound
end

local dog = Animal.new("Dog", "Woof")
print(dog:speak())  -- "Dog says Woof"
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Metamethod error](/languages/lua/lua-metamethod-error)
