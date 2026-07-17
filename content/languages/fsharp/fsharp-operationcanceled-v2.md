---
title: "[Solution] F# OperationCanceledException"
description: "Fix F# OperationCanceledException in async workflows. Handle cancellation tokens and graceful shutdown properly."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `OperationCanceledException` occurs when an asynchronous operation is cancelled, typically via a `CancellationToken`. This is normal during application shutdown but can indicate issues if unexpected.

## Common Causes

- CancellationToken triggered during async work
- HttpClient timeout during request
- Task cancelled by caller
- Application shutdown during pending operations
- Missing cancellation handling

## How to Fix

```fsharp
// WRONG: Not handling cancellation
let fetchData url = async {
    let! response = Http.AsyncRequestString(url)  // May throw if cancelled
    return response
}

// CORRECT: Handle cancellation gracefully
let fetchData url = async {
    try
        let! response = Http.AsyncRequestString(url)
        return Some response
    with
    | :? System.OperationCanceledException ->
        return None
}
```

```fsharp
// WRONG: Not passing cancellation token
let longOperation () = async {
    do! Async.Sleep(10000)  // No cancellation check
    return "done"
}

// CORRECT: Use cancellationToken
let longOperation (ct: System.Threading.CancellationToken) = async {
    let! _ = Async.Sleep(10000) |> Async.WithCancellation ct
    return "done"
}
```

```fsharp
// WRONG: Ignoring cancellation in loop
let processItems items = async {
    for item in items do
        do! processItem item  // Won't check cancellation between items
}

// CORRECT: Check cancellation periodically
let processItems (ct: System.Threading.CancellationToken) items = async {
    for item in items do
        ct.ThrowIfCancellationRequested()
        do! processItem item
}
```

## Examples

```fsharp
// Example 1: Async with cancellation
open System.Threading

let asyncWork (ct: CancellationToken) = async {
    try
        for i in 1 .. 100 do
            ct.ThrowIfCancellationRequested()
            do! Async.Sleep(100)
            printfn "Step %d" i
        return "Completed"
    with
    | :? OperationCanceledException ->
        printfn "Operation was cancelled"
        return "Cancelled"
}

// Example 2: Using Async.Start with cancellation
let cts = new CancellationTokenSource()
let work = asyncWork cts.Token
Async.Start(work, cts.Token)
// Later: cts.Cancel()

// Example 3: HttpClient with timeout
let fetchWithTimeout url timeoutMs = async {
    use client = new System.Net.Http.HttpClient()
    client.Timeout <- System.TimeSpan.FromMilliseconds(float timeoutMs)
    try
        let! response = client.GetStringAsync(url) |> Async.AwaitTask
        return Some response
    with
    | :? System.Threading.Tasks.TaskCanceledException ->
        return None
}
```

## Related Errors

- [fsharp-outofmemoryexception]({{< relref "/languages/fsharp/fsharp-outofmemoryexception" >}}) — out of memory
- [fsharp-stackoverflowexception]({{< relref "/languages/fsharp/fsharp-stackoverflowexception" >}}) — stack overflow
- [fsharp-invalidoperation]({{< relref "/languages/fsharp/fsharp-invalidoperation" >}}) — invalid operation
