---
title: "[Solution] Fix SingularException matrix is singular in Julia"
description: "Resolve SingularException in Julia by checking matrix conditioning with cond, using pinv for pseudo-inverse, and applying Tikhonov regularization methods."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 7
---

## What This Error Means

A `SingularException` is thrown when you try to invert, factorize, or solve a system with a singular (non-invertible) matrix. A singular matrix has a determinant of zero and cannot be used in operations that require an inverse.

The error appears as:

```julia
SingularException(3)
```

indicating that the 3rd pivot during factorization is zero, meaning the matrix is singular.

## Why It Happens

This error occurs due to numerically singular matrices:

- Matrix has linearly dependent rows or columns
- Determinant is zero or extremely close to zero
- Matrix contains rows or columns of zeros
- Poorly conditioned matrix amplifies numerical errors
- Duplicate rows in the matrix causing rank deficiency

## How to Fix It

Check matrix rank before inversion:

```julia
A = [1.0 2.0; 2.0 4.0]

# Check if matrix is singular
println(det(A))   # 0.0 (singular)
println(rank(A))  # 1 (less than full rank)

# WRONG: Trying to invert a singular matrix
inv(A)  # SingularException

# CORRECT: Check rank first
if rank(A) == size(A, 1)
    inv(A)
else
    println("Matrix is singular, cannot invert")
end
```

Use `pinv` (pseudo-inverse) for singular matrices:

```julia
A = [1.0 2.0; 2.0 4.0]

# Use pseudo-inverse instead of inverse
A_pinv = pinv(A)
```

Add regularization for ill-conditioned matrices:

```julia
using LinearAlgebra

function regularized_inverse(A; lambda=1e-6)
    I_mat = I(size(A, 1))
    return inv(A' * A + lambda * I_mat) * A'
end

A = [1.0 2.0; 2.0 4.0]
x = regularized_inverse(A)  # No SingularException
```

Use `lu` factorization with pivoting for numerical stability:

```julia
using LinearAlgebra

A = [1.0 2.0; 2.0 4.0]
F = lu(A, Val(true))  # With pivoting
println(F)
# Even for singular matrices, LU with pivoting gives a useful decomposition
```

Check condition number:

```julia
A = [1.0 2.0; 2.0 4.0]
println(cond(A))  # Inf (singular)

# For nearly-singular matrices, high condition number warns of issues
B = [1.0 2.0; 2.0 4.001]
println(cond(B))  # Large but finite
```

## Common Mistakes

- Not checking `cond()` before inverting matrices in production code
- Assuming `det(A) != 0` is sufficient when numerical precision matters
- Using `inv(A) * b` instead of `A \ b` for solving linear systems
- Not accounting for floating-point precision when checking singularity
- Forgetting that sparse matrices can also be singular

## Related Pages

- [DimensionMismatch: dimensions do not match](/languages/julia/julia-dimension-mismatch)
- [BoundsError: array index out of bounds](/languages/julia/bounds-error)
- [MethodError: no method matching](/languages/julia/julia-method-error)
