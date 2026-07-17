---
title: "[Solution] Lua Syntax Error Near Unexpected Token"
description: "Fix Lua syntax errors when parsing fails. Debug unexpected tokens, missing keywords, and incorrect syntax."
languages: ["lua"]
error-types: ["syntax-error"]
severities: ["error"]
tags: ["syntax", "parse", "token", "compile", "lua"]
weight: 5
---

## What This Error Means

A Lua syntax error occurs when the Lua parser encounters tokens that don't match the expected syntax. The error message typically indicates the line and the unexpected token.

## Common Causes

- Missing `then` after `if` or `elseif`
- Missing `do` after `for` or `while`
- Incorrect function call syntax
- Missing `end` keyword
- Wrong operator usage

## How to Fix

```lua
-- WRONG: Missing then
if x > 5
    print("big")  -- Error: then expected near 'print'

-- CORRECT: Add then
if x > 5 then
    print("big")
end
```

```lua
-- WRONG: Missing do
for i = 1, 10
    print(i)  -- Error: do expected near 'print'

-- CORRECT: Add do
for i = 1, 10 do
    print(i)
end
```

```lua
-- WRONG: Function syntax error
function add(a, b)
return a + b  -- Works but missing end

-- CORRECT: Proper function syntax
function add(a, b)
    return a + b
end
```

## Examples

```lua
-- Example 1: Common syntax patterns
-- if/then/end
if condition then
    action()
elseif other then
    other_action()
else
    default_action()
end

-- for/do/end
for i = 1, 10 do
    print(i)
end

-- while/do/end
while condition do
    process()
end

-- function/end
function myFunc(arg)
    return arg
end

-- Example 2: Check syntax without running
-- lua -e "loadfile('script.lua')"

-- Example 3: Table constructor syntax
local t = {a = 1, b = 2, c = 3}
local arr = {1, 2, 3, [5] = 5}
```

## Related Errors

- [lua-runtime-error]({{< relref "/languages/lua/lua-runtime-error" >}}) — runtime error
- [lua-argument-error]({{< relref "/languages/lua/lua-argument-error" >}}) — argument error
- [lua-type-error]({{< relref "/languages/lua/lua-type-error" >}}) — type error
