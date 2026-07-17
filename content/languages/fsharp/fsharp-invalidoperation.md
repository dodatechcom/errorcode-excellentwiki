---
title: "InvalidOperationException in F#"
description: "F# raises InvalidOperationException when a method call is invalid for the object's current state"
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["invalidoperation", "state", "sequence", " enumerator"]
weight: 5
---

## What This Error Means

An `InvalidOperationException` occurs when a method call is invalid given the object's current state. This commonly happens with sequence enumeration and collection operations.

## Common Causes

- Modifying collection during enumeration
- Calling method on disposed object
- Using enumerator after collection changed
- Invalid state transition

## How to Fix

Handle sequence modification:

```fsharp
let numbers = [1; 2; 3; 4; 5]

// Wrong: modifying during enumeration
// for n in numbers do
//     if n = 3 then numbers.Remove(n)

// Correct: create new collection
let filtered = numbers |> List.filter (fun n -> n <> 3)
```

Use.toList before modification:

```fsharp
let processAndFilter items =
    let snapshot = items |> List.ofSeq
    snapshot |> List.filter (fun x -> x > 0)
```

Check sequence state:

```fsharp
open System.Collections.Generic

let safeFirst (seq: seq<'a>) =
    use enumerator = seq.GetEnumerator()
    if enumerator.MoveNext() then
        Some enumerator.Current
    else
        None
```

## Examples

```fsharp
let list = ResizeArray([1; 2; 3])
for item in list do
    if item = 2 then list.Remove(item) |> ignore
// InvalidOperationException: Collection was modified during enumeration
```

## Related Errors

- [ArgumentException]({{< relref "/languages/fsharp/argument-exception" >}})
- [NullReferenceException]({{< relref "/languages/fsharp/null-reference5" >}})
