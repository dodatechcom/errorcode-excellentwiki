---
title: "ArgumentError: invalid import"
description: "An ArgumentError occurs when attempting to import a name that doesn't exist in the specified module or package."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `ArgumentError` with an invalid import message is thrown when you try to import a symbol (function, type, or constant) from a module that doesn't export or define that name. This commonly happens with typos in imported names or incorrect package usage.

## Common Causes

- Typo in the name being imported
- Importing from wrong module or package
- Name is not exported from the target module
- Package not loaded before importing specific names

## How to Fix

```julia
# WRONG: Importing non-existent name
using LinearAlgebra: normx   # ArgumentError: invalid import

# CORRECT: Use correct name
using LinearAlgebra: norm     # works
```

```julia
# WRONG: Importing from wrong module
import Statistics: sqrt       # ArgumentError: sqrt not in Statistics

# CORRECT: Import from correct module
import Base: sqrt             # works
# or
using LinearAlgebra           # for sqrt of matrices
```

## Examples

```julia
# Example 1: Typo in name
using CSV: read_fiel         # ArgumentError: invalid import

# Example 2: Wrong module
import Pkg: sqrt             # ArgumentError: invalid import

# Example 3: Private name
import MyModule: _private_func  # ArgumentError: not exported
```

## Related Errors

- [UndefVarError: X not defined](/languages/julia/undefined-sym)
- [MethodError: no method matching X](/languages/julia/type-error)
