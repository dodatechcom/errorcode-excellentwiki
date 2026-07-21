---
title: "[Solution] Lua String Rep Error"
description: "Fix Lua string.rep errors when repeating strings."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

String rep errors occur when string.rep is called incorrectly.

## Common Causes

- Negative repeat count
- Repeat count too large
- Non-string input
- Missing arguments

## How to Fix

### 1. Validate repeat count

```lua
local function safeRep(s, n, sep)
  if n < 0 then return "" end
  sep = sep or ""
  return string.rep(s, n, sep)
end
```

### 2. Use with separator

```lua
local dashes = string.rep("-", 10)
print(dashes)  -- "----------"

local dots = string.rep(".", 5, " ")
print(dots)  -- ". . . . ."
```

## Examples

```lua
-- Box drawing
local width = 40
local function boxLine(char)
  return string.rep(char, width)
end

print("+" .. boxLine("-") .. "+")
print("|" .. string.rep(" ", width) .. "|")
print("+" .. boxLine("-") .. "+")
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)
