---
title: "[Solution] F# Mutable Closure Error -- Captured Variable Issues"
description: "Fix F# mutable closure errors when mutable variables captured in closures behave unexpectedly."
languages: ["fsharp"]
error-types: ["runtime"]
severities: ["error"]
---

# F# Mutable Closure Error

This error occurs when mutable variables captured in closures do not reflect expected values due to capture-by-reference semantics.

## Common Causes

- Loop variables captured by reference change after closure creation
- Async workflows capturing mutable state from enclosing scope
- Event handlers sharing mutable bindings unexpectedly
- Multiple closures sharing the same mutable variable

## How to Fix

### Create local copies in loops

```fsharp
// WRONG: captures loop variable by reference
let handlers =
    [for i in 0..2 ->
        fun () -> printfn "%d" i]
// All handlers print 3

// CORRECT: capture a local copy
let handlers =
    [for i in 0..2 ->
        let captured = i
        fun () -> printfn "%d" captured]
```

### Use immutable state with fold

```fsharp
// Instead of mutable accumulator
let sum items =
    let mutable total = 0
    for item in items do
        total <- total + item
    total

// Prefer functional fold
let sum items = List.fold (+) 0 items
```

## Examples

```fsharp
let createCounters () =
    let counters =
        [1..3] |> List.map (fun n ->
            let mutable count = n
            fun () ->
                count <- count + 1
                count)
    counters
```
