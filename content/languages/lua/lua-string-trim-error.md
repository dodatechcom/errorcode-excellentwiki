---
title: "[Solution] Lua String Trim Error"
description: "Fix Lua string trim errors when removing whitespace."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

String trim errors occur when custom trim implementations are incorrect.

## Common Causes

- Lua has no built-in trim
- Pattern not matching whitespace correctly
- Trim function returns nil
- Edge cases with empty strings

## How to Fix

### 1. Use standard trim pattern

```lua
function string.trim(s)
  return s:match("^%s*(.-)%s*$")
end
```

### 2. Use gsub for trimming

```lua
function string.trim(s)
  return s:gsub("^%s+", ""):gsub("%s+$", "")
end
```

## Examples

```lua
-- Trim whitespace
local function trim(s)
  return s:match("^%s*(.-)%s*$")
end

print(trim("  hello  "))  -- "hello"
print(trim("hello"))      -- "hello"
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Pattern error](/languages/lua/lua-pattern-error)
- [String find error](/languages/lua/lua-string-find-error)
