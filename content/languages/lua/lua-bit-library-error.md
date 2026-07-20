---
title: "[Solution] Lua Bitwise Library Error Fix"
description: "Fix Lua bitwise operation errors. Learn how to use the bit library in Lua 5.1/5.2 and the native bitwise operators in Lua 5.3+."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1125
---

## What This Error Means

A bitwise library error occurs when using bit operations on unsupported types or with wrong arguments. Lua 5.3 introduced native bitwise operators (&, |, ~, >>, <<), while earlier versions require the bit32 or bit module.

## Common Causes

- Using bit32 functions on negative numbers (Lua 5.2 limitation)
- Using Lua 5.3 bitwise operators in Lua 5.1/5.2
- Passing non-integer arguments to bit functions
- Not checking if bit library is available
- Confusing bit32 with bit (LuaJIT)

## How to Fix

```lua
-- WRONG: Using Lua 5.3 operators in Lua 5.1
local result = 0xFF & 0x0F  -- Error in Lua 5.1/5.2

-- CORRECT: Use bit32 or bit library
-- Lua 5.2:
local result = bit32.band(0xFF, 0x0F)  -- 0x0F
-- LuaJIT:
local result = bit.band(0xFF, 0x0F)    -- 0x0F
```

```lua
-- WRONG: Passing negative numbers to bit32
local result = bit32.band(-1, 0xFF)  -- Error in Lua 5.2

-- CORRECT: Use unsigned values
local result = bit32.band(0xFFFFFFFF, 0xFF)  -- Use full mask
```

```lua
-- WRONG: Passing non-integer arguments
local result = bit32.bor(1.5, 2.7)  -- Error: number has no integer representation

-- CORRECT: Convert to integer first
local result = bit32.bor(math.floor(1.5), math.floor(2.7))  -- 3
```

```lua
-- Version-agnostic bit operations
local band, bor, bxor, lshift, rshift

if _VERSION == "Lua 5.3" or _VERSION == "Lua 5.4" then
    band = function(a, b) return a & b end
    bor  = function(a, b) return a | b end
    bxor = function(a, b) return a ~ b end
    lshift = function(a, b) return a << b end
    rshift = function(a, b) return a >> b end
elseif bit32 then
    band = bit32.band
    bor  = bit32.bor
    bxor = bit32.bxor
    lshift = bit32.lshift
    rshift = bit32.rshift
elseif bit then
    band = bit.band
    bor  = bit.bor
    bxor = bit.bxor
    lshift = bit.lshift
    rshift = bit.rshift
end

print(band(0xFF, 0x0F))  -- 15 (0x0F)
```

```lua
-- Bit flags example
local READ = 1  -- 001
local WRITE = 2 -- 010
local EXEC = 4  -- 100

local function has_permission(perms, flag)
    return perms & flag == flag
end

local user_perms = READ | WRITE  -- 011
print(has_permission(user_perms, READ))   -- true
print(has_permission(user_perms, EXEC))   -- false
```

## Examples

```lua
-- Color encoding with bits
local function rgba(r, g, b, a)
    local rshift = bit32 and bit32.rshift or (function(x, n) return x >> n end)
    local band = bit32 and bit32.band or (function(x, n) return x & n end)
    local lshift = bit32 and bit32.lshift or (function(x, n) return x << n end)
    return lshift(r, 24) | lshift(g, 16) | lshift(b, 8) | a
end

local color = rgba(255, 128, 64, 255)
print(string.format("%08X", color))  -- FF8040FF
```

## Related Errors

- [Lua runtime error](lua-runtime-error) - runtime issue
- [Lua type error](lua-type-error) - type issue
- [Lua arithmetic error](arithmetic-nil) - arithmetic issue
