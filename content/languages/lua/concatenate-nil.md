---
title: "attempt to concatenate nil"
description: "An attempt to concatenate nil occurs when trying to use the concatenation operator on a nil value."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["concatenate", "nil", "string", "lua"]
weight: 5
---

## What This Error Means

An `attempt to concatenate a nil value` error occurs when you try to use the `..` operator to concatenate a string with a nil value. Lua requires both sides of the concatenation operator to be strings or numbers.

## Common Causes

- Variable is nil instead of string
- Function returning nil
- Missing default value
- Wrong table access

## How to Fix

```lua
-- WRONG: Concatenating nil
local name = nil
print("Hello, " .. name)  -- attempt to concatenate nil

-- CORRECT: Provide default or check nil
local name = nil
print("Hello, " .. (name or "World"))
```

```lua
-- WRONG: Table value is nil
local config = {}
print("Host: " .. config.host)  -- attempt to concatenate nil

-- CORRECT: Check before concatenating
local config = {}
print("Host: " .. (config.host or "localhost"))
```

## Examples

```lua
-- Example 1: Nil variable
local x = nil
print("Value: " .. x)  -- attempt to concatenate nil

-- Example 2: Missing table value
local t = {}
print("Name: " .. t.name)  -- attempt to concatenate nil

-- Example 3: Function returns nil
local function get_name()
    -- forgot to return
end
print("Hello, " .. get_name())  -- attempt to concatenate nil
```

## Related Errors

- [attempt to index nil](/languages/lua/nil-index)
- [attempt to perform arithmetic on nil](/languages/lua/arithmetic-nil)
