---
title: "FSharp StructUnionError"
description: "Fix struct discriminated union errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1117
---

A struct union error occurs when using [<Struct>] attribute on discriminated unions incorrectly.

## Common Causes

- Struct union with reference type fields
- Missing StructLayout attribute
- Incompatible struct union patterns

## How to Fix

Define struct unions correctly:

```fsharp
[<Struct>]
type Shape =
    | Circle of radius: float
    | Rectangle of width: float * height: float
```

Use for performance-critical code:

```fsharp
[<Struct>]
type Point = { X: float; Y: float }

[<Struct>]
type Option<'T> =
    | Some of 'T
    | None
```

## Examples

```fsharp
[<Struct>]
type Distance =
    | Meters of float
    | Kilometers of float
    | Miles of float

let toMeters (d: Distance) =
    match d with
    | Meters m -> m
    | Kilometers k -> k * 1000.0
    | Miles m -> m * 1609.344
```

## Related Errors

- [F# RecordField](/languages/fsharp/fsharp-record-field-error)
- [F# PatternWildcard](/languages/fsharp/fsharp-pattern-wildcard-error)
