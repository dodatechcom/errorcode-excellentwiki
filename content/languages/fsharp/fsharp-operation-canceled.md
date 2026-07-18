---
title: "[Solution] F# OperationCanceledException — Async Task Cancellation Error"
description: "Fix F# OperationCanceledException in async workflows. Learn CancellationToken, async cancellation patterns, and cooperative cancellation."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An `OperationCanceledException` is thrown when an asynchronous operation is canceled via a `CancellationToken`. This is the standard .NET way to signal that an operation should stop. In F#, async workflows respect cancellation tokens and throw this exception when canceled.

## Why It Happens

The most common cause is a `CancellationTokenSource` being canceled externally (like when a user cancels an HTTP request or a timeout expires). The async workflow detects the cancellation and throws `OperationCanceledException`.

Another frequent cause is not registering cancellation callbacks in long-running async operations. If the async workflow does not check the cancellation token periodically, it continues running until it finishes or the runtime forcefully terminates it.

Timeout configurations in ASP.NET Core or HttpClient that are too short cause operations to be canceled before they complete. The default `HttpClient` timeout is 100 seconds, which may not be enough for slow operations.

Nested async workflows that do not propagate cancellation tokens correctly can cause unexpected cancellations. If a child workflow is canceled but the parent is not, the exception propagates up.

Finally, calling `Async.AwaitTask` on a task that was canceled throws `OperationCanceledException` wrapped in `TaskCanceledException`.

## How to Fix It

### Check cancellation token in async workflows

```fsharp
open System.Threading

let longRunningTask (ct: CancellationToken) = async {
    for i in 1 .. 1000 do
        ct.ThrowIfCancellationRequested()
        do! Async.Sleep(100)
        printfn "Step %d" i
    return "Done"
}
```

### Use Async.CancellationToken to get the token

```fsharp
let myWorkflow = async {
    let! ct = Async.CancellationToken
    return! longRunningTask ct
}
```

### Handle cancellation gracefully

```fsharp
let safeWorkflow = async {
    try
        return! longRunningOperation()
    with
    | :? OperationCanceledException ->
        printfn "Operation was canceled"
        return "Canceled"
}
```

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
```

### Register cleanup with cancellation token

```fsharp
let withCleanup (ct: CancellationToken) = async {
    let! reg = ct.Register(fun () -> printfn "Cleaning up")
    try
        return! work()
    finally
        reg.Dispose()
}
```

## Common Mistakes

- Not checking `CancellationToken` in long-running loops
- Using `Async.RunSynchronously` without passing a cancellation token
- Swallowing `OperationCanceledException` without cleanup
- Not propagating cancellation tokens to child async workflows
- Setting very short timeouts without considering actual operation duration

## Related Pages

- [F# NullReferenceException](/languages/fsharp/fsharp-nullreference/)
- [F# InvalidOperation](/languages/fsharp/fsharp-invalidoperation/)
- [F# StackOverflowException](/languages/fsharp/fsharp-stackoverflow/)
