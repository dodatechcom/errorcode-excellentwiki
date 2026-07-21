---
title: "Julia SharedArray Dimension Error"
description: "Fix Julia SharedArray dimension errors when creating or accessing SharedArrays with incorrect shapes across processes."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

SharedArray dimension errors occur when the array shape specified during creation does not match the intended usage, or when processes access SharedArray indices outside valid bounds.

## Common Causes

- SharedArray created with wrong dimensions
- Worker process accesses indices not allocated
- Dimension mismatch between SharedArray and computation
- Forgetting that SharedArray is 1-indexed like all Julia arrays
- Race conditions when multiple workers write same index

## How to Fix

```julia
# WRONG: Wrong dimensions for SharedArray
using SharedArrays
sa = SharedArray{Float64}(100)  # 1D array
sa[1, 1]  # BoundsError: BoundsError

# CORRECT: Use correct dimensions
sa = SharedArray{Float64}(100, 100)  # 2D array
sa[1, 1]  # works
```

```julia
# WRONG: Dimension mismatch in distributed computation
sa = SharedArray{Float64}(10, 10)
workers_data = [sa[i, :] for i in 1:10]
# Each worker gets 10-element vector

# CORRECT: Ensure dimensions match operation
sa = SharedArray{Float64}(10, 10)
for i in 1:10
    row = sa[i, :]  # 10-element slice
    # process row
end
```

## Examples

```julia
# Example 1: Create and use SharedArray
using SharedArrays, Distributed
addprocs(2)

sa = SharedArray{Int}(100, 100)
sa[:] = 1:10000  # fill with sequential values
@distributed for i in 1:100
    sa[i, :] .*= 2
end

# Example 2: SharedArray with specific init
sa = SharedArray{Float64}(50, 50; init=0.0)
@distributed for i in 1:50
    sa[i, i] = 1.0  # set diagonal
end

# Example 3: Check dimensions
size(sa)    # (50, 50)
ndims(sa)   # 2
length(sa)  # 2500
```

## Related Errors

- [BoundsError](bounds-error) -- index out of bounds
- [Shared array error](julia-shared-array-error) -- SharedArray issues
