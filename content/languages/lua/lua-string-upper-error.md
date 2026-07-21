---
title: "[Solution] Lua String Upper Error"
description: "Fix Lua string.upper errors when converting to uppercase."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

String upper errors occur when string.upper is called on non-strings.

## Common Causes

- Non-string input
- Missing argument
- Table or number passed
- Nil value passed

## How to Fix

### 1. Validate input

```lua
local function safeUpper(s)
  if type(s) ~= "string" then return "" end
  return string.upper(s)
end
```

### 2. Use string.upper

```lua
print(string.upper("hello"))  -- "HELLO"
```

## Examples

```lua
-- Title case
local function titleCase(s)
  return s:gsub("(%a)([%w']*)", function(first, rest)
    return first:upper() .. rest:lower()
  end)
end

print(titleCase("hello world"))  -- "Hello World"
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Type error](/languages/lua/lua-type-error)
