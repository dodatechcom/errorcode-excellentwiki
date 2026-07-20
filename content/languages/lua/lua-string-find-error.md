---
title: "[Solution] Lua string.find Pattern Match Error Fix"
description: "Fix Lua string.find pattern matching errors when searching within strings."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1109
---

## What This Error Means

A string.find error occurs when pattern matching fails due to special characters, magic characters not being escaped, or invalid pattern syntax.

## Common Causes

- Not escaping magic characters (., %, [, ], *, +, -, ?, ^, $) in literal searches
- Using plain string where pattern matching is intended
- Pattern syntax errors with unbalanced brackets
- Confusing string.find with string.match
- Not handling nil returns when pattern isn't found

## How to Fix

```lua
-- WRONG: Searching for literal dot (.)
local text = "hello.world"
local pos = text:find(".")  -- Matches any character, not literal dot!
-- pos will be 1 (first char matches)

-- CORRECT: Escape magic characters or use plain flag
local pos = text:find("%.")       -- Escape with %
local pos = text:find(".", 1, true)  -- Plain search (no pattern)
-- pos will be 6
```

```lua
-- WRONG: Not handling nil returns
local text = "hello world"
local start, finish = text:find("xyz")  -- nil, nil
print(start)  -- nil - program may crash

-- CORRECT: Check for nil
local start, finish = text:find("xyz")
if start then
    print("Found at", start, finish)
else
    print("Not found")
end
```

```lua
-- WRONG: Unbalanced brackets
local text = "hello [world]"
local pos = text:find("[world")  -- Unbalanced '[' - pattern error

-- CORRECT: Escape with % or balance brackets
local pos = text:find("%[world")  -- Escaped [
local pos = text:find("%[world%]")  -- Find literal [world]
```

```lua
-- WRONG: Confusing string.find with string.match
local text = "today is 2024-01-15"
local result = text:find("%d+")  -- Returns start/end positions
print(result)  -- 10, 13

-- If you want the matched text:
local matched = text:match("%d+")  -- Returns the match
print(matched)  -- 2024
```

```lua
-- Capturing with string.find
local text = "Name: Alice, Age: 30"
local start, finish, name, age = text:find("Name: (%w+), Age: (%d+)")
if start then
    print(name, age)  -- Alice 30
end
```

## Examples

```lua
local function safe_find(text, pattern, init)
    init = init or 1
    local ok, err = pcall(text.find, text, pattern, init, false)
    if not ok then
        return nil, "Invalid pattern: " .. tostring(err)
    end
    return text:find(pattern, init)
end

local pos = safe_find("hello", "(hello")
if pos then
    print("Found at", pos)
end
```

## Related Errors

- [Lua pattern error](lua-pattern-error) - pattern issue
- [Lua string error](lua-string-error) - string issue
- [Lua runtime error](lua-runtime-error) - runtime issue
