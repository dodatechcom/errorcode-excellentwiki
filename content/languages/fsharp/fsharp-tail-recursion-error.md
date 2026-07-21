---
title: "[Solution] F# Tail Recursion Error -- Stack Overflow Prevention"
description: "Fix F# tail recursion errors to prevent stack overflows. Learn tail-recursive patterns and the tailRec function."
languages: ["fsharp"]
error-types: ["runtime"]
severities: ["error"]
---

# F# Tail Recursion Error

A tail recursion error occurs when a recursive function consumes too much stack space because it is not properly tail-recursive.

## Common Causes

- Recursive call is not the last expression in the function
- Additional computation after the recursive call
- Missing accumulator parameters for state threading
- Using recursion where iteration would suffice

## How to Fix

### Convert to tail-recursive with accumulator

```fsharp
// WRONG: not tail-recursive -- multiplies after recursive call
let rec factorial n =
    if n <= 1 then 1
    else n * factorial (n - 1)

// CORRECT: tail-recursive with accumulator
let factorial n =
    let rec loop n acc =
        if n <= 1 then acc
        else loop (n - 1) (acc * n)
    loop n 1
```

### Use the FSharp.Core tailRec function

```fsharp
open Microsoft.FSharp.Core.Operators.Checked

let sumList items =
    items
    |> List.fold (fun acc item -> acc + item) 0
```

## Examples

```fsharp
let fibonacci n =
    let rec loop i prev curr =
        if i = 0 then prev
        else loop (i - 1) curr (prev + curr)
    loop n 0 1

let result = fibonacci 100  // works without stack overflow
```
