---
title: "Julia BoundsError Slicing Dimension Error"
description: "Fix Julia BoundsError when slicing arrays with indices outside valid ranges for specific dimensions."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

`BoundsError` on slicing occurs when you try to access or slice an array with indices that exceed the array's bounds in any dimension.

## Common Causes

- Slicing beyond array length
- Using wrong dimension index for multi-dimensional arrays
- Off-by-one error in loop ranges
- Accessing empty array slices
- Using 0-based indexing where 1-based is expected

## How to Fix

```julia
# WRONG: Slice beyond array
arr = [1, 2, 3]
arr[1:5]  # BoundsError

# CORRECT: Clamp to valid range
arr[1:min(5, end)]  # [1, 2, 3]
```

```julia
# WRONG: Wrong dimension
mat = ones(3, 4)
mat[5, 1]  # BoundsError

# CORRECT: Check dimensions
mat = ones(3, 4)
size(mat)  # (3, 4)
mat[3, 4]  # works: last valid index
```

## Examples

```julia
# Example 1: Safe slicing
function safe_slice(arr, range)
    valid = range[1]:min(range[end], length(arr))
    return arr[valid]
end
safe_slice([1,2,3], 1:10)  # [1, 2, 3]

# Example 2: Matrix slicing
A = rand(5, 5)
A[1:3, 2:4]  # 3x3 submatrix
A[:, 1]      # first column vector

# Example 3: Range with step
arr = collect(1:10)
arr[1:2:end]  # [1, 3, 5, 7, 9]
```

## Related Errors

- [BoundsError](bounds-error) -- general index errors
- [DimensionMismatch](julia-dimension-mismatch) -- shape incompatibility
