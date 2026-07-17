---
title: "TypeError in Julia"
description: "Julia raises TypeError when a value is of an unexpected type in a type assertion or constructor"
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `TypeError` is thrown when a value does not match the expected type in a type assertion, constructor call, or type-constrained function parameter.

## Common Causes

- Passing wrong type to type-annotated function
- Failed type assertion (`::Type`)
- Constructor called with wrong argument types
- Incompatible type in generic function

## How to Fix

Use type assertions carefully:

```julia
function process(x::Int)
    x * 2
end

process("hello") # TypeError: in process, in Int, expected Int, got a value of type String
```

Check type before using assertion:

```julia
function safe_process(x)
    if x isa Int
        x * 2
    else
        throw(ArgumentError("Expected Int, got $(typeof(x))"))
    end
end
```

Use `convert` for type conversion:

```julia
x = convert(Int, 3.14)  # InexactError (not TypeError)
x = convert(Int, "3")   # MethodError
```

Use parametric types:

```julia
function process_generic(x::T) where T
    println("Processing $T value: $x")
end
```

## Examples

```julia
const MyType = Int
function foo(x::MyType)
    x
end

foo("hello") # TypeError: in foo, in MyType, expected MyType, got a value of type String
```

## Related Errors

- [BoundsError]({{< relref "/languages/julia/bounds-error" >}})
- [InexactError]({{< relref "/languages/julia/inexact-error" >}})
