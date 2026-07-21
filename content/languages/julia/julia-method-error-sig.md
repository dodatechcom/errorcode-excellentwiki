---
title: "Julia MethodError No Method Matching Error"
description: "Fix Julia MethodError when calling a function with argument types that do not match any defined method."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `MethodError` occurs when Julia cannot find a method matching the given function name and argument types. This is common with type mismatches or when the correct package is not loaded.

## Common Causes

- Argument types do not match any defined method signature
- Function not imported from the correct module or package
- Package not loaded (missing `using` or `import`)
- Method defined for different types than provided
- Multiple dispatch ambiguity prevents unique method selection

## How to Fix

```julia
# WRONG: Wrong argument type
f(x::Int) = x * 2
f("hello")  # MethodError: no method matching f(::String)

# CORRECT: Add method for String or convert input
f(x::Int) = x * 2
f(x::String) = parse(Int, x) * 2
f("hello")  # works: parses "hello" -- will error, but method exists
```

```julia
# WRONG: Package not loaded
csv("data.csv")  # UndefVarError: csv not defined

# CORRECT: Load the package first
using CSV
csv("data.csv")  # now works
```

## Examples

```julia
# Example 1: Multiple dispatch
area(r::Number) = π * r^2
area(l::Number, w::Number) = l * w

area(5)         # 78.539...
area(4, 6)      # 24

# Example 2: Type conversion
function process(x::Int)
    println("Integer: $x")
end
process(parse(Int, "42"))  # works

# Example 3: Import specific function
using Statistics: mean, std
mean([1, 2, 3, 4, 5])  # 3.0
```

## Related Errors

- [UndefVarError](undefined-sym) -- undefined variable or function
- [TypeError](type-error) -- type assertion failures
