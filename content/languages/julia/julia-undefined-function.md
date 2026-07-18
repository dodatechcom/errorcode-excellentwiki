---
title: "[Solution] Fix UndefVarError function not defined in Julia"
description: "Resolve UndefVarError in Julia by checking module imports with using and import, understanding variable scope rules, and defining functions before use."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 8
---

## What This Error Means

A `UndefVarError` is thrown when Julia encounters a variable or function name that has not been defined in the current scope. This is one of the most common errors in Julia and indicates the runtime cannot find a binding for the given name.

The error appears as:

```julia
UndefVarError: foo not defined
```

or with module context:

```julia
UndefVarError: MyModule.bar not defined
```

## Why It Happens

This error occurs when a name is referenced before it exists:

- Calling a function that has not been defined yet
- Using a variable outside its scope (e.g., inside a function or block)
- Missing `using` or `import` statement for a module function
- Typo in the function or variable name
- Referencing a variable defined in a different module without qualifying it
- Accessing a variable before it is assigned in a conditional block

## How to Fix It

Define functions before using them:

```julia
# WRONG: Calling greet before it is defined
result = greet("Alice")

function greet(name)
    return "Hello, $name"
end

# CORRECT: Define first, then call
function greet(name)
    return "Hello, $name"
end

result = greet("Alice")
```

Import the module or function you need:

```julia
# WRONG: Using sqrt without importing LinearAlgebra
x = sqrt([1.0 2.0; 3.0 4.0])

# CORRECT: Import the module first
using LinearAlgebra
x = sqrt([1.0 2.0; 3.0 4.0])
```

Check variable scope carefully:

```julia
# WRONG: x is not defined outside the block
for i in 1:10
    x = i * 2
end
println(x)  # UndefVarError

# CORRECT: Declare before the loop
x = 0
for i in 1:10
    x = i * 2
end
println(x)  # 20
```

Use `@isdefined` to check for variable existence:

```julia
if @isdefined(my_var)
    println(my_var)
else
    println("my_var is not defined")
end
```

## Common Mistakes

- Forgetting that Julia modules must be explicitly imported with `using` or `import`
- Assuming global variables are accessible inside functions without passing them
- Misspelling module or function names (Julia error messages are helpful here)
- Using a variable defined in a `let` block outside that block
- Not understanding that `include()` defines names in the caller's scope, not a new module

## Related Pages

- [MethodError: no method matching](/languages/julia/julia-method-error)
- [BoundsError: array index out of bounds](/languages/julia/bounds-error)
- [Syntax error in Julia](/languages/julia/julia-compile-error)
