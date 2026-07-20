---
title: "FSharp PipelineOperatorError"
description: "Fix pipeline operator errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1093
---

A pipeline operator error occurs when using the |> operator incorrectly.

## Common Causes

- Wrong argument order for piped functions
- Missing parentheses in pipeline chains
- Type mismatches between pipeline stages

## How to Fix

Ensure functions accept last parameter:

```fsharp
let result =
    [1; 2; 3; 4; 5]
    |> List.filter (fun x -> x > 2)
    |> List.map (fun x -> x * 10)
```

Use parentheses for multi-argument functions:

```fsharp
let result =
    data
    |> List.fold (fun acc x -> acc + x) 0
```

## Examples

```fsharp
let processText =
    "Hello World"
    |> fun s -> s.ToLower()
    |> fun s -> s.Split(' ')
    |> Array.map (fun s -> s.Length)
    |> Array.sum
```

## Related Errors
n- [F# FunctionComposition](/languages/fsharp/fsharp-function-composition-error)
- [F# ForwardPipe](/languages/fsharp/fsharp-forward-pipe-error)
