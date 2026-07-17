---
title: "table index is nil"
description: "A table index is nil error occurs when trying to use nil as a table key."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `table index is nil` error occurs when you try to use nil as a key in a table. In Lua, table keys cannot be nil — attempting to assign a value with a nil key results in this error.

## Common Causes

- Using nil variable as key
- Forgetting to set table key
- Wrong variable used as key
- Function returning nil as key

## How to Fix

```lua
-- WRONG: Using nil as key
local key = nil
local t = {}
t[key] = "value"  -- table index is nil

-- CORRECT: Ensure key is not nil
local key = "mykey"
local t = {}
t[key] = "value"
```

```lua
-- WRONG: Dynamic key that might be nil
local t = {}
local name = get_name()  -- might return nil
t[name] = true  -- table index is nil

-- CORRECT: Check key first
local name = get_name()
if name then
    t[name] = true
end
```

## Examples

```lua
-- Example 1: Nil key
local t = {}
t[nil] = "value"  -- table index is nil

-- Example 2: Variable nil
local key = nil
local map = {}
map[key] = 1  -- table index is nil

-- Example 3: Missing function return
local function get_key()
    -- forgot to return
end
local data = {}
data[get_key()] = true  -- table index is nil
```

## Related Errors

- [attempt to index nil](/languages/lua/nil-index)
- [attempt to call nil](/languages/lua/call-not-function)
