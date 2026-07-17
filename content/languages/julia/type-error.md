---
title: "MethodError: no method matching X"
description: "A MethodError occurs when calling a function with argument types that don't match any defined method signature."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `MethodError` is thrown when you call a function with arguments whose types don't match any of its defined method signatures. Julia uses multiple dispatch, and the error message shows the closest matching method to help you identify the mismatch.

## Common Causes

- Passing wrong types to a function (e.g., string to arithmetic)
- Calling a method that doesn't exist for the given argument types
- Missing package imports for extended methods
- Typos in function names

## How to Fix

```julia
# WRONG: Passing string to arithmetic
result = 1 + "hello"   # MethodError: no method matching +(::Int64, ::String)

# CORRECT: Use matching types
result = 1 + 2          # 3
result = "hello" * " " * "world"
```

```julia
# WRONG: Calling method with wrong argument count
split("hello world")    # works, but:
split("hello", " ", "x")  # MethodError: no method matching split(::String, ::String, ::String)

# CORRECT: Check method signature
methods(split)
split("hello world", " ")  # ["hello", "world"]
```

## Examples

```julia
# Example 1: Wrong type to length
len = length(42)        # MethodError: no method matching length(::Int64)

# Example 2: Missing method for custom type
struct Point
    x::Float64
    y::Float64
end
p = Point(1.0, 2.0)
p + 1                   # MethodError: no method matching +(::Point, ::Int64)

# Example 3: Wrong argument types
push!(1, 2)             # MethodError: no method matching push!(::Int64, ::Int64)
```

## Related Errors

- [BoundsError: attempt to access X at index [Y]](/languages/julia/bounds-error)
- [UndefVarError: variable not defined](/languages/julia/undefined-sym)
