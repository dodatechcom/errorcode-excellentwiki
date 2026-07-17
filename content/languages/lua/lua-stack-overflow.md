---
title: "[Solution] Lua Stack Overflow Fix"
description: "Fix Lua stack overflow errors. Learn why stack overflow occurs and how to prevent deep recursion."
languages: ["lua"]
severities: ["error"]
error-types: ["memory-error"]
tags: ["stack-overflow", "recursion", "stack", "lua"]
weight: 5
---

## What This Error Means

A Lua stack overflow occurs when the call stack exceeds its limit, typically caused by infinite or very deep recursion. Each function call adds a frame to the stack.

## Common Causes

- Infinite recursion
- Very deep recursive calls
- Circular function calls
- Missing base case

## How to Fix

```lua
-- WRONG: Infinite recursion
function countDown(n)
    countDown(n)  -- No base case
end

-- CORRECT: Add base case
function countDown(n)
    if n <= 0 then return end
    print(n)
    countDown(n - 1)
end
```

```lua
-- WRONG: Deep recursion on large input
function fibonacci(n)
    if n <= 1 then return n end
    return fibonacci(n - 1) + fibonacci(n - 2)
end

-- CORRECT: Use iteration
function fibonacci(n)
    if n <= 1 then return n end
    local a, b = 0, 1
    for i = 2, n do
        a, b = b, a + b
    end
    return b
end
```

## Examples

```lua
-- Example 1: Tail recursion
function sum(n, acc)
    acc = acc or 0
    if n == 0 then return acc end
    return sum(n - 1, acc + n)
end

-- Example 2: Iterative alternative
function factorial(n)
    local result = 1
    for i = 2, n do
        result = result * i
    end
    return result
end

-- Example 3: Trampoline pattern
function trampoline(fn)
    return function(...)
        local result = fn(...)
        while type(result) == "function" do
            result = result()
        end
        return result
    end
end
```

## Related Errors

- [Lua memory error](lua-memory-error) - memory allocation
- [Lua instruction limit](lua-instruction-limit) - instruction limit
- [Lua runtime error](lua-runtime-error) - runtime issue
