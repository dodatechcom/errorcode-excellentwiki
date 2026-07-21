---
title: "[Solution] Lua Type Check Error"
description: "Fix Lua type checking errors when validating variable types."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Type check errors occur when type() is used incorrectly or type validation fails.

## Common Causes

- Wrong type() usage
- Not checking for nil
- Missing type validation
- Comparing wrong types

## How to Fix

### 1. Use type() correctly

```lua
if type(x) == "string" then
  -- use as string
end
```

### 2. Create validation function

```lua
local function assertType(val, expectedType, name)
  local actualType = type(val)
  if actualType ~= expectedType then
    error(name .. ": expected " .. expectedType .. ", got " .. actualType)
  end
  return val
end
```

## Examples

```lua
-- Type checking utilities
local function isString(x) return type(x) == "string" end
local function isNumber(x) return type(x) == "number" end
local function isTable(x) return type(x) == "table" end
local function isFunction(x) return type(x) == "function" end

-- Usage
local function process(value)
  assert(isString(value), "Value must be a string")
  return value:upper()
end
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Nil value error](/languages/lua/lua-nil-value)
