---
title: "FSharp RecordFieldError"
description: "Fix record field access errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1084
---

A record field error occurs when accessing non-existent or mistyped record fields.

## Common Causes

- Typo in field name
- Accessing field on wrong record type
- Using dot notation on non-record types

## How to Fix

Define records with clear fields:

```fsharp
type Person = { Name: string; Age: int }
let person = { Name = "Alice"; Age = 30 }
printfn "%s" person.Name
```

Update records immutably:

```fsharp
let updated = { person with Age = 31 }
```

## Examples

```fsharp
type Score = { Player: string; Points: int }
let scores = [
    { Player = "Alice"; Points = 100 }
    { Player = "Bob"; Points = 85 }
]
let topScore = scores |> List.maxBy (fun s -> s.Points)
```

## Related Errors

- [F# TypeError](/languages/fsharp/fsharp-type-inference-error)
- [F# AccessControl](/languages/fsharp/fsharp-access-control-error)
