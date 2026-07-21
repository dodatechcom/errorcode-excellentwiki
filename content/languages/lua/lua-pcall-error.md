---
title: "[Solution] Lua Pcall Xpcall Error"
description: "Fix Lua pcall/xpcall error handling function errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Pcall/xpcall errors occur when error handling functions are misused.

## Common Causes

- Wrong number of arguments
- Error handler not a function
- pcall with non-function
- Missing error handler

## How to Fix

### 1. Use pcall correctly

```lua
local ok, result = pcall(function()
  return 42
end)

if ok then
  print(result)
end
```

### 2. Use xpcall with handler

```lua
local ok, err = xpcall(function()
  error("something went wrong")
end, function(e)
  return "caught: " .. tostring(e)
end)
```

## Examples

```lua
-- Safe division
local function safeDivide(a, b)
  local ok, result = pcall(function()
    return a / b
  end)
  if ok then
    return result
  else
    return nil, "Division error"
  end
end

print(safeDivide(10, 2))   -- 5
print(safeDivide(10, 0))   -- nil, "Division error"
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Error handler error](/languages/lua/lua-error-handler-error)
