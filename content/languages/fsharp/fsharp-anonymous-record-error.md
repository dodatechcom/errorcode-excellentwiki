---
title: "FSharp AnonymousRecordError"
description: "Fix anonymous record errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1085
---

An anonymous record error occurs when using anonymous records incorrectly.

## Common Causes

- Mismatched anonymous record structure
- Missing required fields
- Incorrect anonymous record syntax

## How to Fix

Use correct anonymous record syntax:

```fsharp
let person = {| Name = "Alice"; Age = 30 |}
printfn "%s" person.Name
```

Pass anonymous records to functions:

```fsharp
let printInfo (info: {| Name: string; Age: int |}) =
    printfn "%s is %d" info.Name info.Age
```

## Examples

```fsharp
let data = {| X = 1; Y = 2; Z = 3 |}
let sum = data.X + data.Y + data.Z

let transform (r: {| Name: string |}) =
    {| r with Upper = r.Name.ToUpper() |}
```

## Related Errors

- [F# RecordField](/languages/fsharp/fsharp-record-field-error)
- [F# TypeError](/languages/fsharp/fsharp-type-inference-error)
