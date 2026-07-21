---
title: "Julia Type Promotion Error in Arithmetic"
description: "Fix Julia TypeError when performing arithmetic operations that require type promotion between incompatible numeric types."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Type promotion errors occur when Julia cannot find a common supertype to perform arithmetic between different numeric types, or when explicit promotion is needed.

## Common Causes

- Mixing incompatible numeric types (e.g., Int and String)
- Custom types missing promote_rule or Number subtyping
- Arithmetic between matrix and scalar with incompatible types
- Missing conversion between numeric precisions
- Complex number mixed with non-numeric type

## How to Fix

```julia
# WRONG: Incompatible types
x = 5
y = "10"
z = x + y  # TypeError: non-numeric argument

# CORRECT: Convert types explicitly
x = 5
y = "10"
z = x + parse(Int, y)  # 15
```

```julia
# WRONG: Custom type missing promotion
struct MyNumber
    value::Float64
end
MyNumber(1.0) + 2  # MethodError

# CORRECT: Implement Number interface
struct MyNumber <: Number
    value::Float64
end
Base.:(+)(a::MyNumber, b::Number) = MyNumber(a.value + b)
Base.:(+)(a::Number, b::MyNumber) = MyNumber(a + b.value)
```

## Examples

```julia
# Example 1: Numeric type promotion
x = Int32(5)
y = Float64(3.14)
z = x + y  # promotes to Float64: 8.14

# Example 2: Matrix type promotion
A = ones(Int, 2, 2)
b = Float64[1.5, 2.5]
result = A .+ b  # promotes to Float64

# Example 3: Safe mixed arithmetic
function safe_add(a::Number, b::Number)
    promote(a, b) .+ (a, b) |> first
end
```

## Related Errors

- [TypeError](julia-type-error) -- type assertion failures
- [MethodError](julia-method-error) -- method not found
