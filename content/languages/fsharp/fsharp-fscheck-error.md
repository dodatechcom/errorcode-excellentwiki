---
title: "FSharp FsCheckError"
description: "Fix FsCheck property-based testing errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1112
---

An FsCheck error occurs when writing property-based tests incorrectly.

## Common Causes

- Property doesn't hold for all generated inputs
- Missing Arb override for custom types
- Incorrect property definition

## How to Fix

Define correct properties:

```fsharp
open FsCheck

let reverseReverseIsIdentity (xs: int list) =
    xs |> List.rev |> List.rev = xs

Check.Quick reverseReverseIsIdentity
```

Use custom generators:

```fsharp
let nonNegativeInts =
    Arb.from<int>
    |> Arb.mapFilter (fun n -> abs n) (fun n -> n >= 0)
```

## Examples

```fsharp
let sortIdempotent (xs: int list) =
    let sorted = xs |> List.sort
    sorted |> List.sort = sorted

let sortPreservesLength (xs: int list) =
    (xs |> List.sort |> List.length) = xs.Length
```

## Related Errors

- [F# Expecto](/languages/fsharp/fsharp-expecto-error)
- [F# UnitTypeMismatch](/languages/fsharp/fsharp-unit-type-mismatch)
