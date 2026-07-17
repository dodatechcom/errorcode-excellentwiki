---
title: "DivideError: integer division error"
description: "A DivideError occurs when attempting to divide an integer by zero."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `DivideError` is thrown when you attempt to divide an integer by zero. This is distinct from floating-point division by zero, which returns `Inf` or `NaN`. Integer division by zero has no defined result and raises an error.

## Common Causes

- Dividing by a variable that evaluates to zero
- Incorrect loop or calculation producing a zero divisor
- Missing zero-check before division
- Computing denominator from user input without validation

## How to Fix

```julia
# WRONG: No zero check
function divide(a, b)
    return a / b
end
divide(10, 0)  # DivideError

# CORRECT: Check for zero before dividing
function divide(a, b)
    b == 0 && error("division by zero")
    return a / b
end
divide(10, 0)  # Error: division by zero
```

```julia
# WRONG: Using integer division without check
a = 10
b = 0
c = div(a, b)  # DivideError

# CORRECT: Validate divisor
if b != 0
    c = div(a, b)
else
    println("Cannot divide by zero")
end
```

## Examples

```julia
# Example 1: Direct integer division by zero
result = 5 \ 0     # DivideError: integer division error

# Example 2: Variable divisor
x = 0
y = 10 ÷ x        # DivideError: integer division error

# Example 3: Function with zero divisor
function average(arr)
    sum(arr) ÷ length(arr)  # crashes if arr is empty
end
average(Int[])     # DivideError
```

## Related Errors

- [BoundsError: attempt to access X at index [Y]](/languages/julia/bounds-error)
- [MethodError: no method matching X](/languages/julia/type-error)
