---
title: "[Solution] Julia DomainError Mathematical Domain Fix"
description: "Fix Julia DomainError when a mathematical operation receives an input outside its domain."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1153
---

## What This Error Means

A DomainError occurs when a mathematical function is called with an argument outside its valid domain (e.g., sqrt of a negative number).

## Common Causes

- sqrt of negative number
- log of non-positive number
- acos/asin of value outside [-1, 1]
- Division by zero in integer arithmetic

## How to Fix

```julia
sqrt(-1)   # DomainError

sqrt(complex(-1))  # 0.0 + 1.0im
sqrt(abs(-1))      # 1.0
```

```julia
log(-5)   # DomainError

log(abs(-5))  # 1.609...
```

```julia
function safe_sqrt(x)
    if x < 0
        return sqrt(complex(x))
    end
    return sqrt(x)
end

println(safe_sqrt(-4))  # 0.0 + 2.0im
```

## Related Errors

- [Julia DomainError](julia-domain-error) - domain error
- [Julia InexactError](julia-inexact-error) - inexact error
- [Julia DivideError](divide-zero) - division by zero
