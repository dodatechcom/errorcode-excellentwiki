---
title: "[Solution] Lua Syntax Error Fix"
description: "Fix Lua syntax errors. Learn why Lua scripts fail to parse and how to fix syntax issues."
languages: ["lua"]
severities: ["error"]
error-types: ["syntax-error"]
tags: ["syntax", "parse", "lua"]
weight: 5
---

## What This Error Means

A Lua syntax error occurs when the Lua interpreter cannot parse your script. This is a compile-time error that prevents execution.

## Common Causes

- Missing keywords (end, then, do)
- Wrong operator usage
- Unclosed strings or comments
- Indentation issues

## How to Fix

```lua
-- WRONG: Missing end
if condition then
    do_something()
-- Missing end

-- CORRECT: Close all blocks
if condition then
    do_something()
end
```

```lua
-- WRONG: Wrong operator
if x = 5 then  -- Assignment, not comparison
    print("Equal")
end

-- CORRECT: Use == for comparison
if x == 5 then
    print("Equal")
end
```

## Examples

```lua
-- Example 1: Check syntax
-- Run with: lua -e "loadfile('script.lua')"

-- Example 2: Proper block structure
function greet(name)
    if name then
        print("Hello, " .. name)
    else
        print("Hello, stranger")
    end
end

-- Example 3: String concatenation
local str = "Hello" .. ", " .. "World"
```

## Related Errors

- [Lua runtime error](lua-runtime-error) - runtime issue
- [Lua argument error](lua-argument-error) - wrong argument
- [Lua type error](lua-type-error) - type mismatch
