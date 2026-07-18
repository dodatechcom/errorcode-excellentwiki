---
title: "[Solution] F# Async Timeout — Waiting for Async Result Too Long"
description: "Fix F# async timeout errors when waiting for results. Learn Async.RunChildWithTimeout, CancellationTokenSource, and timeout patterns."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An async timeout error occurs when an F# `Async` workflow does not complete within the expected time. The error is typically a `System.TimeoutException` or `OperationCanceledException` thrown by the timeout mechanism. This happens when using `Async.RunSynchronously` with a timeout or when a `CancellationTokenSource` expires.

## Why It Happens

The most common cause is calling `Async.RunSynchronously` without a timeout on a workflow that takes longer than expected. The calling thread blocks indefinitely until the async completes.

Another frequent cause is using `CancellationTokenSource` with a timeout that is too short. If the workflow needs 30 seconds but the timeout is 10 seconds, the workflow is canceled.

Network calls inside async workflows are a frequent source of timeouts. HTTP requests, database queries, and remote procedure calls can be slow or unresponsive, causing the async to hang.

Deadlocks between async workflows and synchronous code are another common cause. If an async workflow posts to the synchronization context and the context is blocked waiting for the workflow, a deadlock occurs.

Finally, nested async workflows that do not propagate cancellation tokens correctly may continue running after the parent has timed out.

## How to Fix It

### Use Async.StartChild for timeout patterns

```fsharp
let withTimeout timeout work = async {
    let child = Async.StartChild(work, timeout)
    let! childWork = child
    try
        let! result = childWork
        return Some result
    with
    | :? System.TimeoutException -> None
}

let result = withTimeout (TimeSpan.FromSeconds(5.0)) longRunningWork
             |> Async.RunSynchronously
```

### Use CancellationTokenSource with timeout

```fsharp
let runWithTimeout timeout work = async {
    use cts = new System.Threading.CancellationTokenSource(timeout)
    return! Async.RunChild(work, cts.Token)
}

let result = runWithTimeout 5000 myWorkflow |> Async.RunSynchronously
```

### Avoid deadlocks with async

```fsharp
// Wrong — may deadlock
let result = async { return! doWork() } |> Async.RunSynchronously

// Correct — use async all the way
let result = async {
    let! workResult = doWork()
    return workResult
}
```

### Use Async.Race for competing workflows

```fsharp
let race work1 work2 = async {
    let tcs = System.Threading.Tasks.TaskCompletionSource()
    use cts = new System.Threading.CancellationTokenSource()

    let runWork work = async {
        try
            let! result = work
            tcs.TrySetResult(result) |> ignore
        with _ -> ()
    }

    Async.Start(runWork work1, cts.Token)
    Async.Start(runWork work2, cts.Token)

    return! Async.AwaitTask tcs.Task
}
```

### Set appropriate timeouts based on operation type

```fsharp
// Database query — generous timeout
let dbTimeout = TimeSpan.FromSeconds(30.0)

// HTTP request — moderate timeout
let httpTimeout = TimeSpan.FromSeconds(10.0)

// Cache lookup — short timeout
let cacheTimeout = TimeSpan.FromSeconds(1.0)
```

## Common Mistakes

- Using `Async.RunSynchronously` without a timeout
- Setting timeouts too short for the actual operation duration
- Not propagating cancellation tokens to nested async workflows
- Mixing synchronous blocking with async code, causing deadlocks
- Not cleaning up resources when a timeout occurs

## Related Pages

- [F# OperationCanceledException](/languages/fsharp/fsharp-operation-canceled/)
- [F# OutOfMemoryException](/languages/fsharp/fsharp-out-of-memory/)
- [F# Computation Expression Error](/languages/fsharp/fsharp-computation-expression/)
