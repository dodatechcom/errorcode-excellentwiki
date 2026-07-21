---
title: "Julia InexactError Float to Int Conversion"
description: "Fix Julia InexactError when converting floating point numbers to integers that cannot represent the value exactly."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

`InexactError` occurs when you try to convert a floating-point number to an integer type but the value has a fractional part, or when the value exceeds the integer type's range.

## Common Causes

- Converting Float64 with fractional part to Int
- Value exceeds Int32 or UInt8 range
- Using `convert` instead of `round` or `floor`
- Forcing type conversion with `::Int` on non-integer float
- NaN or Inf conversion to integer

## How to Fix

```julia
# WRONG: Fractional float to Int
x::Int = 3.14  # InexactError: Int64(3.14)

# CORRECT: Round first
x::Int = round(Int, 3.14)  # 3
# or
x::Int = floor(Int, 3.14)  # 3
```

```julia
# WRONG: Value out of range
x::UInt8 = 300  # InexactError: UInt8(300)

# CORRECT: Use appropriate type
x::Int = 300  # works with Int64
```

## Examples

```julia
# Example 1: Safe conversion
x = 3.7
n = round(Int, x)  # 4
n = floor(Int, x)  # 3
n = ceil(Int, x)   # 4

# Example 2: Truncation
x = -2.9
n = trunc(Int, x)  # -2

# Example 3: Type assertion with conversion
function process(x::Float64)
    round(Int, x)
end
process(42.0)   # 42
process(42.5)   # 42 (rounds to even)
process(43.5)   # 44 (rounds to even)
```

## Related Errors

- [OverflowError](julia-overflow-error) -- arithmetic overflow
- [TypeError](julia-type-error) -- type assertion failures
