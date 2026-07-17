---
title: "[Solution] F# StackOverflowException in Recursion"
description: "Fix F# StackOverflowException in recursive functions. Convert to tail recursion or use iterative approaches."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `StackOverflowException` occurs when the .NET runtime runs out of stack space due to deep or infinite recursion. Each recursive call consumes stack space.

## Common Causes

- Unbounded recursion without base case
- Non-tail-recursive function
- Very deep recursion (>10,000 levels)
- Infinite loop in recursion

## How to Fix

```fsharp
// WRONG: Non-tail-recursive factorial
let rec factorial n =
    if n <= 0 then 1
    else n * factorial (n - 1)  // Not tail-recursive
// factorial 100000 may stack overflow

// CORRECT: Tail-recursive with accumulator
let factorial n =
    let rec loop n acc =
        if n <= 0 then acc
        else loop (n - 1) (n * acc)
    loop n 1
```

```fsharp
// WRONG: List recursion without tail call
let rec sumList lst =
    match lst with
    | [] -> 0
    | x :: xs -> x + sumList xs  // Not tail-recursive

// CORRECT: Use accumulator
let sumList lst =
    let rec loop lst acc =
        match lst with
        | [] -> acc
        | x :: xs -> loop xs (acc + x)
    loop lst 0
```

```fsharp
// WRONG: Deep tree recursion
let depth node =
    match node with
    | Leaf -> 0
    | Branch(left, right) -> 1 + max (depth left) (depth right)

// CORRECT: Use continuation-passing style
let depth node =
    let rec depthCont node cont =
        match node with
        | Leaf -> cont 0
        | Branch(left, right) ->
            depthCont left (fun ld ->
                depthCont right (fun rd ->
                    cont (1 + max ld rd)))
    depthCont node id
```

## Examples

```fsharp
// Example 1: Tail-recursive fib
let fib n =
    let rec loop n a b =
        if n = 0 then a
        else loop (n - 1) b (a + b)
    loop n 0 1

// Example 2: Use List.fold instead of recursion
let sumList lst = List.fold (+) 0 lst

// Example 3: CPS for complex recursion
let rec treeSum node =
    match node with
    | Leaf -> 0
    | Branch(v, left, right) ->
        v + treeSum left + treeSum right

// Tail-recursive version:
let treeSumCPS node =
    let rec aux node cont =
        match node with
        | Leaf -> cont 0
        | Branch(v, left, right) ->
            aux left (fun lSum ->
                aux right (fun rSum ->
                    cont (v + lSum + rSum)))
    aux node id
```

## Related Errors

- [fsharp-outofmemoryexception]({{< relref "/languages/fsharp/fsharp-outofmemoryexception" >}}) — out of memory
- [fsharp-matcherror]({{< relref "/languages/fsharp/fsharp-matcherror" >}}) — match failure
- [fsharp-operationcanceled]({{< relref "/languages/fsharp/fsharp-operationcanceled" >}}) — operation cancelled
