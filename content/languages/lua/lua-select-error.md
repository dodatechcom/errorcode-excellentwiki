---
title: "[Solution] Lua Select Error"
description: "Fix Lua select() function errors when selecting multiple return values."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Select errors occur when the select() function is used incorrectly.

## Common Causes

- Wrong index argument
- Index out of range
- Not using with varargs
- Missing select arguments

## How to Fix

### 1. Use select correctly

```lua
local function first(...)
  return select(1, ...)
end

local function third(...)
  return select(3, ...)
end
```

### 2. Count arguments

```lua
local function countArgs(...)
  return select("#", ...)
end
```

## Examples

```lua
-- Get first two values
local function firstTwo(...)
  return select(1, ...)
end

local a, b = firstTwo(1, 2, 3, 4)
print(a, b)  -- 1  2

-- Count arguments
print(select("#", 1, 2, 3))  -- 3
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Varargs error](/languages/lua/lua-varargs-error)
