---
title: "StackOverflowError"
description: "A StackOverflowError occurs when the call stack exceeds its maximum depth, typically due to infinite recursion."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `StackOverflowError` is thrown when a function calls itself recursively without a proper termination condition, causing the call stack to grow beyond its allocated memory limit. Each function call consumes stack space, and eventually the system runs out.

## Common Causes

- Infinite recursion with no base case
- Recursive function that never reaches its termination condition
- Very deep recursion on large data structures
- Mutually recursive functions calling each other indefinitely

## How to Fix

```julia
# WRONG: No base case
function countdown(n)
    return countdown(n - 1)  # StackOverflowError
end

# CORRECT: Add base case
function countdown(n)
    n <= 0 && return 0
    return n + countdown(n - 1)
end
```

```julia
# WRONG: Mutual recursion without termination
function is_even(n)
    n == 0 ? true : is_odd(n - 1)
end
function is_odd(n)
    n == 0 ? false : is_even(n - 1)
end

# CORRECT: Use modulo
function is_even(n)
    n % 2 == 0
end
```

## Examples

```julia
# Example 1: Infinite recursion
function fact(n)
    return n * fact(n - 1)  # no base case
end
fact(5)  # StackOverflowError

# Example 2: Incorrect base case
function sum_list(lst)
    isempty(lst) && return 0
    return first(lst) + sum_list(lst)  # should be tail(lst)
end

# Example 3: Mutual recursion
f(n) = n == 0 ? 0 : g(n)
g(n) = n == 0 ? 0 : f(n)
f(10000)  # StackOverflowError
```

## Related Errors

- [BoundsError: attempt to access X at index [Y]](/languages/julia/bounds-error)
- [MethodError: no method matching X](/languages/julia/type-error)
