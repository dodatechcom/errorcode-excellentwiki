---
title: "[Solution] Lua string.gsub Substitution Error Fix"
description: "Fix Lua string.gsub substitution errors. Learn how to use gsub for string replacement correctly."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1110
---

## What This Error Means

A string.gsub error occurs when performing global string substitution. Common issues include invalid replacement strings, wrong capture group references, or using gsub instead of gmatch.

## Common Causes

- Using %1-style captures in the replacement string incorrectly
- Passing wrong number of arguments
- Not escaping % in replacement strings
- Confusing gsub with gmatch or match
- Not using the correct capture group number

## How to Fix

```lua
-- WRONG: Using %1 in replacement without captures
local text = "hello world"
local result = text:gsub("hello", "%1")  -- No capture group 1

-- CORRECT: Use captures or plain text
local result = text:gsub("(hello)", "%1")  -- Returns "hello world"
local result = text:gsub("hello", "hi")    -- Returns "hi world"
```

```lua
-- WRONG: Not escaping % in replacement
local text = "discount: 50%"
local result = text:gsub("%%", "percent")  -- Wrong: %% is escaped in pattern

-- CORRECT: Handle % in replacement
local result = text:gsub("%%", "%%")  -- Double %% becomes single %
local result = text:gsub("%%", " percent")  -- "discount: 50 percent"
```

```lua
-- WRONG: Using magic chars in replacement without escaping
local text = "hello"
local result = text:gsub("hello", "$1")  -- $ has no special meaning in gsub
print(result)  -- "$1" (literal)

-- CORRECT: Use captures with % references
local result = text:gsub("(h)(ello)", "%1%2")  -- "hello"
local result = text:gsub("(.)", "%1-")  -- "h-e-l-l-o-"
```

```lua
-- Using function as replacement
local text = "hello 42 world 73"
local result = text:gsub("(%d+)", function(n)
    return tostring(tonumber(n) * 2)
end)
print(result)  -- hello 84 world 146
```

```lua
-- Getting replacement count
local text = "apple, banana, apple, orange"
local result, count = text:gsub("apple", "pear")
print(result)  -- "pear, banana, pear, orange"
print(count)   -- 2
```

## Examples

```lua
local text = "First: Alice, Second: Bob"

-- Swap name and position
local result = text:gsub("(%w+): (%w+)", "%2 is %1")
print(result)  -- "Alice is First, Bob is Second"
```

## Related Errors

- [Lua pattern error](lua-pattern-error) - pattern issue
- [Lua string error](lua-string-error) - string issue
- [Lua runtime error](lua-runtime-error) - runtime issue
