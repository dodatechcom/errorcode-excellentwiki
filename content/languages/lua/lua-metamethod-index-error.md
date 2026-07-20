---
title: "[Solution] Lua __index / __newindex Metamethod Error Fix"
description: "Fix Lua __index and __newindex metamethod errors in metatables."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1102
---

## What This Error Means

An __index or __newindex metamethod error occurs when these methods are incorrectly defined or cause infinite recursion in a metatable chain.

## Common Causes

- Infinite recursion in __index (calling rawget on self)
- __newindex preventing writes incorrectly
- __index set to a table but table doesn't contain the key
- __newindex interfering with rawset
- Forgetting to use rawget/rawset inside metamethods

## How to Fix

```lua
-- WRONG: Infinite recursion in __index
local mt = {}
mt.__index = function(t, key)
    return t[key]  -- Calls __index again -> infinite recursion
end

-- CORRECT: Use rawget to bypass __index
mt.__index = function(t, key)
    return rawget(t, key)
end
```

```lua
-- WRONG: __newindex that blocks all writes
local t = setmetatable({}, {
    __newindex = function(t, key, value)
        -- No rawset called -> write silently lost
    end
})
t.name = "Alice"
print(t.name)  -- nil

-- CORRECT: Use rawset inside __newindex
local t = setmetatable({}, {
    __newindex = function(t, key, value)
        if key == "protected" then
            error("Cannot set protected key")
        else
            rawset(t, key, value)
        end
    end
})
t.name = "Alice"
print(t.name)  -- Alice
```

```lua
-- WRONG: __index on table with missing key
local defaults = { x = 0, y = 0 }
local t = setmetatable({}, { __index = defaults })
print(t.z)  -- nil (defaults doesn't have z either)

-- CORRECT: Chain multiple levels
defaults.__index = { z = 10 }
```

```lua
-- Using __index for default values
local Defaults = { name = "Unknown", age = 0 }
local user = setmetatable({ name = "Alice" }, { __index = Defaults })
print(user.name)  -- Alice
print(user.age)   -- 0 (from Defaults)
```

## Examples

```lua
local Logger = {}
Logger.__index = Logger

function Logger.new(prefix)
    return setmetatable({ prefix = prefix }, Logger)
end

function Logger.log(self, msg)
    print("[" .. self.prefix .. "] " .. msg)
end

function Logger.__call(self, msg)
    self:log(msg)
end

local log = Logger.new("APP")
log("Hello")  -- [APP] Hello
```

## Related Errors

- [Lua metatable error](lua-metatable-error) - metatable issue
- [Lua nil index error](lua-nil-index-error) - nil index
- [Lua type error](lua-type-error) - type issue
