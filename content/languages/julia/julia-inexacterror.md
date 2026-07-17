---
title: "InexactError in Julia"
description: "Julia raises InexactError when converting between numeric types loses precision"
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `InexactError` is thrown when converting a floating-point number to an integer (or other type) would lose precision. Julia's `convert` function throws this error instead of silently rounding.

## Common Causes

- Converting Float64 to Int without rounding
- Assigning non-integer value to typed array
- Integer overflow in conversion
- Lossy type conversion

## How to Fix

Use explicit rounding:

```julia
x = 3.7
y = round(Int, x)  # 4 (rounds to nearest)
z = floor(Int, x)  # 3 (rounds down)
w = ceil(Int, x)   # 4 (rounds up)
```

Check before converting:

```julia
function safe_to_int(x::Float64)
    if isinteger(x)
        return Int(x)
    else
        throw(ArgumentError("Cannot convert $x to Int exactly"))
    end
end
```

Use `trunc` for truncation:

```julia
x = 3.9
y = trunc(Int, x)  # 3 (truncate toward zero)
```

Handle array element types:

```julia
# Wrong
arr = Vector{Int}(undef, 3)
arr[1] = 3.14  # InexactError

# Correct
arr = Vector{Float64}(undef, 3)
arr[1] = 3.14
```

## Examples

```julia
x = 3.14
y = Int(x)  # InexactError: truncating Int64 from 3.14

matrix = zeros(Int, 2, 2)
matrix[1, 1] = 1.5  # InexactError
```

## Related Errors

- [TypeError]({{< relref "/languages/julia/type-error" >}})
- [ArgumentError]({{< relref "/languages/julia/argumenterror" >}})
