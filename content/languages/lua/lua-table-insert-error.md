---
title: "[Solution] Lua Table Insert Error"
description: "Fix Lua table.insert errors when adding elements to tables."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Table insert errors occur when table.insert is called incorrectly.

## Common Causes

- Invalid position argument
- Inserting nil value
- Table is nil or read-only
- Position out of range

## How to Fix

### 1. Validate position

```lua
local function safeInsert(t, pos, value)
  if value == nil then return end
  pos = pos or #t + 1
  table.insert(t, pos, value)
end
```

### 2. Insert at end

```lua
local t = {}
table.insert(t, 42)  -- Insert at end
```

## Examples

```lua
local list = {1, 2, 3}
table.insert(list, 2, 99)  -- Insert at position 2
print(table.concat(list, ", "))  -- "1, 99, 2, 3"
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)
