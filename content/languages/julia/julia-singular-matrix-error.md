---
title: "Julia LinearAlgebra SingularMatrix Error"
description: "Fix Julia LinearAlgebra singular matrix errors when attempting operations on non-invertible matrices."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `SingularException` occurs in Julia's LinearAlgebra module when you try to invert, factorize, or solve a system with a singular (non-invertible) matrix. The matrix has determinant zero.

## Common Causes

- Matrix rows or columns are linearly dependent
- Matrix contains all zeros in a row or column
- Near-singular matrix with very small determinant
- Using lu! or similar on ill-conditioned matrix
- Copying singular matrix without checking

## How to Fix

```julia
# WRONG: Inverting singular matrix
using LinearAlgebra
A = [1.0 2.0; 2.0 4.0]  # second row is 2x first
inv(A)  # SingularException

# CORRECT: Check singularity first
A = [1.0 2.0; 2.0 4.0]
det(A)  # 0.0 -- singular!
# Use pseudoinverse instead
pinv(A)
```

```julia
# WRONG: Solving singular system
A = [1.0 1.0; 1.0 1.0]
b = [1.0, 2.0]
A \ b  # SingularException

# CORRECT: Use least-squares solution
A = [1.0 1.0; 1.0 1.0]
b = [1.0, 2.0]
A \ b  # gives least-squares solution
# or use QR factorization
qr(A) \ b
```

## Examples

```julia
# Example 1: Check if matrix is singular
A = [1.0 2.0; 3.0 4.0]
println(det(A))  # -2.0 -- not singular
 println(isapprox(det(A), 0))  # false

# Example 2: Pseudoinverse for singular matrix
A = [1.0 2.0; 2.0 4.0]
A_pinv = pinv(A)
println(A_pinv * A)  # approximate identity on range

# Example 3: Regularization for near-singular
A = [1.0 1.0; 1.0 1.0001]
λ = 1e-6
A_reg = A + λ * I
x = A_reg \ b  # regularized solution
```

## Related Errors

- [Singular matrix error](julia-singular-matrix) -- matrix singularity
- [SVD convergence error](julia-svd-convergence-error) -- SVD failures
