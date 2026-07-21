---
title: "Julia UndefVarError Variable Not Defined"
description: "Fix Julia UndefVarError when referencing variables that have not been defined in the current scope."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

`UndefVarError` occurs when Julia encounters a variable name that has not been defined in the current scope. This includes typos, variables from other modules, and scope-related issues with global vs local variables.

## Common Causes

- Typo in variable name
- Variable defined in wrong scope (global vs local)
- Missing `using` or `import` for module variables
- Variable defined after the point of reference
- Circular dependency between modules

## How to Fix

```julia
# WRONG: Variable not defined
println(x)  # UndefVarError: x not defined

# CORRECT: Define before use
x = 42
println(x)
```

```julia
# WRONG: Scope confusion
for i in 1:10
    y = i * 2
end
println(y)  # UndefVarError: y not defined (local to loop)

# CORRECT: Define outside loop or use global
y = 0
for i in 1:10
    y = i * 2
end
println(y)  # 20
```

## Examples

```julia
# Example 1: Module variable access
module MyModule
    export myvar
    myvar = 10
end
using .MyModule
println(myvar)  # 10

# Example 2: Function scope
function test()
    local z = 100
    return z
end
println(test())  # 100
# println(z)  # would be UndefVarError

# Example 3: Global in loop
global_count = 0
for i in 1:5
    global global_count += 1
end
println(global_count)  # 5
```

## Related Errors

- [MethodError](julia-method-error) -- method not found
- [LoadError](julia-loading-error) -- file loading issues
