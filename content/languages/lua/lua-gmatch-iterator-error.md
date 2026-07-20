---
title: "[Solution] Lua string.gmatch Iterator Error Fix"
description: "Fix Lua string.gmatch iterator errors when parsing strings with patterns."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1111
---

## What This Error Means

A string.gmatch error occurs when using the gmatch function to iterate over pattern matches. Common issues include using gmatch in a non-iterator context, incorrect capture groups, or consuming the iterator incorrectly.

## Common Causes

- Using gmatch without a loop (expecting immediate results)
- Wrong number of captures in the pattern
- Trying to reset or reuse a gmatch iterator
- Pattern mismatch causing no matches
- Modifying the source string during iteration

## How to Fix

```lua
-- WRONG: Using gmatch like it returns all matches at once
local text = "a,b,c"
local matches = text:gmatch("(%w)")  -- Creates iterator, not list!
print(matches[1])  -- nil - cannot index an iterator

-- CORRECT: Use in a loop
for match in text:gmatch("(%w)") do
    print(match)
end
-- Or collect into a table
local all = {}
for match in text:gmatch("(%w)") do
    table.insert(all, match)
end
```

```lua
-- WRONG: Number of captures doesn't match expectations
local text = "Alice,30,Boston"
local csv_pattern = "(%w+),(%w+)"  -- Only 2 captures
for first, second, third in text:gmatch(csv_pattern) do
    print(first, second, third)  -- third is nil
end

-- CORRECT: Match all fields
for first, second, third in text:gmatch("(%w+),(%d+),(%w+)") do
    print(first, second, third)  -- Alice, 30, Boston
end
```

```lua
-- WRONG: Trying to reuse an iterator
local text = "1,2,3,4,5"
local iter = text:gmatch("%d+")
for n in iter do
    print(n)
end
-- iter is now exhausted
for n in iter do  -- No more iterations
    print(n)  -- Never runs
end

-- CORRECT: Create new iterator each time
local function get_numbers(str)
    return str:gmatch("%d+")
end
for n in get_numbers(text) do print(n) end
for n in get_numbers(text) do print(n) end
```

```lua
-- Pattern with no captures returns full matches
local text = "hello world"
for word in text:gmatch("%a+") do
    print(word)  -- "hello", "world"
end
```

## Examples

```lua
local csv = "apple,1.99,5\nbanana,0.99,3\n"
for name, price, qty in csv:gmatch("(%w+),(%d+%.?%d*),(%d+)") do
    print(string.format("%s: $%s x %s", name, price, qty))
end
```

## Related Errors

- [Lua pattern error](lua-pattern-error) - pattern issue
- [Lua string error](lua-string-error) - string issue
- [Lua nil call error](lua-nil-call-error) - nil call
