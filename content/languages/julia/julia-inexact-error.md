---
title: "[Solution] Julia InexactError — Integer Conversion Failed"
description: "Fix Julia InexactError when converting floating-point to integer. Learn rounding, truncation, and safe numeric conversions."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An `InexactError` is thrown when you try to convert a floating-point number to an integer but the value has a fractional part that cannot be represented exactly. Julia's `convert(Int, 3.5)` throws `InexactError` because 3.5 is not exactly representable as an integer.

## Why It Happens

The most common cause is calling `Int(3.5)` or `convert(Int, 3.5)` on a non-integer float. Julia does not automatically truncate or round because different rounding modes are needed for different use cases.

Another frequent cause is converting `NaN` or `Inf` to an integer. These special float values have no integer representation, so any conversion attempt fails.

Large floating-point values that exceed the integer type's range also cause this error. `Int(1e20)` throws `InexactError` because 10^20 is larger than `typemax(Int64)`.

Rational number conversions can also fail. Converting `3//2` (which is 1.5 as a rational) to `Int` fails for the same reason as float-to-int conversion.

## How to Fix It

### Use explicit rounding functions

```julia
# Wrong — InexactError
Int(3.5)

# Correct — choose your rounding strategy
round(Int, 3.5)    # 4 (rounds to nearest)
floor(Int, 3.5)    # 3 (rounds down)
ceil(Int, 3.5)     # 4 (rounds up)
trunc(Int, 3.5)    # 3 (truncates toward zero)
```

### Check for special values before conversion

```julia
function safe_int(x::Float64)
    if isnan(x) || isinf(x)
        throw(ArgumentError("Cannot convert $x to integer"))
    end
    round(Int, x)
end
```

### Use checked conversion

```julia
function safe_convert(::Type{Int}, x::Float64)
    if x > typemax(Int) || x < typemin(Int)
        throw(OverflowError("Value $x out of range for Int"))
    end
    round(Int, x)
end
```

### Use floating-point for approximate integer arithmetic

```julia
# When you need the fractional part
result = floor(3.5)  # Returns 3.0 as Float64
```

### Handle NaN and Inf explicitly

```julia
function process_float(x)
    isnan(x) && return 0
    isinf(x) && return x > 0 ? typemax(Int) : typemin(Int)
    round(Int, x)
end
```

## Common Mistakes

- Using `Int(float)` instead of `round(Int, float)`
- Not checking for `NaN` and `Inf` before integer conversion
- Assuming `convert(Int, x)` works the same as `round(Int, x)`
- Not handling overflow for very large floating-point values
- Using `trunc` when `round` is more appropriate

## Related Pages

- [Julia OverflowError](/languages/julia/julia-overflowerror/)
- [Julia ArgumentError](/languages/julia/julia-argumenterror/)
- [Julia DomainError](/languages/julia/julia-domainsingularity/)
