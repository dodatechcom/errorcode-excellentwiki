---
title: "[Solution] Lua String Gsub Error"
description: "Fix Lua string.gsub pattern substitution errors."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

String gsub errors occur when pattern substitution fails.

## Common Causes

- Invalid replacement string
- Pattern with unbalanced captures
- Replacement function error
- Missing pattern argument

## How to Fix

### 1. Use proper replacement syntax

```lua
local s = "Hello World"
local result = s:gsub("World", "Lua")
print(result)  -- "Hello Lua"
```

### 2. Use function replacement

```lua
local result = s:gsub("(%a+)", function(w)
  return w:upper()
end)
```

## Examples

```lua
-- Replace all vowels
local s = "hello world"
local result = s:gsub("[aeiou]", "*")
print(result)  -- "h*ll* w*rld"

-- Function replacement
local result2 = s:gsub("(%a+)", function(w)
  return w:reverse()
end)
print(result2)  -- "olleh dlrow"
```

## Related Errors

- [Pattern error](/languages/lua/lua-pattern-error)
- [Runtime error](/languages/lua/lua-runtime-error)
- [String format error](/languages/lua/lua-string-format-error)
