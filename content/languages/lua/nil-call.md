---
title: "[Solution] Lua Attempt to Call a Nil Value — Runtime Error Fix"
description: "Fix Lua 'attempt to call a nil value' error. Learn why calling nil as a function crashes and how to ensure functions are defined before use."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nil", "call", "function", "nil-value", "runtime"]
weight: 5
---

# Attempt to Call a Nil Value — Runtime Error Fix

An `attempt to call a nil value` error occurs when you try to invoke a variable as a function, but the variable is `nil`. In Lua, only functions (and objects with `__call` metamethods) can be called.

## Description

In Lua, functions are first-class values. If you try to call a variable with `()` and that variable is `nil` instead of a function, Lua raises a runtime error. This commonly happens when a module fails to load, a function name is misspelled, or a function isn't defined before it's called.

Common scenarios:

- **Misspelled function name** — calling a function that doesn't exist.
- **Module load failure** — `require` returns `nil` instead of a module table.
- **Function called before definition** — calling a local function defined later in the file.
- **Table method missing** — calling a method on a table that doesn't define it.

## Common Causes

```lua
-- Cause 1: Misspelled function name
local function greet()
    print("Hello!")
end
greett() -- attempt to call a nil value (global 'greett')

-- Cause 2: Module not loaded
local utils = require("nonexistent_utils")
utils.doSomething() -- attempt to call a nil value

-- Cause 3: Local function called before definition
local result = myFunc() -- crash: myFunc is nil here
local function myFunc()
    return 42
end

-- Cause 4: Missing method on table
local obj = { name = "Alice" }
obj.greet() -- attempt to call a nil value (greet is nil)
```

## How to Fix

### Fix 1: Verify function exists before calling

```lua
-- Wrong
myFunction()

-- Correct
if myFunction then
    myFunction()
else
    print("myFunction is not defined")
end
```

### Fix 2: Define local functions before use

```lua
-- Wrong
local result = myFunc()  -- myFunc is nil here

local function myFunc()
    return 42
end

-- Correct
local function myFunc()
    return 42
end

local result = myFunc()  -- works fine
```

### Fix 3: Check module loads properly

```lua
-- Wrong
local utils = require("my_utils")
utils.process()

-- Correct
local ok, utils = pcall(require, "my_utils")
if ok and utils then
    utils.process()
else
    error("Failed to load my_utils: " .. tostring(utils))
end
```

### Fix 4: Define methods in table constructor

```lua
-- Wrong
local obj = {}
obj.greet() -- crash

-- Correct
local obj = {
    greet = function(self)
        print("Hello, " .. self.name)
    end,
    name = "Alice"
}
obj:greet() -- works
```

## Examples

```lua
-- This triggers: attempt to call a nil value (global 'undefinedFunc')
undefinedFunc()
```

## Related Errors

- [nil-index] — attempt to index a nil value (accessing fields on nil).
- [attempt to perform arithmetic on a nil value] — using nil in math operations.
- [attempt to concatenate a nil value] — trying to join nil with a string.
