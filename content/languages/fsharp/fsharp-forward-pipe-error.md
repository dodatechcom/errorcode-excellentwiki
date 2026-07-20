---
title: "FSharp ForwardPipeError"
description: "Fix forward pipe errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1094
---

A forward pipe error occurs when using the |> operator with incompatible function signatures.

## Common Causes

- Function expects wrong number of arguments
- Pipeline breaks due to type changes
- Missing intermediate transformations

## How to Fix

Chain compatible functions:

```fsharp
let result =
    [1; 2; 3]
    |> List.map (fun x -> x * 2)
    |> List.filter (fun x -> x > 3)
```

Use flip for argument order:

```fsharp
let flip f a b = f b a
let result = data |> flip Map.add "key" value
```

## Examples

```fsharp
let processNumbers =
    [5; 3; 8; 1; 9]
    |> List.sort
    |> List.rev
    |> List.take 3
    |> List.sum
```

## Related Errors

- [F# PipelineOperator](/languages/fsharp/fsharp-pipeline-operator-error)
- [F# BackwardPipe](/languages/fsharp/fsharp-backward-pipe-error)
