---
title: "[Solution] Julia UndefVarError Variable Not Defined Fix"
description: "Fix Julia UndefVarError when accessing a variable that has not been defined."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1151
---

## What This Error Means

An UndefVarError occurs when you try to access a variable or function name that hasn't been defined in the current scope.

## Common Causes

- Variable not yet assigned
- Typo in variable name
- Variable defined in different scope
- Module not loaded or imported

## How to Fix

```julia
println(x)  # UndefVarError: x not defined

x = 42
println(x)  # 42
```

```julia
module MyMod
    x = 10
end
println(MyMod.x)  # 10
println(x)        # UndefVarError

using .MyMod
println(x)  # 10
```

```julia
if false
    y = 100
end
println(y)  # UndefVarError (never executed)

y = if true
    100
else
    0
end
println(y)  # 100
```

## Related Errors

- [Julia UndefVarError](undefined-var) - undefined variable
- [Julia TypeError](julia-type-error) - type error
- [Julia UndefKeywordError](julia-undefined-function) - keyword error
