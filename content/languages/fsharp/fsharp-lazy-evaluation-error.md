---
title: "[Solution] F# Lazy Evaluation Error -- Thunk Value Issues"
description: "Fix F# lazy evaluation errors when lazy values are evaluated unexpectedly or cause side effects multiple times."
languages: ["fsharp"]
error-types: ["runtime"]
severities: ["warning"]
---

# F# Lazy Evaluation Error

This error occurs when lazy values are evaluated at the wrong time, causing duplicate side effects or unexpected performance issues.

## Common Causes

- Forgetting that lazy values are evaluated every time in non-lazy contexts
- Using `Lazy<T>` from .NET instead of F# lazy keyword
- Lazy values with side effects running multiple times
- Thread safety issues with shared lazy values

## How to Fix

### Use the lazy keyword correctly

```fsharp
// WRONG: evaluates immediately
let computation = lazy (expensiveCall())
let result = computation  // result is lazy, not evaluated yet
printfn "%A" result  // forces evaluation, prints Lazy<int>

// CORRECT: force with .Value or force function
let computation = lazy (expensiveCall())
let result = computation.Value  // forces evaluation
```

### Ensure thread safety

```fsharp
let threadSafeLazy =
    Lazy<float>.Create(fun () -> System.Math.PI)

let value = threadSafeLazy.Value  // thread-safe access
```

## Examples

```fsharp
let expensiveComputation n =
    printfn "Computing for %d..." n
    System.Threading.Thread.Sleep(1000)
    n * n

let lazyResult = lazy (expensiveComputation 42)
printfn "Before forcing"
let value = lazyResult.Value  // prints "Computing for 42..."
printfn "After forcing: %d" value
```
