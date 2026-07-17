---
title: "DimensionMismatch in Julia"
description: "Julia raises DimensionMismatch when array dimensions do not match for an operation"
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `DimensionMismatch` is thrown when an operation requires arrays to have compatible dimensions but they don't match. This commonly occurs with matrix multiplication, broadcasting, and element-wise operations.

## Common Causes

- Matrix multiplication with incompatible dimensions
- Broadcasting arrays with incompatible shapes
- Array assignment with mismatched dimensions
- Linear algebra operations on wrong-sized matrices

## How to Fix

Check array dimensions before operations:

```julia
A = zeros(3, 4)
B = zeros(4, 5)
C = A * B  # Works: (3×4) * (4×5) = (3×5)

D = zeros(3, 3)
E = zeros(4, 4)
F = D * E  # DimensionMismatch
```

Use broadcasting with compatible shapes:

```julia
a = [1, 2, 3]
b = [1, 2, 3]
c = a .+ b  # Works: element-wise addition

d = [1 2; 3 4]  # 2×2 matrix
e = [1, 2, 3]   # 3-element vector
f = d .+ e      # DimensionMismatch
```

Reshape arrays when needed:

```julia
a = [1, 2, 3, 4]
b = reshape(a, 2, 2)  # Convert to 2×2 matrix
c = reshape(a, 4, 1)  # Convert to column vector
```

Verify dimensions:

```julia
function safe_multiply(A, B)
    if size(A, 2) != size(B, 1)
        throw(DimensionMismatch("A columns ($(size(A,2))) != B rows ($(size(B,1)))"))
    end
    A * B
end
```

## Examples

```julia
A = [1 2; 3 4]  # 2×2
b = [1, 2, 3]    # 3-element vector
c = A * b        # DimensionMismatch: A has dimensions 2×2, b has dimensions 3
```

## Related Errors

- [BoundsError]({{< relref "/languages/julia/bounds-error" >}})
- [ArgumentError]({{< relref "/languages/julia/argumenterror" >}})
