---
title: "[Solution] Lua String Concatenation Error Fix"
description: "Fix Lua string concatenation errors. Learn why string operations fail and how to handle strings properly."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["string", "concatenation", "concat", "lua"]
weight: 5
---

## What This Error Means

A Lua string concatenation error occurs when you try to concatenate incompatible types, like nil or tables, with the .. operator.

## Common Causes

- Concatenating nil
- Concatenating tables
- Wrong type in concatenation
- Large string operations

## How to Fix

```lua
-- WRONG: Concatenating nil
local name = nil
print("Hello, " .. name)  -- attempt to concatenate nil

-- CORRECT: Provide default
print("Hello, " .. (name or "World"))
```

```lua
-- WRONG: Concatenating table
local data = {1, 2, 3}
print("Data: " .. data)  -- attempt to concatenate table

-- CORRECT: Convert to string
local data = {1, 2, 3}
print("Data: " .. table.concat(data, ", "))
```

## Examples

```lua
-- Example 1: Safe concatenation
local function safe_concat(...)
    local parts = {}
    for i = 1, select("#", ...) do
        local v = select(i, ...)
        parts[i] = tostring(v or "nil")
    end
    return table.concat(parts, " ")
end

-- Example 2: String building
local parts = {}
for i = 1, 1000 do
    parts[#parts + 1] = "item" .. i
end
local result = table.concat(parts, ", ")

-- Example 3: Type-safe concatenation
local function concat(a, b)
    return tostring(a) .. tostring(b)
end
```

## Related Errors

- [Lua nil error](lua-nil-error) - nil access
- [Lua type error](lua-type-error) - type mismatch
- [Lua runtime error](lua-runtime-error) - runtime issue
