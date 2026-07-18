---
title: "[Solution] F# IndexOutOfRangeException — Array Index Out of Bounds"
description: "Fix F# IndexOutOfRangeException when accessing arrays. Learn bounds checking, safe indexing with tryItem, and list/array best practices."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An `IndexOutOfRangeException` is thrown when you access an array, string, or list with an index that is less than zero or greater than or equal to the collection's length. The F# runtime performs bounds checking on array access and throws this exception for invalid indices.

## Why It Happens

The most common cause is using a loop counter that exceeds the array bounds. For example, iterating from 0 to `array.Length` (instead of `array.Length - 1`) accesses one element past the end.

Off-by-one errors are the classic source. Using `<=` instead of `<` in a loop condition or forgetting that F# arrays are zero-indexed causes this error.

Another frequent cause is calculating an index from external data (like a user input or database value) without validating it first. If the index comes from a calculation that can produce negative values or values beyond the array size, the access fails.

String indexing with `.Chars()` also throws this exception for out-of-range indices. Unlike some languages that return a default value, F# enforces strict bounds checking.

Finally, negative indices are never valid in F#. Some languages allow negative indexing from the end of an array, but F# does not, so `array.[-1]` throws this exception.

## How to Fix It

### Check bounds before array access

```fsharp
let safeAccess index (arr: 'a array) =
    if index >= 0 && index < arr.Length then
        Some arr.[index]
    else
        None
```

### Use List.tryItem for safe list indexing

```fsharp
let item = myList |> List.tryItem 5
match item with
| Some value -> printfn "Item: %A" value
| None       -> printfn "Index out of range"
```

### Use Seq.tryItem for sequences

```fsharp
let thirdItem = mySeq |> Seq.tryItem 2
```

### Validate index calculations

```fsharp
let getElementSafe index (arr: 'a array) =
    let normalizedIndex = index % arr.Length
    let safeIndex = if normalizedIndex < 0 then normalizedIndex + arr.Length else normalizedIndex
    arr.[safeIndex]
```

### Use safe array slicing

```fsharp
// Wrong — may throw if index is out of range
let subset = arr.[5..10]

// Correct — check bounds first
let subset =
    if arr.Length > 10 then arr.[5..10]
    elif arr.Length > 5 then arr.[5..]
    else [||]
```

### Use Array.tryFind instead of index-based access

```fsharp
let found = myArray |> Array.tryFind (fun x -> x > 100)
```

## Common Mistakes

- Using `arr.Length` as an index (valid indices are 0 to Length-1)
- Not checking for negative indices from calculations
- Using mutable index variables that may not be updated correctly
- Assuming List and Array have the same performance characteristics for random access
- Forgetting that string indexing in F# uses `.Chars()` method

## Related Pages

- [F# KeyNotFoundException](/languages/fsharp/fsharp-key-not-found/)
- [F# ArgumentException](/languages/fsharp/fsharp-argument-exception/)
- [F# InvalidOperation](/languages/fsharp/fsharp-invalidoperation/)
