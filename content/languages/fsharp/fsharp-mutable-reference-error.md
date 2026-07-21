---
title: "[Solution] F# Mutable Reference Error -- Ref Cell Issues"
description: "Fix F# mutable reference errors when using ref cells incorrectly or forgetting the .Value accessor."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Mutable Reference Error

This error occurs when ref cells are used incorrectly, such as accessing a ref cell without `.Value` or using the wrong assignment operator.

## Common Causes

- Forgetting `.Value` when reading or writing ref cells
- Using `<-` instead of `:=` for assignment
- Using ref cells where mutable bindings would be simpler
- Incorrectly capturing ref cells in closures

## How to Fix

### Use correct ref cell syntax

```fsharp
// WRONG: missing .Value
let count = ref 0
count <- 1  // assigns a new ref, not the value

// CORRECT: use := for assignment and .Value for reading
let count = ref 0
count := 1
printfn "%d" count.Value
```

### Prefer mutable for simple cases

```fsharp
// Ref cell (older style)
let count = ref 0
count := !count + 1

// Modern mutable (preferred)
let mutable count = 0
count <- count + 1
```

## Examples

```fsharp
let mutableCounter () =
    let count = ref 0
    fun () ->
        count := !count + 1
        !count

let counter = mutableCounter ()
printfn "%d" (counter ())  // 1
printfn "%d" (counter ())  // 2
```
