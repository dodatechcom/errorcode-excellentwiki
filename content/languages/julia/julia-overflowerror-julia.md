---
title: "OverflowError in Julia"
description: "Julia raises OverflowError when arithmetic operations exceed type limits"
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `OverflowError` occurs when an integer arithmetic operation produces a result that exceeds the maximum value that can be stored in the type. This is common with fixed-width integer types.

## Common Causes

- Integer overflow in arithmetic operations
- Multiplying large numbers that exceed Int64
- Accumulating values without checking bounds
- Using fixed-width types for unbounded calculations

## How to Fix

Use `BigInt` for large numbers:

```julia
# Wrong: overflow with Int64
x = typemax(Int64) + 1  # OverflowError

# Correct: use BigInt
x = BigInt(typemax(Int64)) + 1
```

Check for overflow before operations:

```julia
function safe_add(a::Int, b::Int)
    if a > 0 && b > typemax(Int) - a
        throw(OverflowError("Addition would overflow"))
    end
    a + b
end
```

Use `checked_add` and similar functions:

```julia
import Base: checked_add, checked_mul

result = checked_add(typemax(Int64), 1)  # Throws OverflowError
```

Use `BigFloat` for floating-point overflow:

```julia
x = BigFloat("1e1000")  # Works
y = Float64(x)  # Inf (overflow to infinity)
```

## Examples

```julia
x = typemax(Int64)  # 9223372036854775807
y = x + 1           # OverflowError: arithmetic overflow
```

## Related Errors

- [BoundsError]({{< relref "/languages/julia/bounds-error" >}})
- [InexactError]({{< relref "/languages/julia/inexact-error" >}})
