---
title: "stack overflow"
description: "A stack overflow occurs when the call stack exceeds its maximum depth due to infinite recursion."
languages: ["lua"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `stack overflow` error occurs when a function calls itself recursively without reaching a base case, causing the call stack to exceed its memory limit. Lua has a default stack limit of about 200 levels.

## Common Causes

- Infinite recursion with no base case
- Very deep recursion
- Mutual recursion without termination
- Missing termination condition

## How to Fix

```lua
-- WRONG: No base case
function factorial(n)
    return n * factorial(n - 1)  -- stack overflow
end

-- CORRECT: Add base case
function factorial(n)
    if n <= 0 then return 1 end
    return n * factorial(n - 1)
end
```

```lua
-- WRONG: Deep recursion
function sum_list(lst, idx)
    if idx > #lst then return 0 end
    return lst[idx] + sum_list(lst, idx + 1)  -- may overflow for large lists
end

-- CORRECT: Use iteration
function sum_list(lst)
    local sum = 0
    for i = 1, #lst do
        sum = sum + lst[i]
    end
    return sum
end
```

## Examples

```lua
-- Example 1: Infinite recursion
function f()
    return f()
end
f()  -- stack overflow

-- Example 2: Missing base case
function count(n)
    return 1 + count(n - 1)
end
count(10000)  -- stack overflow

-- Example 3: Mutual recursion
function is_even(n)
    if n == 0 then return true end
    return is_odd(n - 1)
end
function is_odd(n)
    if n == 0 then return false end
    return is_even(n - 1)
end
is_even(10000)  -- stack overflow
```

## Related Errors

- [script error](/languages/lua/script-error)
- [attempt to index nil](/languages/lua/nil-index)
