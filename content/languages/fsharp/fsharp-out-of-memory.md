---
title: "[Solution] F# OutOfMemoryException — Heap Space Exhausted in F# Process"
description: "Fix F# OutOfMemoryException when memory is exhausted. Learn lazy evaluation, streaming, array pooling, and .NET memory management."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An `OutOfMemoryException` is thrown when the .NET garbage collector cannot free enough memory to satisfy an allocation request. The process has exhausted its available heap space, and the runtime cannot allocate more memory for new objects.

## Why It Happens

The most common cause is loading entire datasets into memory at once. Reading a large CSV file into a `list` or `array` can consume gigabytes of memory if the file is large enough.

Recursive functions that build up large intermediate structures without tail-call optimization also cause this issue. Each recursive call retains a reference to previous stack frames, preventing garbage collection.

String concatenation in loops creates many temporary objects that consume memory before they can be collected. Each `+` operation on strings creates a new string object.

Mutable collections that grow without bounds (like `List<T>` or `Dictionary<T,U>` that are never cleared) accumulate objects that the garbage collector cannot reclaim.

Finally, the default .NET heap size may be too small for the application. The CLR typically allows up to 2GB for 32-bit processes and much more for 64-bit, but configuration may limit this.

## How to Fix It

### Use sequences for lazy evaluation

```fsharp
// Wrong — loads all data into memory
let data = System.IO.File.ReadAllLines("huge.csv") |> Array.ofSeq

// Correct — processes one line at a time
let data = System.IO.File.ReadLines("huge.csv")
data |> Seq.iter (fun line -> processLine line)
```

### Use tail recursion for large iterations

```fsharp
// Not tail recursive
let rec sum lst =
    match lst with
    | [] -> 0
    | x :: xs -> x + sum xs

// Tail recursive
let sum lst =
    let rec loop acc = function
        | [] -> acc
        | x :: xs -> loop (acc + x) xs
    loop 0 lst
```

### Use StringBuilder for string concatenation

```fsharp
open System.Text.StringBuilder

let buildString items =
    let sb = StringBuilder()
    for item in items do
        sb.AppendLine(item) |> ignore
    sb.ToString()
```

### Process files in chunks

```fsharp
let processFile filePath =
    use reader = new System.IO.StreamReader(filePath)
    while not reader.EndOfStream do
        let line = reader.ReadLine()
        processLine line
```

### Increase memory limits if needed

```bash
# Set GC server mode for large applications
dotnet run --configFiles=dotnet.config

# In runtimeconfig.json
{
  "configProperties": {
    "System.GC.Server": true,
    "System.GC.HeapHardLimit": 4294967296
  }
}
```

## Common Mistakes

- Using `List` instead of `Seq` for large datasets
- Not using tail recursion for functions that process large lists
- Building strings with `+` in a loop instead of `StringBuilder`
- Holding references to large objects in closures
- Not disposing resources that implement `IDisposable`

## Related Pages

- [F# StackOverflowException](/languages/fsharp/fsharp-stackoverflow/)
- [F# InvalidOperation](/languages/fsharp/fsharp-invalidoperation/)
- [F# NullReferenceException](/languages/fsharp/fsharp-nullreference/)
