---
title: "[Solution] Lua Table Indexing Error Fix"
description: "Fix Lua table indexing errors when accessing or modifying table elements incorrectly."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1100
---

## What This Error Means

A table indexing error in Lua occurs when you try to access an index that doesn't exist in a table, or when you use invalid index types. Lua tables can be indexed by any type except nil.

## Common Causes

- Accessing a table key that hasn't been set
- Using nil as a table index
- Confusing array-style indexing with hash-style indexing
- Off-by-one errors with Lua's 1-based indexing
- Using a floating-point number that looks like an integer

## How to Fix

```lua
-- WRONG: Indexing with nil
local t = { a = 1 }
local key = nil
print(t[key])  -- error: table index is nil

-- CORRECT: Use a valid key
local key = "a"
print(t[key])  -- 1
```

```lua
-- WRONG: Off-by-one (Lua is 1-based)
local arr = {10, 20, 30}
print(arr[0])  -- nil (not an error, but unexpected)
print(arr[4])  -- nil

-- CORRECT: Use 1-based indices
print(arr[1])  -- 10
print(arr[2])  -- 20
print(arr[3])  -- 30
```

```lua
-- WRONG: Assuming boolean keys work like strings
local t = { true = "yes", false = "no" }
print(t[true])  -- yes

-- CORRECT: Be consistent with key types
local t = { ["true"] = "yes", ["false"] = "no" }
print(t["true"])  -- yes
```

```lua
-- WRONG: Using float that doesn't represent an integer exactly
local t = {1, 2, 3}
print(t[2.0])  -- 2 (2.0 == 2 in Lua)
-- But:
print(t[2.5])  -- nil
```

```lua
-- Check if key exists safely
local t = { name = "Alice" }
if t.name ~= nil then
    print(t.name)
end
-- or
if t["name"] then
    print(t["name"])
end
```

## Examples

```lua
local inventory = {
    gold = 100,
    items = {"sword", "shield", "potion"}
}

print(inventory.gold)          -- 100
print(inventory.items[1])      -- sword
print(inventory.items[#inventory.items]) -- potion
```

## Related Errors

- [Lua nil index error](lua-nil-index-error) - nil index
- [Lua table length error](lua-table-length) - length issue
- [Lua index error](lua-index-error) - general index issue
