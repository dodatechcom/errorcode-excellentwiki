---
title: "[Solution] F# OutOfMemoryException"
description: "Fix F# OutOfMemoryException when the .NET runtime cannot allocate more memory. Optimize data structures and use streaming."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `OutOfMemoryException` occurs when the .NET garbage collector cannot allocate enough memory to fulfill a request. This happens when processing large datasets or creating many objects.

## Common Causes

- Loading large files entirely into memory
- Building large intermediate collections
- Memory leaks from retained references
- Large string concatenation
- Too many objects preventing GC

## How to Fix

```fsharp
// WRONG: Loading entire file into memory
let lines = System.IO.File.ReadAllLines("huge.csv")  // May OOM

// CORRECT: Process line by line
System.IO.File.ReadLines("huge.csv")
|> Seq.iter (fun line -> processLine line)
```

```fsharp
// WRONG: Building large list in memory
let result = [1 .. 10000000] |> List.map (fun x -> x * x)  // OOM

// CORRECT: Use sequences (lazy evaluation)
let result = seq { 1 .. 10000000 } |> Seq.map (fun x -> x * x)
// Process lazily
result |> Seq.iter (fun x -> printfn "%d" x)
```

```fsharp
// WRONG: String concatenation in loop
let mutable result = ""
for i in 1 .. 1000000 do
    result <- result + i.ToString()  // OOM

// CORRECT: Use StringBuilder or Array.concat
let sb = System.Text.StringBuilder()
for i in 1 .. 1000000 do
    sb.Append(i.ToString()) |> ignore
let result = sb.ToString()
```

## Examples

```fsharp
// Example 1: Streaming file processing
open System.IO

let processFile path =
    use reader = new StreamReader(path)
    while not reader.EndOfStream do
        let line = reader.ReadLine()
        processLine line

// Example 2: Chunked processing
let processInChunks size items =
    items
    |> Seq.chunkBySize size
    |> Seq.iter (fun chunk -> processChunk chunk)

// Example 3: Monitor memory
let checkMemory () =
    let mem = System.GC.GetTotalMemory(false)
    printfn "Memory: %d bytes" mem
    if mem > 1_000_000_000L then
        System.GC.Collect()
```

## Related Errors

- [fsharp-stackoverflowexception]({{< relref "/languages/fsharp/fsharp-stackoverflowexception" >}}) — stack overflow
- [fsharp-operationcanceled]({{< relref "/languages/fsharp/fsharp-operationcanceled" >}}) — operation cancelled
- [fsharp-invalidoperation]({{< relref "/languages/fsharp/fsharp-invalidoperation" >}}) — invalid operation
