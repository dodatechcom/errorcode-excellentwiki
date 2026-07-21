---
title: "[Solution] F# Let Mutable Default Error -- Uninitialized Mutable Binding"
description: "Fix F# let mutable errors when mutable bindings are used without proper initialization."
languages: ["fsharp"]
error-types: ["runtime"]
severities: ["error"]
---

# F# Let Mutable Default Error

This error occurs when a mutable binding is used before being assigned a meaningful value, leading to use of uninitialized state.

## Common Causes

- Declaring a mutable binding without an initial value
- Using a mutable variable before the first assignment in all code paths
- Assigning None or default values that mask real errors
- Using mutable bindings across parallel async workflows

## How to Fix

### Always provide initial values

```fsharp
// WRONG: mutable with no initial value in some code paths
let mutable result
if condition then
    result <- 42
printfn "%d" result  // warning: may be uninitialized

// CORRECT: initialize with a default
let mutable result = 0
if condition then
    result <- 42
printfn "%d" result
```

### Use option for explicit tracking

```fsharp
let mutable result: int option = None

if condition then
    result <- Some 42

match result with
| Some value -> printfn "Got %d" value
| None -> printfn "No result"
```

## Examples

```fsharp
let findFirst items predicate =
    let mutable found = None
    for item in items do
        if found.IsNone && predicate item then
            found <- Some item
    found

let result = findFirst [1..10] (fun x -> x > 5)
```
