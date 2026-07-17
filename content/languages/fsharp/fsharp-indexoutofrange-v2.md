---
title: "[Solution] F# IndexOutOfRangeException"
description: "Fix F# IndexOutOfRangeException when accessing elements beyond valid indices. Use safe indexing with tryGet or bounds checks."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `IndexOutOfRangeException` occurs when you access an element at an index that is outside the valid bounds of an array, list, or string.

## Common Causes

- Index exceeds collection length
- Off-by-one error in loops
- Empty collection access
- Negative index (for arrays)
- String index beyond length

## How to Fix

```fsharp
// WRONG: Index exceeds bounds
let items = [| 1; 2; 3 |]
let value = items.[5]  // IndexOutOfRangeException

// CORRECT: Check bounds first
let items = [| 1; 2; 3 |]
let value = if items.Length > 5 then items.[5] else 0
```

```fsharp
// WRONG: Accessing empty array
let empty = Array.empty<int>
let first = empty.[0]  // IndexOutOfRangeException

// CORRECT: Check if empty
let empty = Array.empty<int>
let first = if Array.isEmpty empty then 0 else empty.[0]
```

```fsharp
// WRONG: Off-by-one in loop
let items = [| "a"; "b"; "c" |]
for i in 0 .. items.Length do  // Length is exclusive bound
    printfn "%s" items.[i]  // Error on i = 3

// CORRECT: Use correct range
for i in 0 .. items.Length - 1 do
    printfn "%s" items.[i]
```

## Examples

```fsharp
// Example 1: Safe array access
let tryGet index (arr: 'a array) =
    if index >= 0 && index < arr.Length then Some arr.[index]
    else None

let items = [| 1; 2; 3 |]
printfn "%A" (tryGet 1 items)  // Some 2
printfn "%A" (tryGet 5 items)  // None

// Example 2: Safe string indexing
let tryCharAt index (s: string) =
    if index >= 0 && index < s.Length then Some s.[index]
    else None

// Example 3: Using Seq.tryItem (F# 6+)
let items = [1; 2; 3] |> List.toSeq
let item = items |> Seq.tryItem 1  // Some 2
```

## Related Errors

- [fsharp-invalidoperation]({{< relref "/languages/fsharp/fsharp-invalidoperation" >}}) — sequence empty
- [fsharp-argumentexception]({{< relref "/languages/fsharp/fsharp-argumentexception" >}}) — argument error
- [fsharp-notfoundexception]({{< relref "/languages/fsharp/fsharp-notfoundexception" >}}) — key not found
