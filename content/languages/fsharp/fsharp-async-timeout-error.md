---
title: "FSharp AsyncTimeoutError"
description: "Fix async timeout errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1088
---

An async timeout error occurs when async operations take too long or hang.

## Common Causes

- No timeout specified on async operations
- Deadlocks in async workflows
- Missing cancellation tokens

## How to Fix

Add timeouts to async operations:

```fsharp
open System.Threading

let withTimeout timeoutMs operation =
    async {
        let! ct = Async.CancellationToken
        use timer = new CancellationTokenSource(timeoutMs)
        return! Async.StartChild(operation, timeoutMs)
    } |> Async.RunSynchronously
```

Use Async.Choice for timeout:

```fsharp
let withTimeout operation timeoutMs =
    let timeout = async {
        do! Async.Sleep timeoutMs
        return None
    }
    Async.Choice [ operation |> Async.map Some; timeout ]
```

## Examples

```fsharp
let longOperation = async {
    do! Async.Sleep 5000
    return "done"
}

let result =
    longOperation
    |> Async.withTimeout 1000
    |> Async.RunSynchronously
```

## Related Errors

- [F# TaskComputation](/languages/fsharp/fsharp-task-computation-error)
- [F# MailboxProcessor](/languages/fsharp/fsharp-mailboxprocessor-error)
