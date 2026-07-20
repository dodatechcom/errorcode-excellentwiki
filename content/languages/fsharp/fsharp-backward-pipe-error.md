---
title: "FSharp BackwardPipeError"
description: "Fix backward pipe operator errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1095
---

A backward pipe error occurs when using the <| operator incorrectly.

## Common Causes

- Confusing <| with <|>
- Wrong argument placement
- Using backward pipe unnecessarily

## How to Fix

Use backward pipe for readability:

```fsharp
let result = List.map (fun x -> x * 2) <| [1; 2; 3]
```

Avoid when forward pipe is clearer:

```fsharp
// Prefer this:
[1; 2; 3] |> List.map (fun x -> x * 2)
// Over this:
List.map (fun x -> x * 2) <| [1; 2; 3]
```

## Examples

```fsharp
let config =
    { defaultConfig with
        Timeout = 5000
    } <| fun cfg -> { cfg with Retries = 3 }
```

## Related Errors

- [F# ForwardPipe](/languages/fsharp/fsharp-forward-pipe-error)
- [F# FunctionComposition](/languages/fsharp/fsharp-function-composition-error)
