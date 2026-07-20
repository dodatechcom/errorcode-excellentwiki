---
title: "[Solution] LuaJIT FFI Library Error Fix"
description: "Fix LuaJIT FFI errors when using the Foreign Function Interface to call C functions."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1123
---

## What This Error Means

A LuaJIT FFI error occurs when using ffi.load, ffi.cdef, or ffi.C to call C functions. Common issues include missing libraries, incorrect function signatures, or type mismatches.

## Common Causes

- Library not found by ffi.load
- Incorrect C function declaration in cdef
- Argument type mismatch between Lua and C
- Using ffi.C without loading the library
- Memory management errors with allocated structs

## How to Fix

```lua
-- WRONG: Library not found
local ffi = require("ffi")
ffi.load("nonexistent_library")  -- Error: no such library

-- CORRECT: Check library availability
local ffi = require("ffi")
local ok, lib = pcall(ffi.load, "c")  -- libc
if ok then
    print("Library loaded")
end
```

```lua
-- WRONG: Incorrect C declaration
ffi.cdef[[
    int printf(const char *fmt, ...);  // Correct
    void *malloc(size_t size);         // Correct
    // Wrong:
    void nonexistent_func(void);       // Only detected at call time
]]

-- CORRECT: Only declare functions you actually use
ffi.cdef[[
    int printf(const char *fmt, ...);
]]
ffi.C.printf("Hello %s\n", "world")
```

```lua
-- WRONG: Type mismatch in arguments
ffi.cdef[[
    double sqrt(double x);
]]
local result = ffi.C.sqrt("not_a_number")  -- Argument type mismatch

-- CORRECT: Pass correct types
local result = ffi.C.sqrt(2.0)
print(result)  -- 1.414...
```

```lua
-- WRONG: Memory management with allocated structs
ffi.cdef[[
    typedef struct { int x, y; } Point;
]]
-- Creating structs
local p = ffi.new("Point", 3, 4)
print(p.x, p.y)  -- 3, 4

-- WRONG: Out-of-bounds access
p.z = 5  -- Field doesn't exist
```

```lua
-- Proper FFI metatype usage
ffi.cdef[[
    typedef struct { double x, y; } Point;
]]

local Point = ffi.metatype("Point", {
    __add = function(a, b)
        return ffi.new("Point", a.x + b.x, a.y + b.y)
    end,
    __tostring = function(p)
        return "(" .. p.x .. ", " .. p.y .. ")"
    end,
})

local p1 = Point(1, 2)
local p2 = Point(3, 4)
print(p1 + p2)  -- (4, 6)
```

## Examples

```lua
local ffi = require("ffi")

ffi.cdef[[
    int getpid(void);
    int usleep(unsigned int usec);
]]

print("PID:", ffi.C.getpid())
ffi.C.usleep(100000)  -- Sleep 100ms
```

## Related Errors

- [Lua FFI error](lua-ffi-error) - FFI issue
- [Lua C API error](lua-capi-error) - C API issue
- [Lua type error](lua-type-error) - type issue
