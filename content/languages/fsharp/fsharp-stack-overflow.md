---
title: "[Solution] F# StackOverflowException — Infinite Recursion in Function"
description: "Fix F# StackOverflowException from deep or infinite recursion. Learn tail recursion, trampolines, and iterative alternatives."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `StackOverflowException` is thrown when the call stack overflows due to excessive or infinite recursion. Each recursive call adds a frame to the call stack, and when the stack exceeds its limit (typically 1MB), the .NET runtime terminates the process. This exception cannot be caught with `try-catch`.

## Why It Happens

The most common cause is a recursive function that is not in tail position. When a function performs work after the recursive call, the compiler cannot optimize it into a loop, and each call consumes stack space.

Mutually recursive functions (where function A calls B and B calls A) can overflow the stack even if each call appears to be in tail position, because the .NET JIT compiler does not always perform tail-call optimization.

Infinite recursion from incorrect base cases is another frequent cause. For example, a factorial function that checks `n = 0` but receives negative input will recurse forever.

Recursive data structures like deeply nested trees or linked lists can cause stack overflow when traversed with recursive functions. A tree with tens of thousands of levels will overflow even a correct tail-recursive function.

Finally, calling `printfn` or other I/O functions inside deep recursion can consume additional stack space per call.

## How to Fix It

### Use tail recursion with an accumulator

```fsharp
// Not tail recursive
let rec factorial n =
    if n <= 1 then 1 else n * factorial (n - 1)

// Tail recursive
let factorial n =
    let rec loop acc n =
        if n <= 1 then acc
        else loop (acc * n) (n - 1)
    loop 1 n
```

### Use Seq.fold for list accumulation

```fsharp
let sum lst = lst |> List.fold (fun acc x -> acc + x) 0
```

### Convert recursive algorithms to iterative

```fsharp
// Recursive Fibonacci (stack overflow risk)
let rec fib n =
    if n <= 1 then n else fib (n - 1) + fib (n - 2)

// Iterative Fibonacci
let fib n =
    let mutable a, b = 0, 1
    for _ in 2 .. n do
        let temp = a + b
        a <- b
        b <- temp
    if n = 0 then 0 else b
```

### Use a trampoline for mutual recursion

```fsharp
type Trampoline<'a> =
    | Done of 'a
    | Step of (unit -> Trampoline<'a>)

let rec run trampoline =
    match trampoline with
    | Done value -> value
    | Step f     -> run (f ())

let isEven n =
    let rec loop n =
        if n = 0 then Done true
        else Step (fun () -> loop (n - 1))
    loop n
```

### Increase stack size temporarily

```bash
dotnet run --roll-forward LatestMajor
# Or set COMPlus_DefaultStackSize environment variable
```

## Common Mistakes

- Writing recursive functions without checking for tail position
- Performing computation after the recursive call instead of in an accumulator
- Assuming .NET always performs tail-call optimization
- Not checking for infinite recursion in base cases
- Using recursion where iteration would be more appropriate

## Related Pages

- [F# OutOfMemoryException](/languages/fsharp/fsharp-out-of-memory/)
- [F# MatchFailureException](/languages/fsharp/fsharp-match-failure/)
- [F# OperationCanceledException](/languages/fsharp/fsharp-operation-canceled/)
