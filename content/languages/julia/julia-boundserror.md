---
title: "BoundsError: Array Index Out of Bounds in Julia"
description: "Julia raises BoundsError when accessing an array or string at an index outside its valid range"
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `BoundsError` is thrown when you try to access an element of a collection using an index that doesn't exist. Julia uses 1-based indexing by default.

## Common Causes

- Using 0-based indexing (common for C/Python programmers)
- Off-by-one errors in loop bounds
- Accessing an empty collection
- Computed index exceeds collection length

## How to Fix

Use valid 1-based indices:

```julia
arr = [10, 20, 30]
x = arr[1]  # 10 (first element)
```

Use `eachindex` for safe iteration:

```julia
arr = [1, 2, 3, 4, 5]
for i in eachindex(arr)
    println(arr[i])
end
```

Use `getindex` with default:

```julia
arr = [10, 20, 30]
value = get(arr, 5, nothing)  # Returns nothing instead of BoundsError
```

Check before accessing:

```julia
arr = [1, 2, 3]
idx = 5
if 1 <= idx <= length(arr)
    println(arr[idx])
else
    println("Index out of bounds")
end
```

## Examples

```julia
matrix = zeros(3, 3)
value = matrix[4, 1]    # BoundsError: attempt to access 3×3 Matrix at index [4, 1]

empty_arr = Int[]
x = empty_arr[1]         # BoundsError: attempt to access 0-element Vector at index [1]
```

## Related Errors

- [ArgumentError]({{< relref "/languages/julia/argumenterror" >}})
- [UndefVarError]({{< relref "/languages/julia/undefinedvar" >}})
