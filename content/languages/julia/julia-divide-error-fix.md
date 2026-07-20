---
title: "[Solution] Julia DivideError Integer Division by Zero Fix"
description: "Fix Julia DivideError when dividing an integer by zero."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1155
---

## What This Error Means

A DivideError occurs when an integer division by zero is attempted. In Julia, integer division by zero throws a DivideError, while floating-point division returns Inf or -Inf.

## Common Causes

- Integer division by zero (div(a, 0) or a ÷ 0)
- Integer modulus by zero (rem(a, 0) or mod(a, 0))
- Loop with denominator that can become zero

## How to Fix

```julia
1 / 0    # Inf (floating point, returns Inf)
1 ÷ 0    # DivideError: integer division error
div(1, 0)  # DivideError

function safe_div(a, b)
    if b == 0
        return nothing
    end
    return a / b
end
```

```julia
function safe_div(a::Int, b::Int)
    if b == 0
        return Inf
    end
    return a / b
end
```

```julia
x, y = 10, 0
if y != 0
    println(x ÷ y)
else
    println("Cannot divide by zero")
end
```

## Related Errors

- [Julia divide zero](divide-zero) - division by zero
- [Julia DomainError](julia-domain-error) - domain error
- [Julia OverflowError](julia-overflow-error) - overflow error
