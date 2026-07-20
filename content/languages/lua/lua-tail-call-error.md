---
title: "[Solution] Lua Tail Call Recursion Error Fix"
description: "Fix Lua tail call errors when using tail-recursive functions and stack management."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1139
---

## What This Error Means

A tail call error occurs when Lua cannot perform a tail call optimization. Lua supports proper tail calls if certain conditions are met, and violations cause stack growth instead of constant-space recursion.

## Common Causes

- Not using `return` before the tail call
- Adding operations after the tail call (e.g., return fn() + 1)
- Wrapping the tail call in a table or expression
- Using the tail call inside a non-tail position (e.g., in conditional branches)
- The called function is not immediately returned

## How to Fix

```lua
-- WRONG: Not returning the recursive call
function factorial(n)
    if n <= 1 then return 1 end
    n * factorial(n - 1)  -- Not a tail call (result used)
end

-- CORRECT: Accumulator pattern (tail-recursive)
function factorial(n, acc)
    acc = acc or 1
    if n <= 1 then return acc end
    return factorial(n - 1, n * acc)  -- Tail call!
end

print(factorial(10000))  -- Works without stack overflow
```

```lua
-- WRONG: Operation after tail call
function process(lst, acc)
    if #lst == 0 then return acc end
    return process({table.unpack(lst, 2)}, acc + lst[1])  -- Still not tail?
end

-- CORRECT: Pure tail call with proper structure
function sum(lst, acc)
    acc = acc or 0
    if #lst == 0 then return acc end
    return sum({table.unpack(lst, 2)}, acc + lst[1])
end
```

```lua
-- WRONG: Tail call inside expression
function max(lst, m)
    m = m or -math.huge
    if #lst == 0 then return m end
    return max({table.unpack(lst, 2)}, math.max(m, lst[1]))
end

-- CORRECT: Tail call must be the last operation
function max(lst, m)
    if #lst == 0 then return m end
    local first = lst[1]
    m = m or first
    return max({table.unpack(lst, 2)}, m > first and m or first)
end
```

```lua
-- WRONG: Not a tail call because of the 'and' guard
function safe_tail(n)
    if n > 0 then
        return safe_tail(n - 1)  -- This IS a tail call (in if branch)
    end
    return "done"
end

-- This works correctly as tail call
```

```lua
-- Properly tail-recursive even function
local function is_even_tail(n, parity)
    parity = parity or 0
    if n == 0 then return parity == 0 end
    return is_even_tail(n - 1, 1 - parity)
end

print(is_even_tail(100000))  -- true (no stack overflow)
```

## Examples

```lua
-- Tail-recursive list reversal
local function reverse_tail(lst, acc)
    acc = acc or {}
    if #lst == 0 then return acc end
    table.insert(acc, 1, lst[1])
    return reverse_tail({table.unpack(lst, 2)}, acc)
end

local rev = reverse_tail({1, 2, 3, 4, 5})
for _, v in ipairs(rev) do print(v) end
```

## Related Errors

- [Lua stack overflow](lua-stack-overflow) - stack overflow
- [Lua recursive error](lua-recursive-error) - recursion issue
- [Lua runtime error](lua-runtime-error) - runtime issue
