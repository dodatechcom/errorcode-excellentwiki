---
title: "[Solution] Lua Table Remove Error"
description: "Fix Lua table.remove errors when removing elements from tables."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Table remove errors occur when table.remove is called with invalid arguments.

## Common Causes

- Position out of bounds
- Position is zero or negative
- Table is nil or not a table
- Position exceeds table length

## How to Fix

### 1. Check bounds before removal

```lua
if pos >= 1 and pos <= #t then
  table.remove(t, pos)
end
```

### 2. Safe remove function

```lua
local function safeRemove(t, pos)
  if type(t) ~= "table" then return nil end
  pos = pos or #t
  if pos < 1 or pos > #t then return nil end
  return table.remove(t, pos)
end
```

## Examples

```lua
local list = {"a", "b", "c", "d"}
local removed = table.remove(list, 2)
print(removed)        -- "b"
print(table.concat(list, ", "))  -- "a, c, d"
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)
