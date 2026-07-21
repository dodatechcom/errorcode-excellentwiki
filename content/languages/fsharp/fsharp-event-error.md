---
title: "[Solution] F# Event Error -- Incorrect Event Handling"
description: "Fix F# event errors when subscribing to, raising, or unsubscribing from .NET events."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Event Error

This error occurs when event subscription, raising, or unsubscription is performed incorrectly.

## Common Causes

- Using `=` instead of `<-` for event subscription
- Forgetting to unsubscribe from events causing memory leaks
- Raising events from wrong thread context
- Not using the `[<CLIEvent>]` attribute on F# events

## How to Fix

### Subscribe with correct syntax

```fsharp
// WRONG: incorrect subscription
button.Click += handler  // may cause type issues

// CORRECT: use <- operator
button.Click.Add handler
// or
button.Click.Subscribe(handler) |> ignore
```

### Unsubscribe properly

```fsharp
let subscriber =
    button.Click.Subscribe(fun args ->
        printfn "Clicked at %A" args.Timestamp)

// Later, to unsubscribe
subscriber.Dispose()
```

## Examples

```fsharp
type Timer() =
    let tickEvent = Event<unit>()

    [<CLIEvent>]
    member _.Tick = tickEvent.Publish

    member this.Start() =
        let timer = new System.Timers.Timer(1000.0)
        timer.Elapsed.Add(fun _ -> tickEvent.Trigger())
        timer.Start()
```
