---
title: "[Solution] Julia ErrorException — Unhandled Exception in Try/Catch"
description: "Fix Julia ErrorException in try/catch blocks. Learn about exception types, rethrow, and proper error handling patterns in Julia."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An `ErrorException` is Julia's general-purpose exception type. It is thrown when an error occurs that does not have a more specific exception type. The error message provides details about what went wrong. `ErrorException` is the supertype of many specific exception types.

## Why It Happens

The most common cause is calling `error("message")` explicitly. This is the standard way to throw an `ErrorException` with a custom message in Julia.

Another frequent cause is assertion failures from `@assert` macro. When an assertion condition is false, the macro throws an `ErrorException` with the assertion text.

Accessing undefined variables or global scope issues can also produce `ErrorException`. If a variable is referenced before it is assigned in the current scope, Julia throws this error.

Package loading failures often manifest as `ErrorException` when a package cannot be found or has incompatible dependencies.

Finally, method errors that do not match any specific exception type fall back to `ErrorException`.

## How To Fix It

### Use specific exception types when possible

```julia
# Wrong — generic error
function divide(a, b)
    b == 0 && error("Cannot divide by zero")
    a / b
end

# Correct — use specific exception
function divide(a, b)
    b == 0 && throw(ArgumentError("Cannot divide by zero"))
    a / b
end
```

### Catch specific exceptions in try-catch

```julia
try
    risky_operation()
catch e
    if e isa ArgumentError
        println("Bad argument: $(e.msg)")
    elseif e isa BoundsError
        println("Index out of bounds")
    else
        rethrow()
    end
end
```

### Use @assert for development checks only

```julia
function process(data)
    @assert !isempty(data) "Data must not be empty"
    # Process data
end
```

### Use custom exception types for libraries

```julia
struct ValidationError <: Exception
    field::String
    reason::String
end

Base.showerror(io::IO, e::ValidationError) =
    print(io, "Validation error in $(e.field): $(e.reason)")

function validate(name)
    isempty(name) && throw(ValidationError("name", "cannot be empty"))
end
```

### Use @assert with custom messages

```julia
@assert x >= 0 "x must be non-negative, got $x"
```

## Common Mistakes

- Using `error()` for all exceptions instead of specific types
- Catching `ErrorException` too broadly and hiding the root cause
- Using `@assert` for production validation (assertions can be disabled)
- Not providing descriptive error messages
- Using `rethrow()` incorrectly, losing the original stack trace

## Related Pages

- [Julia ArgumentError](/languages/julia/julia-argumenterror/)
- [Julia TypeError](/languages/julia/julia-typeerror/)
- [Julia BoundsError](/languages/julia/julia-boundserror/)
