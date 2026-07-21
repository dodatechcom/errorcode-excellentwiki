---
title: "[Solution] Lua Load Error"
description: "Fix Lua load/loadstring errors when loading code."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

Load errors occur when load() or loadstring() encounters invalid code.

## Common Causes

- Syntax error in loaded string
- Invalid chunk name
- Missing load function
- Non-string argument

## How to Fix

### 1. Validate code before loading

```lua
local function safeLoad(code)
  if type(code) ~= "string" then return nil, "Not a string" end
  local fn, err = load(code)
  if fn == nil then
    return nil, err
  end
  return fn
end
```

### 2. Use load correctly

```lua
local code = "return 42"
local fn = load(code)
if fn then
  print(fn())  -- 42
end
```

## Examples

```lua
-- Dynamic code loading
local function executeCode(code, env)
  local fn, err = load(code, "dynamic", "t", env)
  if fn then
    return fn()
  else
    return nil, err
  end
end

local result = executeCode("return 2 + 2", {})
print(result)  -- 4
```

## Related Errors

- [Syntax error](/languages/lua/lua-syntax-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
