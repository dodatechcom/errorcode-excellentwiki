---
title: "DomainError in Julia"
description: "Julia raises DomainError when a mathematical function receives a value outside its valid domain"
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["domain", "math", "singular", "domainerror", "function"]
weight: 5
---

## What This Error Means

A `DomainError` is thrown when a mathematical function receives a value outside its valid domain. For example, taking the square root of a negative number or logarithm of zero.

## Common Causes

- Square root of negative number (real domain)
- Logarithm of zero or negative number
- Inverse trigonometric function outside [-1, 1]
- Division by zero in mathematical context

## How to Fix

Check domain before calling function:

```julia
function safe_sqrt(x::Real)
    if x < 0
        throw(DomainError(x, "sqrt requires non-negative argument"))
    end
    sqrt(x)
end
```

Use complex numbers for extended domain:

```julia
x = -1.0
y = sqrt(x)        # DomainError
z = sqrt(complex(x))  # Works: 0.0 + 1.0im
```

Handle edge cases:

```julia
function safe_log(x::Real)
    if x <= 0
        throw(DomainError(x, "log requires positive argument"))
    end
    log(x)
end
```

Use `clamp` for bounded functions:

```julia
function asin_safe(x::Real)
    if abs(x) > 1
        throw(DomainError(x, "asin requires -1 <= x <= 1"))
    end
    asin(x)
end
```

## Examples

```julia
sqrt(-1.0)    # DomainError: sqrt was asked to return the real square root of a negative number
log(0.0)      # DomainError: log was asked to return the real logarithm of a negative number
asin(2.0)     # DomainError: asin was asked to return a real result from a domain error
```

## Related Errors

- [ArgumentError]({{< relref "/languages/julia/argumenterror" >}})
- [InexactError]({{< relref "/languages/julia/inexact-error" >}})
