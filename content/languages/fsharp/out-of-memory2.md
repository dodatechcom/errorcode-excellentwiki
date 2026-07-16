---
title: "OutOfMemoryException"
description: "An OutOfMemoryException occurs when the system runs out of memory to allocate."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["memory", "out-of-memory", "allocation", "outofmemoryexception"]
weight: 5
---

## What This Error Means

An `OutOfMemoryException` is thrown when the .NET runtime cannot allocate enough memory to fulfill a request. This can happen when creating very large arrays, strings, or when there's a memory leak.

## Common Causes

- Creating very large arrays or collections
- Memory leaks from unreleased resources
- Accumulating large objects in memory
- Insufficient memory on system

## How to Fix

```fsharp
// WRONG: Creating huge array
let hugeArray = Array.zeroCreate<int64> (1024 * 1024 * 1024)  // OutOfMemoryException

// CORRECT: Process in chunks
let processInChunks size =
    [|1..1000000|]
    |> Array.chunkBySize size
    |> Array.iter (fun chunk -> processChunk chunk)
```

```fsharp
// WRONG: Building huge string in memory
let rec buildHugeString n =
    if n = 0 then ""
    else buildHugeString (n - 1) + "x"

// CORRECT: Use StringBuilder
open System.Text
let sb = StringBuilder()
for i in 1..1000000 do
    sb.Append("x") |> ignore
let result = sb.ToString()
```

## Examples

```fsharp
// Example 1: Huge list
let rec infiniteList() = 1 :: infiniteList()
infiniteList()  // OutOfMemoryException

// Example 2: Large allocation
let arr = Array.create (System.Int32.MaxValue / 2) 0  // OutOfMemoryException

// Example 3: String concatenation
let mutable s = ""
for i in 1..100000000 do
    s <- s + "a"  // OutOfMemoryException
```

## Related Errors

- [StackOverflowException](/languages/fsharp/stack-overflow2)
- [IndexOutOfRangeException](/languages/fsharp/index-out-of-range)
