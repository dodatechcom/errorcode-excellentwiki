---
title: "[Solution] Lua Infinite Recursion Fix"
description: "Fix Lua infinite recursion errors. Learn why recursive functions cause stack overflow and how to prevent it."
languages: ["lua"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["recursion", "infinite", "stack", "lua"]
weight: 5
---

## What This Error Means

A Lua infinite recursion error occurs when a function calls itself without a proper termination condition, eventually causing a stack overflow.

## Common Causes

- Missing base case
- Wrong termination condition
- Mutual recursion without termination
- Accidental self-reference

## How to Fix

```lua
-- WRONG: Missing base case
function factorial(n)
    return n * factorial(n - 1)  -- Never stops
end

-- CORRECT: Add base case
function factorial(n)
    if n <= 1 then return 1 end
    return n * factorial(n - 1)
end
```

```lua
-- WRONG: Wrong termination
function countDown(n)
    if n > 0 then  -- Should be >= or <=
        print(n)
        countDown(n)
    end
end

-- CORRECT: Proper termination
function countDown(n)
    if n > 0 then
        print(n)
        countDown(n - 1)  -- Decrements toward 0
    end
end
```

## Examples

```lua
-- Example 1: Safe recursion with accumulator
function sum(n, acc)
    acc = acc or 0
    if n == 0 then return acc end
    return sum(n - 1, acc + n)
end

-- Example 2: Convert to iteration
function fibonacci(n)
    if n <= 1 then return n end
    local a, b = 0, 1
    for i = 2, n do
        a, b = b, a + b
    end
    return b
end

-- Example 3: Tail recursion optimization
function gcd(a, b)
    if b == 0 then return a end
    return gcd(b, a % b)  -- Tail recursive
end
```

## Related Errors

- [Lua stack overflow](lua-stack-overflow) - stack overflow
- [Lua memory error](lua-memory-error) - memory allocation
- [Lua instruction limit](lua-instruction-limit) - instruction limit
