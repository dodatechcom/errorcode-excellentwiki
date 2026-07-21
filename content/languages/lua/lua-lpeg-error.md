---
title: "[Solution] Lua Lpeg Error"
description: "Fix Lua LPeg pattern matching errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

LPeg errors occur when using LPeg patterns incorrectly.

## Common Causes

- Invalid pattern syntax
- Pattern too complex
- Stack overflow
- Missing lpeg module

## How to Fix

### 1. Use lpeg correctly

```lua
local lpeg = require("lpeg")
local match = lpeg.match
local pattern = lpeg.R("az")^1
```

### 2. Handle errors

```lua
local function safeMatch(pattern, subject)
  local ok, result = pcall(match, pattern, subject)
  if ok then
    return result
  else
    return nil, result
  end
end
```

## Examples

```lua
-- Simple pattern matching
local lpeg = require("lpeg")

local digit = lpeg.R("09")
local number = digit^1 / tonumber
local space = lpeg.S(" \t\n")^0
local expr = number * space * lpeg.P("+") * space * number

local function calc(str)
  local a, b = lpeg.match(expr * lpeg.Cp(), str)
  return a + b
end

print(calc("1+2"))  -- 3
```

## Related Errors

- [Pattern error](/languages/lua/lua-pattern-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Type error](/languages/lua/lua-type-error)
