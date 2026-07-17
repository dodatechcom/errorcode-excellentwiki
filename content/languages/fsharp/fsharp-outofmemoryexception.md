---
title: "OutOfMemoryException in F#"
description: "F# raises OutOfMemoryException when the system runs out of memory"
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `OutOfMemoryException` occurs when the CLR cannot allocate more memory for objects. This happens when the managed heap is full and garbage collection cannot free enough space.

## Common Causes

- Loading too much data into memory
- Memory leaks (retained references)
- Large array/list allocations
- Infinite recursion creating stack objects
- Insufficient .NET heap configuration

## How to Fix

Process data in chunks:

```fsharp
let processLargeFile path =
    seq {
        use reader = System.IO.File.ReadLines(path)
        for line in reader do
            processLine line
    }
```

Use sequences for lazy evaluation:

```fsharp
// Wrong: loads all into memory
let data = [1..10000000] |> List.map expensiveComputation

// Correct: lazy evaluation
let data = seq { 1..10000000 } |> Seq.map expensiveComputation
data |> Seq.take 100 |> Seq.iter (printfn "%A")
```

Increase heap size:

```bash
dotnet run --roll-forward LatestMajor -e DOTNET_GCHeapHardLimit=4000000000
```

Dispose resources:

```fsharp
let processResource path =
    use stream = System.IO.File.OpenRead(path)
    // Process file
    stream.CopyTo(System.Console.OpenStandardOutput())
```

## Examples

```fsharp
let array = Array.create (System.Int32.MaxValue) 0  // OutOfMemoryException
```

## Related Errors

- [StackOverflowException]({{< relref "/languages/fsharp/stack-overflow2" >}})
- [NullReferenceException]({{< relref "/languages/fsharp/null-reference5" >}})
