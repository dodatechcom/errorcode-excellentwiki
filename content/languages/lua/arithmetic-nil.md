---
title: "attempt to perform arithmetic on nil"
description: "An attempt to perform arithmetic on nil occurs when using nil in mathematical operations."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["arithmetic", "nil", "math", "lua"]
weight: 5
---

## What This Error Means

An `attempt to perform arithmetic on a nil value` error occurs when you try to use nil in arithmetic operations (+, -, *, /, %, ^). Lua requires both operands to be numbers for arithmetic operations.

## Common Causes

- Variable is nil instead of number
- Function returning nil
- Missing default value
- Wrong table access

## How to Fix

```lua
-- WRONG: Arithmetic on nil
local x = nil
local result = x + 1  -- attempt to perform arithmetic on nil

-- CORRECT: Provide default or check nil
local x = nil
local result = (x or 0) + 1  -- 1
```

```lua
-- WRONG: Table value is nil
local config = {}
local timeout = config.timeout * 1000  -- attempt to perform arithmetic

-- CORRECT: Check before arithmetic
local config = {}
local timeout = (config.timeout or 30) * 1000
```

## Examples

```lua
-- Example 1: Nil in addition
local a = nil
print(a + 1)  -- attempt to perform arithmetic on nil

-- Example 2: Missing function return
local function get_value()
    -- forgot to return
end
local result = get_value() * 2  -- attempt to perform arithmetic

-- Example 3: Wrong table access
local settings = {}
local port = settings.port + 1  -- attempt to perform arithmetic
```

## Related Errors

- [attempt to index nil](/languages/lua/nil-index)
- [attempt to concatenate nil](/languages/lua/concatenate-nil)
