---
title: "FSharp UnitTypeMismatch"
description: "Fix unit type mismatch errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1082
---

A unit type mismatch error occurs when a function returns unit but a value is expected.

## Common Causes

- Using mutable assignment in expression context
- Calling void-returning functions in pipelines
- Returning unit from functions expecting a value

## How to Fix

Ensure correct return types:

```fsharp
let logMessage (msg: string) =
    printfn "%s" msg
    ()  // explicit unit return
```

Use ignore for side effects:

```fsharp
[1; 2; 3] |> List.iter (fun x -> printfn "%d" x) |> ignore
```

## Examples

```fsharp
let mutable counter = 0
let increment () = counter <- counter + 1  // returns unit
let value = increment ()  // value is unit
```

## Related Errors

- [F# TypeError](/languages/fsharp/fsharp-type-inference-error)
- [F# LetBinding](/languages/fsharp/fsharp-let-binding-type-inference.md)
