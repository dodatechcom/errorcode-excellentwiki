---
title: "FSharp MailboxProcessorError"
description: "Fix MailboxProcessor errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1109
---

A MailboxProcessor error occurs when using the mailbox actor model incorrectly.

## Common Causes

- Not starting the mailbox processor
- Incorrect message handling patterns
- Memory leaks from unprocessed messages

## How to Fix

Create a mailbox processor:

```fsharp
let agent = MailboxProcessor.Start(fun inbox ->
    let rec loop () = async {
        let! msg = inbox.Receive()
        printfn "Received: %s" msg
        return! loop ()
    }
    loop ())

agent.Post "hello"
```

Handle different message types:

```fsharp
type Message =
    | Process of string
    | Shutdown

let agent = MailboxProcessor.Start(fun inbox ->
    let rec loop () = async {
        let! msg = inbox.Receive()
        match msg with
        | Process s -> printfn "Processing: %s" s
        | Shutdown -> return ()
        return! loop ()
    }
    loop ())
```

## Examples

```fsharp
let counter = MailboxProcessor.Start(fun inbox ->
    let mutable count = 0
    let rec loop () = async {
        let! _ = inbox.Receive()
        count <- count + 1
        printfn "Count: %d" count
        return! loop ()
    }
    loop ())
```

## Related Errors

- [F# PostAndReply](/languages/fsharp/fsharp-postandreply-error)
- [F# MailboxProcessorScan](/languages/fsharp/fsharp-mailboxprocessor-scan-error)
