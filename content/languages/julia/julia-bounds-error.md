---
title: "[Solution] Fix BoundsError array index out of bounds in Julia"
description: "Fix BoundsError in Julia by using safe indexing with get and eachindex, checking array lengths before access, and understanding Julia 1-based indexing."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 8
---

## What This Error Means

A `BoundsError` is thrown when you try to access an element of an array, string, or other indexable collection at an index outside its valid range. Julia uses 1-based indexing by default.

The error appears as:

```julia
BoundsError: attempt to access 3-element Vector{Int64} at index [5]
```

or for matrices:

```julia
BoundsError: attempt to access 2x3 Matrix{Float64} at index [3, 2]
```

## Why It Happens

This error occurs when accessing indices outside valid bounds:

- Using 0-based indexing (common for C/Python programmers)
- Off-by-one errors in loop bounds
- Accessing an empty collection at any index
- Computed index exceeds collection length
- Accessing multi-dimensional arrays with wrong number of indices

## How to Fix It

Use valid 1-based indices:

```julia
arr = [10, 20, 30]
x = arr[1]   # 10 (first element)
y = arr[end] # 30 (last element)
```

Use `eachindex` for safe iteration:

```julia
arr = [1, 2, 3, 4, 5]
for i in eachindex(arr)
    println(arr[i])
end
```

Use `getindex` with default values:

```julia
arr = [10, 20, 30]

# WRONG: Crashes if index is out of bounds
value = arr[5]

# CORRECT: Use get with a default
value = get(arr, 5, nothing)  # Returns nothing
```

Check bounds before accessing:

```julia
arr = [1, 2, 3]
idx = 5

if 1 <= idx <= length(arr)
    println(arr[idx])
else
    println("Index $idx out of bounds for array of length $(length(arr))")
end
```

Use `@boundscheck` for debug-mode bounds checking:

```julia
function safe_get(arr, idx)
    @boundscheck checkbounds(arr, idx)
    @inbounds arr[idx]
end
```

## Common Mistakes

- Forgetting Julia uses 1-based indexing, not 0-based
- Using `length(arr)` as the last valid index (it should be `length(arr)`)
- Not accounting for empty arrays before accessing index 1
- Mixing up row and column indices for matrices
- Using `pop!` or `shift!` on empty arrays without checking first

## Related Pages

- [MethodError: no method matching](/languages/julia/julia-method-error)
- [DimensionMismatch: dimensions do not match](/languages/julia/julia-dimension-mismatch)
- [UndefVarError: function not defined](/languages/julia/julia-undefined-function)
