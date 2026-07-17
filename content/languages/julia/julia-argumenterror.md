---
title: "ArgumentError in Julia"
description: "Julia raises ArgumentError when a function receives an invalid or unexpected argument value"
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["argument", "validation", "argumenterror", "runtime"]
weight: 5
---

## What This Error Means

An `ArgumentError` is thrown when a function receives an argument that is valid in type but invalid in value. This is a common Julia error used to enforce preconditions.

## Common Causes

- Invalid argument value passed to function
- Missing required keyword argument
- Argument out of expected range
- Wrong argument type for function

## How to Fix

Validate arguments with `throw`:

```julia
function set_percentage(value::Float64)
    if !(0.0 <= value <= 1.0)
        throw(ArgumentError("Percentage must be between 0 and 1, got $value"))
    end
    value
end
```

Use `@assert` for development checks:

```julia
function divide(a::Int, b::Int)
    @assert b != 0 "Cannot divide by zero"
    a / b
end
```

Check keyword arguments:

```julia
function connect(; host::String, port::Int=8080)
    if isempty(host)
        throw(ArgumentError("host cannot be empty"))
    end
    println("Connecting to $host:$port")
end
```

Use default values with validation:

```julia
function clamp_value(x; min_val=0, max_val=100)
    if min_val > max_val
        throw(ArgumentError("min_val must be <= max_val"))
    end
    clamp(x, min_val, max_val)
end
```

## Examples

```julia
function factorial(n::Int)
    n < 0 && throw(ArgumentError("n must be non-negative"))
    n <= 1 ? 1 : n * factorial(n - 1)
end

factorial(-1) # ArgumentError: n must be non-negative
```

## Related Errors

- [BoundsError]({{< relref "/languages/julia/bounds-error" >}})
- [TypeError]({{< relref "/languages/julia/type-error" >}})
