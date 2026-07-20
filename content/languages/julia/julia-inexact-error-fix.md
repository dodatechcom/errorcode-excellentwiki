---
title: "[Solution] Julia InexactError Type Conversion Fix"
description: "Fix Julia InexactError when a value cannot be converted exactly to the target type."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1154
---

## What This Error Means

An InexactError occurs when converting a value to a type that cannot represent it exactly, such as converting a float to an integer when the value is not an integer.

## Common Causes

- Converting float with fractional part to integer
- Converting large integer to smaller integer type
- Converting negative to unsigned type

## How to Fix

```julia
convert(Int, 3.14)   # InexactError

convert(Int, 3)      # 3
convert(Int, trunc(3.14))  # 3
Int(round(3.14))     # 3
```

```julia
convert(UInt8, 300)  # InexactError (300 > 255)

convert(UInt8, 255)  # 255
mod(300, 256)        # 44
```

```julia
x = 3.14
Int(trunc(x))   # 3
floor(Int, x)   # 3
ceil(Int, x)    # 4
round(Int, x)   # 3
```

## Related Errors

- [Julia InexactError](julia-inexact-error) - inexact error
- [Julia OverflowError](julia-overflow-error) - overflow error
- [Julia TypeError](julia-type-error) - type error
