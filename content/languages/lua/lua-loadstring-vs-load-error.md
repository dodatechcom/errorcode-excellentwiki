---
title: "[Solution] Lua loadstring vs load Function Error Fix"
description: "Fix Lua loadstring and load function errors. Learn the differences between loadstring and load in Lua versions."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1112
---

## What This Error Means

A loadstring/load error occurs when loading Lua code from a string. In Lua 5.1, loadstring was the primary function; in Lua 5.2+, loadstring was deprecated in favor of load with a string argument.

## Common Causes

- Using loadstring in Lua 5.2+ (deprecated, use load instead)
- Calling load with wrong arguments
- Syntax errors in the loaded code string
- Security concerns with loading untrusted code
- Loading code in a restricted environment

## How to Fix

```lua
-- WRONG: Using loadstring in Lua 5.2+
local chunk = loadstring("print('hello')")  -- Works but deprecated

-- CORRECT: Use load in Lua 5.2+
local chunk = load("print('hello')")
if chunk then
    chunk()
end
```

```lua
-- WRONG: Calling load on invalid code
local chunk = load("invalid lua code @@")
if chunk then  -- This check is wrong for error handling
    chunk()
end

-- CORRECT: Check for errors properly
local chunk, err = load("invalid lua code @@")
if not chunk then
    print("Load error:", err)
end
```

```lua
-- WRONG: Loading code that accesses restricted globals
local env = {}
local chunk = load("os.execute('rm -rf /')", nil, "t", env)
-- Still tries to access os which may not be in env

-- CORRECT: Use a sandbox environment
local sandbox = {}
local code = "print('safe code')"
local fn, err = load(code, "=sandbox", "t", sandbox)
if fn then
    fn()
end
```

```lua
-- Safe code loading pattern
local function safe_load(code, env)
    env = env or {}
    local fn, err = load(code, "=custom", "t", env)
    if not fn then
        return nil, err
    end
    return fn
end

local fn, err = safe_load("return 2 + 2")
if fn then
    local result = fn()
    print(result)  -- 4
end
```

## Examples

```lua
local function compile_template(template)
    local code = "return [[" .. template .. "]]"
    local fn, err = load(code)
    if not fn then
        return nil, "Template error: " .. tostring(err)
    end
    return fn
end

local fn = compile_template("Hello, {{name}}")
print(fn and fn() or "Error")
```

## Related Errors

- [Lua runtime error](lua-runtime-error) - runtime issue
- [Lua syntax error](lua-syntax-error) - syntax issue
- [Lua module error](lua-module-error) - module issue
