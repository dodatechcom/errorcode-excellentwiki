---
title: "[Solution] F# InvalidOperation Sequence Is Empty"
description: "Fix F# InvalidOperation when calling First, Single, or Head on empty sequences. Use TryFirst, TryHead, or check emptiness."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `InvalidOperationException` with message `Sequence contains no elements` occurs when you call `Seq.head`, `Seq.first`, `Seq.exactlyOne`, or similar functions on an empty sequence.

## Common Causes

- Calling head/first on empty collection
- Using single where multiple elements exist
- LINQ First() without Where predicate matching
- Empty result from database query

## How to Fix

```fsharp
// WRONG: Calling head on empty sequence
let items: int list = []
let first = List.head items  // InvalidOperationException

// CORRECT: Check if empty first
let items: int list = []
let first = if List.isEmpty items then 0 else List.head items
```

```fsharp
// WRONG: Seq.head on empty
let result = Seq.head (Seq.empty<int>)  // Error

// CORRECT: Use Seq.tryHead (F# 6+)
let result = Seq.tryHead (Seq.empty<int>)
// result = None
```

```fsharp
// WRONG: LINQ First() on empty
open System.Linq
let items = Seq.empty<int>
let first = items.First()  // InvalidOperationException

// CORRECT: Use Seq.tryHead or Seq.head with guard
let first = 
    if Seq.isEmpty items then 0
    else Seq.head items
```

## Examples

```fsharp
// Example 1: Safe head functions
let safeHead xs =
    match xs with
    | [] -> None
    | x :: _ -> Some x

// Example 2: Seq.tryHead (F# 6+)
let items = [1; 2; 3] |> List.toSeq
let first = items |> Seq.tryHead  // Some 1

// Example 3: Default value with headOr
let headOr defaultVal xs =
    match xs with
    | [] -> defaultVal
    | x :: _ -> x

let result = headOr 0 []  // 0
let result2 = headOr 0 [1; 2]  // 1
```

## Related Errors

- [fsharp-indexoutofrange]({{< relref "/languages/fsharp/fsharp-indexoutofrange" >}}) — index out of range
- [fsharp-notfoundexception]({{< relref "/languages/fsharp/fsharp-notfoundexception" >}}) — key not found
- [fsharp-matcherror]({{< relref "/languages/fsharp/fsharp-matcherror" >}}) — match failure
