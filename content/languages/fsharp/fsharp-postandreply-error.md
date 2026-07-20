---
title: "FSharp PostAndReplyError"
description: "Fix PostAndReply errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1110
---

A PostAndReply error occurs when using synchronous mailbox replies incorrectly.

## Common Causes

- Not implementing reply channel handling
- Deadlocks from blocking calls
- Missing reply in match cases

## How to Fix

Use PostAndReply correctly:

```fsharp
let agent = MailboxProcessor.Start(fun inbox ->
    let rec loop () = async {
        let! (reply: AsyncReplyChannel<_>, msg) = inbox.Receive()
        reply.Reply($"Processed: {msg}")
        return! loop ()
    }
    loop ())

let result = agent.PostAndReply(fun reply -> (reply, "hello"))
```

Use timeout:

```fsharp
let result =
    agent.PostAndReply(
        (fun reply -> (reply, "query")),
        timeout = 5000)
```

## Examples

```fsharp
let queryAgent = MailboxProcessor.Start(fun inbox ->
    let mutable state = Map.empty
    let rec loop () = async {
        let! (reply, key, value) = inbox.Receive()
        state <- Map.add key value state
        reply.Reply(state)
        return! loop ()
    }
    loop ())
```

## Related Errors

- [F# MailboxProcessor](/languages/fsharp/fsharp-mailboxprocessor-error)
- [F# AsyncTimeout](/languages/fsharp/fsharp-async-timeout-error)
