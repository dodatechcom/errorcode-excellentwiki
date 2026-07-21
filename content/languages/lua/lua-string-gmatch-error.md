---
title: "[Solution] Lua String Gmatch Error"
description: "Fix Lua string.gmatch iterator errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

String gmatch errors occur when the iterator from string.gmatch is misused.

## Common Causes

- Invalid pattern in gmatch
- Pattern with unbalanced captures
- Not using iterator results
- Pattern causing infinite loop

## How to Fix

### 1. Use gmatch correctly

```lua
local s = "hello world foo bar"
for word in s:gmatch("%a+") do
  print(word)
end
```

### 2. Collect results

```lua
local function findAll(s, pat)
  local result = {}
  for match in s:gmatch(pat) do
    result[#result + 1] = match
  end
  return result
end
```

## Examples

```lua
local text = "Error 404: File not found"
local codes = {}
for code in text:gmatch("Error (%d+)") do
  codes[#codes + 1] = tonumber(code)
end
print(codes[1])  -- 404
```

## Related Errors

- [Pattern error](/languages/lua/lua-pattern-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [Iterator error](/languages/lua/lua-iterator-error)
