---
title: "attempt to call nil"
description: "An attempt to call nil occurs when trying to call a value that is not a function."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `attempt to call a nil value` error occurs when you try to call a variable as a function, but the variable is nil. This happens when a function isn't defined, module require fails, or a variable is misspelled.

## Common Causes

- Function not defined
- Module require returns nil
- Typo in function name
- Variable used before assignment

## How to Fix

```lua
-- WRONG: Calling undefined function
greet("Hello")  -- attempt to call nil value

-- CORRECT: Define function first
local function greet(name)
    print("Hello, " .. name)
end
greet("World")
```

```lua
-- WRONG: Not checking require
local mod = require("nonexistent")
mod.doSomething()  -- attempt to call nil

-- CORRECT: Check require result
local ok, mod = pcall(require, "my_module")
if ok and mod then
    mod.doSomething()
end
```

## Examples

```lua
-- Example 1: Undefined function
myFunc()  -- attempt to call nil value

-- Example 2: Module not loaded
local math = require("nonexistent")
math.sqrt(4)  -- attempt to call nil

-- Example 3: Typo
local function calculate()
    return 42
end
calulate()  -- attempt to call nil (typo)
```

## Related Errors

- [attempt to index nil](/languages/lua/nil-index)
- [attempt to concatenate nil](/languages/lua/concatenate-nil)
