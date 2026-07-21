---
title: "[Solution] Lua String Find Error"
description: "Fix Lua string.find errors when pattern matching."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
---

String find errors occur when string.find pattern matching fails or is used incorrectly.

## Common Causes

- Invalid pattern syntax
- Pattern too complex
- Missing pattern argument
- Plain mode mismatch

## How to Fix

### 1. Use proper pattern syntax

```lua
local s = "Hello World"
local start, finish = string.find(s, "World")
print(start, finish)  -- 7 11
```

### 2. Use plain matching when needed

```lua
local function findLiteral(s, literal)
  return string.find(s, literal, 1, true)
end
```

## Examples

```lua
-- Basic find
local s = "Hello World"
local pos = string.find(s, "World")
print(pos)  -- 7

-- With captures
local start, finish, word = string.find(s, "(%a+)")
print(word)  -- "Hello"
```

## Related Errors

- [Runtime error](/languages/lua/lua-runtime-error)
- [Bad argument error](/languages/lua/lua-bad-argument-error)
- [Pattern error](/languages/lua/lua-pattern-error)
