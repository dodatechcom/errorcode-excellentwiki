---
title: "FSharp TaskComputationError"
description: "Fix task computation expression errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1089
---

A task computation expression error occurs when using task {} blocks incorrectly.

## Common Causes

- Missing task CE builder
- Incorrect use of return! in tasks
- Mixing async and task workflows

## How to Fix

Use correct task syntax:

```fsharp
open System.Threading.Tasks

let fetchData = task {
    let! data = HttpClient.GetStringAsync("https://api.example.com")
    return data
}
```

Chain tasks with bind:

```fsharp
let processUser userId = task {
    let! user = getUser userId
    let! orders = getOrders user.Id
    return orders
}
```

## Examples

```fsharp
let computeValue = task {
    do! Task.Delay(100)
    return 42
}

let result = computeValue.Result
```

## Related Errors

- [F# AsyncTimeout](/languages/fsharp/fsharp-async-timeout-error)
- [F# MailboxProcessor](/languages/fsharp/fsharp-mailboxprocessor-error)
