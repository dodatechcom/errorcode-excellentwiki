---
title: "[Solution] Lua Metatable Bad Self Argument Error Fix"
description: "Fix Lua 'bad self argument to metamethod' errors. Learn why metamethod calls fail and how to set up metatables correctly."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

The `bad self argument to metamethod` error in Lua occurs when a metamethod receives an argument that is not the expected table. This typically happens when you call an operator on a non-table value that has a metatable, or when a metamethod is invoked with the wrong `self` parameter.

## Why It Happens

- Calling `__index` or `__newindex` on a non-table value with a metatable
- Invoking `__add`, `__sub`, or other arithmetic metamethods on objects where `self` is not a table
- Incorrectly using the `:` method call syntax on a value that is not a table
- Metatable `__index` function returning a non-table value that is then indexed
- Improperly setting up the metatable chain where an intermediate value is not a table

## How to Fix It

### Validate self type inside metamethods

```lua
-- WRONG: Not checking self type
local mt = {
    __index = function(self, key)
        return self.data[key]  -- crashes if self is not a table
    end
}

-- CORRECT: Validate self in metamethods
local mt = {
    __index = function(self, key)
        if type(self) ~= "table" then
            error("bad self argument to __index, expected table, got " .. type(self))
        end
        return rawget(self, key) or self.data and self.data[key]
    end
}
```

### Ensure metatable is set on a table

```lua
-- WRONG: Setting metatable on a non-table
local obj = "hello"
setmetatable(obj, { __len = function(self) return 5 end })  -- error

-- CORRECT: Set metatable only on tables
local obj = { value = "hello" }
setmetatable(obj, {
    __len = function(self)
        return #self.value
    end
})
print(#obj)  -- 5
```

### Use rawget and rawset to avoid recursion

```lua
-- WRONG: __index triggers itself through recursive lookup
local mt = {
    __index = function(self, key)
        return self.defaults[key]  -- self.defaults triggers __index again
    end
}

-- CORRECT: Use rawget to bypass metamethods
local mt = {
    __index = function(self, key)
        local defaults = rawget(self, "defaults")
        return defaults and defaults[key]
    end
}
```

### Handle arithmetic metamethods properly

```lua
-- WRONG: __add returning wrong type
local vec_mt = {
    __add = function(a, b)
        return a.x + b.x  -- returns a number, not a table
    end
}

-- CORRECT: Return proper type from metamethod
local vec_mt = {
    __add = function(a, b)
        return setmetatable({ x = a.x + b.x, y = a.y + b.y }, vec_mt)
    end
}
```

### Check for nil metatable chains

```lua
-- WRONG: Metatable chain broken
local a = setmetatable({}, { __index = nil })
local b = getmetatable(a).__index  -- __index is nil

-- CORRECT: Verify metatable structure before use
local mt = getmetatable(a)
if mt and mt.__index then
    -- safe to use
end
```

## Common Mistakes

- Using `:` syntax on a non-table value, which passes the wrong self argument
- Setting `__index` to a function that does not return the expected type
- Creating circular metatable references that cause infinite recursion
- Not using `rawget` inside `__index` metamethods, leading to infinite loops
- Forgetting that `setmetatable` returns the modified table, not a new one

## Related Pages

- [Lua Nil Index Error](lua-nil-index-error) - indexing nil value
- [Lua Argument Type Error](lua-argument-type-error) - wrong argument type
- [Lua Table Length](lua-table-length) - table length undefined behavior
- [Lua Userdata Error](lua-userdata-error) - userdata operation failure
