---
title: "OperationCanceledException in F#"
description: "F# raises OperationCanceledException when an async operation is cancelled"
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `OperationCanceledException` occurs when an asynchronous operation is cancelled via a `CancellationToken`. This is a normal part of async programming in .NET.

## Common Causes

- CancellationToken triggered during async work
- Timeout exceeded on async operation
- User cancelled long-running task
- Application shutdown during async work

## How to Fix

Handle cancellation gracefully:

```fsharp
open System.Threading
open System.Threading.Tasks

let longRunningTask (ct: CancellationToken) =
    async {
        for i in 1..100 do
            ct.ThrowIfCancellationRequested()
            do! Async.Sleep(100)
            printfn "Step %d" i
        return "Done"
    }
```

Use try-with:

```fsharp
let safeOperation ct =
    async {
        try
            let! result = longRunningTask ct
            return result
        with :? OperationCanceledException ->
            return "Cancelled"
    }
```

Register cancellation callback:

```fsharp
let withCleanup ct =
    async {
        use _reg = ct.Register(fun () -> printfn "Cleaning up...")
        do! Async.Sleep(10000)
        return "Completed"
    }
```

Use Async.CancellationToken:

```fsharp
let work () =
    async {
        let! ct = Async.CancellationToken
        return! longRunningTask ct
    }
```

## Examples

```fsharp
let cts = new CancellationTokenSource()
cts.CancelAfter(1000)

async {
    do! Async.Sleep(5000)
    printfn "This won't print"
} |> Async.Start(ct = cts.Token)
// OperationCanceledException
```

## Related Errors

- [OutOfMemoryException]({{< relref "/languages/fsharp/out-of-memory2" >}})
- [StackOverflowException]({{< relref "/languages/fsharp/stack-overflow2" >}})
