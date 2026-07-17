---
title: "IndexOutOfRangeException in F#"
description: "F# raises IndexOutOfRangeException when accessing an array or list at an invalid index"
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["index", "out-of-range", "array", "list", "range"]
weight: 5
---

## What This Error Means

An `IndexOutOfRangeException` occurs when trying to access an element at an index that is outside the valid range of the collection.

## Common Causes

- Accessing index >= collection length
- Negative index access
- Off-by-one errors in loops
- Empty collection access

## How to Fix

Check bounds before access:

```fsharp
let safeGet index (arr: 'a array) =
    if index >= 0 && index < arr.Length then
        Some arr.[index]
    else
        None
```

Use List.tryItem:

```fsharp
let numbers = [1; 2; 3]
let third = numbers |> List.tryItem 2  // Some 3
let fifth = numbers |> List.tryItem 4  // None
```

Use Seq.tryItem:

```fsharp
let items = seq { 1..5 }
let item = items |> Seq.tryItem 10  // None
```

Safe array access:

```fsharp
let getOrElse index defaultValue (arr: 'a array) =
    if index >= 0 && index < arr.Length then arr.[index]
    else defaultValue
```

## Examples

```fsharp
let arr = [|1; 2; 3|]
let value = arr.[5]  // IndexOutOfRangeException
```

## Related Errors

- [KeyNotFoundException]({{< relref "/languages/fsharp/notfoundexception" >}})
- [NullReferenceException]({{< relref "/languages/fsharp/null-reference5" >}})
