---
title: "Julia MethodAmbiguity Dispatch Error"
description: "Fix Julia MethodAmbiguity errors when multiple method definitions are equally applicable to given argument types."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

`MethodAmbiguity` occurs when Julia's multiple dispatch cannot determine which method is most specific for the given argument types. Two or more methods are equally applicable.

## Common Causes

- Overlapping method signatures without specificity
- Abstract type hierarchies creating ambiguous dispatch
- Mixing concrete and abstract type arguments
- Methods defined on Union types that overlap
- Forwarding methods that create ambiguity with originals

## How to Fix

```julia
# WRONG: Ambiguous methods
f(x::Int, y::Any) = "int, any"
f(x::Any, y::Int) = "any, int"
f(1, 2)  # MethodAmbiguity: both match

# CORRECT: Add specific method
f(x::Int, y::Any) = "int, any"
f(x::Any, y::Int) = "any, int"
f(x::Int, y::Int) = "int, int"  # resolves ambiguity
```

```julia
# WRONG: Overlapping abstract types
g(x::Real) = "real"
g(x::Integer) = "integer"
g(1)  # Integer <: Real, ambiguous

# CORRECT: Make Integer method more specific
g(x::Real) = "real"
g(x::Integer) = "integer"  # this is fine, Integer is more specific
g(1)  # "integer"
```

## Examples

```julia
# Example 1: Resolving ambiguity
h(x::AbstractFloat, y::AbstractFloat) = "float, float"
h(x::Float64, y::Float64) = "Float64, Float64"
h(1.0, 2.0)  # "Float64, Float64"

# Example 2: Union type ambiguity
k(x::Union{Int,String}) = "int or str"
k(x::Int) = "int"
k(42)  # "int" -- specific wins

# Example 3: Type hierarchy dispatch
abstract type Shape end
struct Circle <: Shape end
struct Square <: Shape end

area(c::Circle) = π * r^2
area(s::Square) = s.side^2
area(x::Shape) = error("unknown shape")
```

## Related Errors

- [MethodError](julia-method-error) -- method not found
- [TypeError](julia-type-error) -- type mismatch
