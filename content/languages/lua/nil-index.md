---
title: "attempt to index nil"
description: "An attempt to index nil occurs when trying to access a field or index on a nil value."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `attempt to index a nil value` error occurs when you try to access a field or index on a variable that is nil. In Lua, only tables (and userdata with metamethods) can be indexed — nil cannot.

## Common Causes

- Uninitialized table
- Missing return value from function
- Wrong module require (returns nil)
- Typo in variable name

## How to Fix

```lua
-- WRONG: Accessing nil table
local config = {}
print(config.database.host)  -- attempt to index nil value

-- CORRECT: Initialize nested tables
local config = {}
config.database = {}
config.database.host = "localhost"
```

```lua
-- WRONG: Not checking require
local mylib = require("nonexistent_module")
print(mylib.some_function())  -- attempt to index nil

-- CORRECT: Check require result
local ok, mylib = pcall(require, "my_module")
if ok and mylib then
    mylib.doSomething()
else
    print("Failed to load module")
end
```

## Examples

```lua
-- Example 1: Nil variable
local obj = nil
print(obj.field)  -- attempt to index nil value

-- Example 2: Module not found
local mylib = require("nonexistent")
print(mylib.func())  -- attempt to index nil

-- Example 3: Typo
local settings = { debug = true }
print(settingss.debug)  -- attempt to index nil
```

## Related Errors

- [attempt to call nil](/languages/lua/call-not-function)
- [attempt to perform arithmetic on nil](/languages/lua/arithmetic-nil)
