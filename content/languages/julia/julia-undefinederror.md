---
title: "UndefVarError in Julia"
description: "Julia raises UndefVarError when referencing an undefined variable or symbol"
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `UndefVarError` is thrown when you try to use a variable or symbol that has not been defined in the current scope. This is a common error when variables are misspelled or used before assignment.

## Common Causes

- Typo in variable name
- Variable used before assignment
- Variable defined in different scope (module, function)
- Missing import of module or package

## How to Fix

Check variable name spelling:

```julia
username = "Alice"
println(username)  # Correct
# println(usename)  # UndefVarError: usename not defined
```

Initialize variables before use:

```julia
# Wrong
println(x)  # UndefVarError: x not defined

# Correct
x = 10
println(x)
```

Import modules properly:

```julia
using LinearAlgebra

# Now can use dot, cross, etc.
v = [1.0, 2.0, 3.0]
norm(v)
```

Use `isdefined` check:

```julia
if @isdefined(myvar)
    println(myvar)
else
    println("Variable not defined")
end
```

## Examples

```julia
function greet()
    println(message)  # UndefVarError: message not defined
end
```

```julia
module MyModule
    export my_func
    my_func() = 42
end

using MyModule
my_func()  # Works
my_func   # UndefVarError if not exported
```

## Related Errors

- [BoundsError]({{< relref "/languages/julia/bounds-error" >}})
- [ArgumentError]({{< relref "/languages/julia/argumenterror" >}})
