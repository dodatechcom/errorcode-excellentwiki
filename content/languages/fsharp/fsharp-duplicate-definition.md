---
title: "[Solution] F# Duplicate Definition Error -- Fixing Redeclaration Conflicts"
description: "Fix F# duplicate definition errors when the same name is defined more than once in the same scope."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Duplicate Definition Error

This error occurs when you attempt to define the same identifier twice within the same scope. F# does not allow shadowing at the same scope level.

## Common Causes

- Defining the same let binding twice in a module
- Reusing parameter names in nested functions
- Duplicate open statements for the same namespace
- Defining overlapping type aliases

## How to Fix

### Rename the duplicate binding

```fsharp
// WRONG: duplicate definition
let value = 10
let value = 20

// CORRECT: use distinct names
let firstValue = 10
let secondValue = 20
```

### Use different parameter names

```fsharp
// WRONG: same parameter name in nested scope
let calculate x =
    let inner x = x * 2  // shadows outer x
    inner x

// CORRECT: use a distinct name
let calculate x =
    let inner v = v * 2
    inner x
```

## Examples

```fsharp
module App =

    type Config = { Name: string; Timeout: int }
    type Settings = { Name: string; Timeout: int }  // OK -- different type name

    let run (cfg: Config) =
        let name = cfg.Name  // distinct from module member
        printfn "Running %s" name
```
