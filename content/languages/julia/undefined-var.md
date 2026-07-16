---
title: "UndefVarError: X not defined"
description: "An UndefVarError occurs when referencing a variable that has not been defined in the current scope."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["variable", "undefined", "scope", "undefvarerror"]
weight: 5
---

## What This Error Means

An `UndefVarError` is thrown when you try to use a variable name that hasn't been defined in the current scope. This can happen due to typos, using a variable before it's assigned, or referencing a variable from a different scope.

## Common Causes

- Typo in variable name
- Using a variable before it's defined
- Variable defined in a different scope (e.g., inside a function)
- Missing module or package import

## How to Fix

```julia
# WRONG: Typo in variable name
myVariable = 10
println(myvariable)  # UndefVarError: myvariable not defined

# CORRECT: Match the exact variable name
myVariable = 10
println(myVariable)  # 10
```

```julia
# WRONG: Variable defined in inner scope
function greet()
    message = "hello"
end
println(message)  # UndefVarError: message not defined

# CORRECT: Return the value or define in outer scope
function greet()
    message = "hello"
    return message
end
msg = greet()
println(msg)  # "hello"
```

## Examples

```julia
# Example 1: Typo
total = 100
println(toal)  # UndefVarError: toal not defined

# Example 2: Undefined in scope
for i in 1:5
    x = i
end
println(x)  # UndefVarError: x not defined

# Example 3: Missing import
println(MyModule.my_function)  # UndefVarError: MyModule not defined
```

## Related Errors

- [BoundsError: attempt to access X at index [Y]](/languages/julia/bounds-error)
- [MethodError: no method matching X](/languages/julia/type-error)
