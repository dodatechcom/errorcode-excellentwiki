---
title: "[Solution] Lua Attempt to Index Nil Value"
description: "Fix Lua 'attempt to index a nil value' error when accessing fields on nil. Check variable initialization and table existence."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["index", "nil", "table", "field", "access", "lua"]
weight: 5
---

## What This Error Means

The error `attempt to index a nil value` occurs when you try to access a field or method on a variable that is `nil`. This is one of the most common Lua errors.

## Common Causes

- Variable not initialized (nil by default)
- Function returning nil
- Table not created before field access
- Module not loaded
- Incorrect variable name

## How to Fix

```lua
-- WRONG: Accessing field on nil
local config = nil
print(config.host)  -- attempt to index nil value

-- CORRECT: Initialize table
local config = {}
config.host = "localhost"
config.port = 8080
```

```lua
-- WRONG: Function returning nil
local function get_config()
    return nil
end
local cfg = get_config()
print(cfg.host)  -- Error

-- CORRECT: Check return value
local function get_config()
    return { host = "localhost" }
end
local cfg = get_config()
if cfg then
    print(cfg.host)
end
```

```lua
-- WRONG: Module not loaded
local json = require("json")
local data = json.decode(input)  -- Error if module not found

-- CORRECT: Check module loaded
local ok, json = pcall(require, "json")
if ok then
    local data = json.decode(input)
else
    print("JSON module not available")
end
```

## Examples

```lua
-- Example 1: Safe access pattern
local function safe_get(t, key, default)
    if type(t) == "table" then
        return t[key] or default
    end
    return default
end

-- Example 2: Nested table access
local config = {
    database = {
        host = "localhost",
        port = 5432,
    }
}
-- WRONG: config.cache.ttl  -- Error if cache is nil
-- CORRECT:
local cache = config.cache or {}
local ttl = cache.ttl or 300

-- Example 3: Chained nil checks
local function get_nested(obj, ...)
    local current = obj
    for _, key in ipairs({...}) do
        if type(current) ~= "table" then return nil end
        current = current[key]
    end
    return current
end
```

## Related Errors

- [lua-nil-error]({{< relref "/languages/lua/lua-nil-error" >}}) — call nil as function
- [lua-type-error]({{< relref "/languages/lua/lua-type-error" >}}) — type error
- [lua-runtime-error]({{< relref "/languages/lua/lua-runtime-error" >}}) — runtime error
