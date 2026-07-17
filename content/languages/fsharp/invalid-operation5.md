---
title: "InvalidOperationException"
description: "An InvalidOperationException occurs when a method call is invalid for the object's current state."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `InvalidOperationException` is thrown when a method is called on an object in a state that doesn't support that operation. This is common with enumerators, streams, and collection types.

## Common Causes

- Calling methods in wrong order
- Using disposed resources
- Enumerating collection while modifying it
- Calling methods on objects in invalid state

## How to Fix

```fsharp
// WRONG: Modifying during enumeration
let list = [1; 2; 3]
for item in list do
    if item = 2 then
        list.RemoveAt(1)  // InvalidOperationException

// CORRECT: Create new collection
let list = [1; 2; 3]
let modified = list |> List.filter (fun x -> x <> 2)
```

```fsharp
// WRONG: Using disposed stream
let stream = new System.IO.MemoryStream()
stream.Close()
stream.ReadByte()  // InvalidOperationException

// CORRECT: Check if disposed
let stream = new System.IO.MemoryStream()
if stream.CanRead then
    stream.ReadByte()
```

## Examples

```fsharp
// Example 1: Enumerator invalidation
let arr = [|1; 2; 3|]
let enumerator = arr.GetEnumerator()
while enumerator.MoveNext() do
    arr.[0] <- 100  // InvalidOperationException

// Example 2: Stream closed
let fs = System.IO.File.OpenRead("test.txt")
fs.Close()
fs.Read([|0uy|], 0, 1)  // ObjectDisposedException

// Example 3: Wrong state
let queue = System.Collections.Generic.Queue<int>()
queue.Dequeue()  // InvalidOperationException (empty)
```

## Related Errors

- [NullReferenceException](/languages/fsharp/null-reference5)
- [ArgumentException](/languages/fsharp/argument-exception)
