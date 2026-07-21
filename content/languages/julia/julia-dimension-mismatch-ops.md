---
title: "Julia DimensionMismatch Error in Array Operations"
description: "Fix Julia DimensionMismatch errors when performing array operations with incompatible dimensions."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

`DimensionMismatch` is thrown when an operation requires arrays to have compatible shapes but they do not. This commonly occurs in arithmetic, concatenation, and broadcasting.

## Common Causes

- Adding arrays with different sizes
- Matrix multiplication with incompatible dimensions
- Broadcasting with non-compatible shapes
- Concatenating arrays along wrong dimension
- Assigning values from differently shaped arrays

## How to Fix

```julia
# WRONG: Different sized arrays
a = [1, 2, 3]
b = [1, 2]
c = a + b  # DimensionMismatch

# CORRECT: Ensure compatible sizes
a = [1, 2, 3]
b = [1, 2, 3]
c = a + b  # [2, 4, 6]
```

```julia
# WRONG: Matrix multiplication dimension error
A = ones(3, 4)
B = ones(3, 4)
C = A * B  # DimensionMismatch: 3x4 * 3x4

# CORRECT: Inner dimensions must match
A = ones(3, 4)
B = ones(4, 2)
C = A * B  # 3x2 matrix
```

## Examples

```julia
# Example 1: Array addition
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
c = a + b  # [5.0, 7.0, 9.0]

# Example 2: Broadcasting
a = [1, 2, 3]
b = [10, 20, 30]
c = a .+ b  # [11, 22, 33]

# Example 3: Matrix dimensions
A = rand(3, 3)
b = rand(3)
x = A \ b  # solves Ax = b
```

## Related Errors

- [BoundsError](bounds-error) -- index out of bounds
- [MethodError](julia-method-error) -- method signature mismatch
