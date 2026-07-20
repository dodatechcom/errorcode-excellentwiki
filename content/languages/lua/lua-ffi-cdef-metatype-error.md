---
title: "[Solution] LuaJIT ffi.cdef / ffi.metatype Declaration Error Fix"
description: "Fix LuaJIT ffi.cdef and ffi.metatype declaration errors when defining C types and their Lua methods."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1124
---

## What This Error Means

An ffi.cdef or ffi.metatype error occurs when declaring C types or attaching metamethods to C types in LuaJIT's FFI. These errors usually result from syntax errors in cdef or incorrect metatype definitions.

## Common Causes

- C syntax errors inside ffi.cdef string
- Redeclaring types that conflict with each other
- Using ffi.metatype on undeclared types
- Missing required metamethods for FFI types
- Incorrect argument types in metatype methods

## How to Fix

```lua
-- WRONG: C syntax error in cdef
ffi.cdef[[
    typedef struct {  // Missing closing brace
        int x, y;
]]
-- CORRECT: Proper C syntax
ffi.cdef[[
    typedef struct {
        int x, y;
    } Point;
]]
```

```lua
-- WRONG: Using metatype on undeclared type
local vec = ffi.metatype("Vector", {})  -- 'Vector' not declared

-- CORRECT: Declare type first
ffi.cdef[[
    typedef struct { double x, y, z; } Vector;
]]
local Vector = ffi.metatype("Vector", {
    __add = function(a, b)
        return Vector(a.x + b.x, a.y + b.y, a.z + b.z)
    end,
})
```

```lua
-- WRONG: Redeclaring an existing type
ffi.cdef[[typedef struct { int a; } Foo;]]
ffi.cdef[[typedef struct { int a; } Foo;]]  -- Redeclaration error

-- CORRECT: Declare once
ffi.cdef[[typedef struct { int a; } Foo;]]
```

```lua
-- ffi.metatype with custom methods
ffi.cdef[[
    typedef struct {
        int x, y;
    } Point;
]]

local Point = ffi.metatype("Point", {
    __index = {
        distance = function(p)
            return math.sqrt(p.x * p.x + p.y * p.y)
        end,
        scale = function(p, factor)
            return Point(p.x * factor, p.y * factor)
        end,
    },
    __tostring = function(p)
        return "(" .. p.x .. ", " .. p.y .. ")"
    end,
})

local p = Point(3, 4)
print(p:distance())  -- 5
print(p:scale(2))    -- (6, 8)
```

```lua
-- Array types with ffi.metatype
ffi.cdef[[
    typedef struct { int id; char name[64]; } User;
]]

local User = ffi.metatype("User", {
    __tostring = function(u)
        return string.format("User[%d]: %s", u.id, ffi.string(u.name))
    end,
})

local u = User(1, "Alice")
print(u)  -- User[1]: Alice
```

## Examples

```lua
local ffi = require("ffi")

ffi.cdef[[
    typedef struct {
        double real;
        double imag;
    } Complex;
]]

local Complex = ffi.metatype("Complex", {
    __add = function(a, b)
        return Complex(a.real + b.real, a.imag + b.imag)
    end,
    __mul = function(a, b)
        return Complex(a.real * b.real - a.imag * b.imag,
                       a.real * b.imag + a.imag * b.real)
    end,
    __tostring = function(c)
        return string.format("%g + %gi", c.real, c.imag)
    end,
})

local a = Complex(1, 2)
local b = Complex(3, 4)
print(a + b)  -- 4 + 6i
print(a * b)  -- -5 + 10i
```

## Related Errors

- [Lua FFI error](lua-ffi-error) - FFI issue
- [Lua C API error](lua-capi-error) - C API issue
- [Lua type error](lua-type-error) - type issue
