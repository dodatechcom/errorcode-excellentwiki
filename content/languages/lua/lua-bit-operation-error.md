---
title: "[Solution] Lua Bit Operation Error"
description: "Fix Lua bitwise operation errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Bit operation errors occur when using bitwise operations incorrectly.

## Common Causes

- Wrong operator
- Integer expected
- Overflow
- Missing bit library

## How to Fix

### 1. Use bit library

```lua
local bit = require("bit")
local result = bit.band(0xFF, 0x0F)
```

### 2. Lua 5.3 native bitops

```lua
local result = 0xFF & 0x0F  -- Lua 5.3
```

## Examples

```lua
-- Bit operations
local bit = require("bit")

-- Common operations
local a = 0xFF
local b = 0x0F

print("AND:", bit.band(a, b))    -- 15
print("OR:", bit.bor(a, b))      -- 255
print("XOR:", bit.bxor(a, b))   -- 240
print("NOT:", bit.bnot(a))       -- -256
print("LSH:", bit.lshift(a, 4))  -- 4080
print("RSH:", bit.rshift(a, 4))  -- 15
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)
