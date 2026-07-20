---
title: "FSharp MailboxProcessorScanError"
description: "Fix MailboxProcessor.Scan errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1111
---

A MailboxProcessor.Scan error occurs when using the Scan method incorrectly.

## Common Causes

- Scan function doesn't match expected messages
- Missing catch-all pattern in scan
- Incorrect scan function return type

## How to Fix

Use Scan for selective processing:

```fsharp
let agent = MailboxProcessor.Start(fun inbox ->
    let rec loop () = async {
        let! msg =
            inbox.Scan(fun msg ->
                match msg with
                | :? string as s when s.StartsWith("important") ->
                    Some (async {
                        printfn "Important: %s" s
                    })
                | _ -> None)
        return! loop ()
    }
    loop ())
```

Handle multiple message types:

```fsharp
inbox.Scan(function
    | :? int as n -> Some (async { processNumber n })
    | :? string as s -> Some (async { processString s })
    | _ -> None)
```

## Examples

```fsharp
let dispatcher = MailboxProcessor.Start(fun inbox ->
    let rec loop () = async {
        let! handler = inbox.Scan(function
            | :? PingMsg -> Some (async { printfn "Pong!" })
            | :? DataMsg d -> Some (async { processData d })
            | _ -> None)
        return! loop ()
    }
    loop ())
```

## Related Errors

- [F# MailboxProcessor](/languages/fsharp/fsharp-mailboxprocessor-error)
- [F# PatternWildcard](/languages/fsharp/fsharp-pattern-wildcard-error)
