---
title: "StackOverflowException in F#"
description: "F# raises StackOverflowException when the call stack overflows from deep recursion"
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["stackoverflow", "recursion", "stack", "tail-call", "overflow"]
weight: 5
---

## What This Error Means

A `StackOverflowException` occurs when a method calls itself recursively too many times, exhausting the call stack. This is fatal and cannot be caught in .NET.

## Common Causes

- Deep recursion without tail-call optimization
- Infinite recursive loop
- Missing base case
- Very deep object graph traversal

## How to Fix

Use tail-recursive functions:

```fsharp
// Wrong: not tail-recursive
let rec factorial n =
    if n <= 1 then 1
    else n * factorial (n - 1)  // Stack overflow for large n

// Correct: tail-recursive with accumulator
let factorial n =
    let rec loop n acc =
        if n <= 1 then acc
        else loop (n - 1) (n * acc)
    loop n 1
```

Use `tailrec` attribute:

```fsharp
[<TailCall>]
let rec sumList lst acc =
    match lst with
    | [] -> acc
    | head :: tail -> sumList tail (acc + head)
```

Convert to iterative:

```fsharp
let sumList items =
    let mutable total = 0
    for item in items do
        total <- total + item
    total
```

Use fold:

```fsharp
let factorial n =
    [1..n] |> List.fold (fun acc x -> acc * x) 1
```

## Examples

```fsharp
let rec infinite () = infinite ()
infinite ()  // StackOverflowException
```

## Related Errors

- [OutOfMemoryException]({{< relref "/languages/fsharp/out-of-memory2" >}})
- [MatchFailureException]({{< relref "/languages/fsharp/match-failure" >}})
