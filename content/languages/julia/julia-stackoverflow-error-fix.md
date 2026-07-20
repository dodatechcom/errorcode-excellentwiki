---
title: "[Solution] Julia StackOverflowError Infinite Recursion Fix"
description: "Fix Julia StackOverflowError when recursive functions overflow the call stack."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1157
---

## What This Error Means

A StackOverflowError occurs when the call stack exceeds the available stack space, typically from infinite or too-deep recursion.

## Common Causes

- Missing base case in recursive function
- Infinite recursion (no termination condition)
- Recursion depth exceeding available stack

## How to Fix

```julia
function factorial(n)
    if n <= 1
        return 1
    end
    return n * factorial(n - 1)
end

factorial(100000)  # StackOverflowError
```

```julia
function factorial_tco(n, acc=1)
    if n <= 1
        return acc
    end
    return factorial_tco(n - 1, n * acc)
end

factorial_tco(100000)  # Still may overflow (Julia doesn't guarantee TCO)
```

```julia
function factorial_iter(n)
    result = 1
    for i in 2:n
        result *= i
    end
    return result
end

factorial_iter(100000)  # Works (may overflow integer)
```

## Related Errors

- [Julia stack overflow](julia-stack-overflow) - stack overflow
- [Julia system error](julia-system-error) - system error
- [Julia runtime error](julia-try-catch) - runtime error
