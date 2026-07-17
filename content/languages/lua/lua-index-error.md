---
title: "[Solution] Lua Index Error Fix"
description: "Fix Lua index out of range errors. Learn why table indexing fails and how to access elements safely."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["index", "range", "table", "lua"]
weight: 5
---

## What This Error Means

A Lua index error occurs when you access a table element at an index that does not exist or is out of range. In Lua, accessing a nil value from a table returns nil, but indexing nil causes an error.

## Common Causes

- Accessing non-existent key
- Wrong index type
- Array indexing from wrong start
- Nil table access

## How to Fix

```lua
-- WRONG: Accessing non-existent key
local config = {host = "localhost"}
local port = config.port  -- nil, may cause issues

-- CORRECT: Provide default
local port = config.port or 3000
```

```lua
-- WRONG: Indexing nil
local obj = nil
print(obj.field)  -- attempt to index nil

-- CORRECT: Check for nil
if obj then
    print(obj.field)
end
```

## Examples

```lua
-- Example 1: Safe table access
local function safe_get(table, key)
    if type(table) == "table" then
        return table[key]
    end
    return nil
end

-- Example 2: Array access
local arr = {1, 2, 3}
print(arr[1])  -- 1 (Lua arrays start at 1)
print(arr[4])  -- nil

-- Example 3: Nested access
local config = {database = {host = "localhost"}}
local host = config.database and config.database.host
```

## Related Errors

- [Lua nil error](lua-nil-error) - nil access
- [Lua type error](lua-type-error) - type mismatch
- [Lua runtime error](lua-runtime-error) - runtime issue
