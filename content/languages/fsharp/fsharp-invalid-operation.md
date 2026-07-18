---
title: "[Solution] F# InvalidOperationException — Sequence Empty Error"
description: "Fix F# InvalidOperationException when calling First, Single, or Last on empty sequences. Use safe alternatives like tryHead and Seq.tryFind."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An `InvalidOperationException` with the message "Sequence contains no elements" is thrown when you call `Seq.head`, `Seq.first`, `Seq.last`, `Seq.exactlyOne`, or `Seq.reduce` on an empty sequence. These methods require at least one element and throw if the sequence is empty.

## Why It Happens

The most common cause is calling `.Head` or `Seq.head` on an empty list or sequence. This happens when filtering produces no results, when database queries return empty collections, or when reading from sources that may not have data.

Another frequent cause is using `Seq.reduce` on an empty sequence. The `reduce` function applies a function to combine elements, but it needs at least one element to start with.

Using `Seq.exactlyOne` when the sequence has zero or more than one element also throws this exception. This is useful for enforcing single-element sequences but fails if the assumption is wrong.

Linq operations like `.First()` and `.Single()` are also common sources. Unlike `Seq.head` which returns the first element, `.First()` throws with a different exception message.

Finally, lazy sequences that evaluate to empty when materialized can cause this error when consumed with eager methods.

## How to Fix It

### Use tryHead for safe first element access

```fsharp
let firstItem = myList |> List.tryHead
match firstItem with
| Some item -> printfn "First: %A" item
| None      -> printfn "List is empty"
```

### Use Seq.tryFind instead of Seq.find

```fsharp
let found = myList |> Seq.tryFind (fun x -> x > 10)
match found with
| Some value -> printfn "Found: %d" value
| None       -> printfn "No matching element"
```

### Check isEmpty before accessing elements

```fsharp
if myList |> List.isEmpty |> not then
    let first = myList |> List.head
    printfn "First: %A" first
```

### Use Option.map for safe transformations

```fsharp
let result =
    myList
    |> List.tryHead
    |> Option.map (fun x -> x * 2)
    |> Option.defaultValue 0
```

### Use Seq.tryHead for sequences

```fsharp
let processItems items =
    items
    |> Seq.tryHead
    |> function
    | Some item -> processItem item
    | None      -> printfn "No items to process"
```

## Common Mistakes

- Using `.Head` without checking `.IsEmpty` first
- Using `Seq.reduce` instead of `Seq.fold` with an initial value
- Calling `.First()` from Linq instead of F#'s `Seq.tryHead`
- Not handling empty sequences in data pipelines
- Assuming a database query will always return at least one row

## Related Pages

- [F# NullReferenceException](/languages/fsharp/fsharp-nullreference/)
- [F# IndexOutOfRangeException](/languages/fsharp/fsharp-indexoutofrange/)
- [F# KeyNotFoundException](/languages/fsharp/fsharp-key-not-found/)
