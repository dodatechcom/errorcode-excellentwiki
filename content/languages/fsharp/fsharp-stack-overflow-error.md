---
title: "[Solution] F# Stack Overflow Error -- Deep Recursion Issues"
description: "Fix F# stack overflow errors caused by deep recursion, circular references, or unbounded call chains."
languages: ["fsharp"]
error-types: ["runtime"]
severities: ["error"]
---

# F# Stack Overflow Error

This error occurs when the call stack overflows due to deeply nested function calls or unbounded recursion.

## Common Causes

- Non-tail-recursive functions with large input
- Circular type references creating infinite loops
- Deep LINQ expression chains in .NET interop
- Very large nested computation expression chains

## How to Fix

### Convert to tail recursion

```fsharp
// WRONG: deep recursion without tail call
let rec traverse depth =
    if depth = 0 then "leaf"
    else "node(" + traverse (depth - 1) + ")"

// CORRECT: tail-recursive with accumulator
let traverse maxDepth =
    let rec loop depth acc =
        if depth = 0 then acc
        else loop (depth - 1) ("node(" + acc + ")")
    loop maxDepth "leaf"
```

### Use stack-safe iteration

```fsharp
let safeSum items =
    Seq.fold (fun acc item -> acc + item) 0 items
```

## Examples

```fsharp
open System.Threading.Tasks

// Stack-safe async with trampoline
let rec trampoline depth =
    task {
        if depth = 0 then return 0
        else
            let! sub = Task.FromResult(0) |> Async.AwaitTask
            return 1 + sub
    }
```
