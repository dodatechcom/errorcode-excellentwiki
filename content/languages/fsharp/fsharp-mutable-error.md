---
title: "[Solution] F# Mutable Variable Capture Error — How to Fix"
description: "Fix F# mutable variable capture errors in closures and lambdas. Learn why mutable capture is restricted and how to work around it safely in your F# code."
languages: ["fsharp"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

F# restricts the capture of mutable variables in closures to prevent subtle bugs related to shared state. When a lambda or closure captures a mutable variable, the behavior may be unexpected because the closure sees the current value of the variable, not the value at the time of capture.

The most common cause is using a mutable variable inside a lambda that is executed later. The lambda captures a reference to the variable, not its value, and sees whatever value the variable has when the lambda runs.

Another frequent cause is capturing mutable variables in list or sequence computations. Operations like `List.map`, `List.iter`, and `Seq.delay` create closures that capture variables, and the timing of execution affects what values are seen.

Mutable variables in recursive functions that are captured by closures cause especially confusing behavior. The closure sees the accumulated value from each iteration, not the value at the point of capture.

Thread safety concerns with mutable variable capture in concurrent code can cause race conditions. Multiple threads accessing the same mutable variable through closures can produce non-deterministic results.

The F# compiler detects most mutable capture issues and reports them as warnings or errors, but some cases involving higher-order functions or complex control flow may not be caught.

## Common Error Messages

```
error FS0052: The mutable variable 'x' is used in a way that is not thread safe
```

```
warning FS0052: Mutable variable captured by closure — value may change before closure executes
```

```
error FS0039: The mutable variable 'counter' cannot be captured in this expression
```

```
warning FS0052: This mutable local is captured by a closure, which is not allowed in this context
```

## How to Fix It

### Use immutable bindings instead of mutable variables

```fsharp
// Wrong — mutable variable captured in closure
let mutable counter = 0
let incrementers = [
    fun () -> counter <- counter + 1
]

// Better — use immutable values with explicit state
let counter = ref 0
let incrementers = [
    fun () -> counter := !counter + 1
]
```

### Use ref cells for mutable state in closures

```fsharp
// ref cells can be captured in closures
let state = ref 0

let processors = [
    fun () -> state := !state + 1
    fun () -> state := !state * 2
]

// Execute in sequence
processors |> List.iter (fun f -> f())
printfn "Final state: %d" !state
```

### Use mutable variables only in simple scopes

```fsharp
// Mutable in a simple loop — no closure capture
for i in 1..10 do
    let mutable sum = 0
    sum <- sum + i
    printfn "%d" sum

// Wrong — mutable captured by closure
let mutable total = 0
let addToTotal = fun () -> total <- total + 1
```

### Use accumulator pattern for fold operations

```fsharp
// Wrong — mutable accumulator
let mutable total = 0
[1; 2; 3; 4; 5] |> List.iter (fun x -> total <- total + x)

// Correct — use List.fold
let total = [1; 2; 3; 4; 5] |> List.fold (+) 0

// Or use List.sum
let total = [1; 2; 3; 4; 5] |> List.sum
```

### Use async state management correctly

```fsharp
// Wrong — mutable captured across async boundaries
let mutable lastResult = None
async {
    let! result = someAsyncOperation()
    lastResult <- Some result
}

// Correct — use immutable state with return values
async {
    let! result = someAsyncOperation()
    return Some result
}
```

## Common Scenarios

- Building a pipeline of functions that accumulate results
- Creating event handlers that need to update shared state
- Working with concurrent operations that modify shared mutable state

## Prevent It

- Prefer immutable data and `List.fold` or `Seq.fold` over mutable accumulators
- Use `ref` cells when you need mutable state that closures can safely capture
- Avoid capturing mutable variables in lambdas that are executed asynchronously or in different threads
