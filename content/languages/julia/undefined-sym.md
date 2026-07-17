---
title: "UndefVarError: X not defined"
description: "An UndefVarError occurs when a variable or symbol is referenced before it has been assigned a value in the current scope."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `UndefVarError` is thrown when Julia encounters a variable name that has not been defined in the current scope. This can happen due to typos, referencing a variable before assignment, or scope issues with closures and comprehensions.

## Common Causes

- Typos in variable names
- Referencing a variable before it is assigned
- Scope issues when using closures or `for` loops
- Assuming a global variable is accessible inside a local scope

## How to Fix

```julia
# WRONG: Typo in variable name
result = calculat_total(10, 20)  # UndefVarError: calculat_total not defined

# CORRECT: Fix the typo
result = calculate_total(10, 20)
```

```julia
# WRONG: Variable not defined in scope
function process()
    println(x)          # UndefVarError: x not defined
end

# CORRECT: Define before use, or pass as parameter
function process(x)
    println(x)
end
```

## Examples

```julia
# Example 1: Variable before assignment
function example()
    println(myvar)       # UndefVarError: myvar not defined
    myvar = 42
end

# Example 2: Scope issue in loops
function find_max()
    for i in 1:10
        if i > 5
            best = i     # best is defined only in this branch
        end
    end
    return best          # UndefVarError: best not defined
end

# Example 3: Missing import
using LinearAlgebra
result = eigvals(my_matrix)  # UndefVarError: my_matrix not defined
```

## How to Debug

- Check for typos in variable names
- Verify variable is assigned before use
- Use `@which` to find where a function is defined
- Use `names()` to list variables in scope

## Related Errors

- [BoundsError: attempt to access X at index [Y]](/languages/julia/bounds-error)
