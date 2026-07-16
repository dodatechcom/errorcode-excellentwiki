---
title: "BoundsError: attempt to access X at index [Y]"
description: "A BoundsError occurs when attempting to access an array, string, or other indexable collection at an index that is outside its valid range."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["bounds", "index", "array", "boundserror"]
weight: 5
---

## What This Error Means

A `BoundsError` is thrown when you try to access an element of a collection (array, string, tuple, etc.) using an index that doesn't exist. Julia uses 1-based indexing by default, and indices must fall within the declared range of the collection.

## Common Causes

- Using 0-based indexing (common for programmers coming from C/Python)
- Off-by-one errors in loop bounds
- Accessing an empty collection
- Using a computed index that goes out of range

## How to Fix

```julia
# WRONG: Accessing index 0 (Julia is 1-indexed)
arr = [10, 20, 30]
x = arr[0]          # BoundsError: attempt to access 3-element Vector{Int64} at index [0]

# CORRECT: Use valid 1-based index
arr = [10, 20, 30]
x = arr[1]          # 10
```

```julia
# WRONG: Loop one past the end
arr = [1, 2, 3, 4, 5]
for i in 1:length(arr)+1
    println(arr[i])  # BoundsError on last iteration
end

# CORRECT: Use proper range
arr = [1, 2, 3, 4, 5]
for i in eachindex(arr)
    println(arr[i])  # safe iteration
end
```

## Examples

```julia
# Example 1: Out of bounds on a matrix
matrix = zeros(3, 3)
value = matrix[4, 1]    # BoundsError: attempt to access 3×3 Matrix{Float64} at index [4, 1]

# Example 2: Empty array access
empty_arr = Int[]
x = empty_arr[1]         # BoundsError: attempt to access 0-element Vector{Int64} at index [1]

# Example 3: String indexing
str = "hello"
ch = str[10]             # BoundsError: attempt to access String at index [10]
```

## Related Errors

- [UndefVarError: X not defined](/languages/julia/undefined-sym)
