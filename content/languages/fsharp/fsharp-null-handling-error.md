---
title: "FSharp NullHandlingError"
description: "Fix null handling errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1105
---

A null handling error occurs when dealing with null values incorrectly in F#.

## Common Causes

- Using null in F# code instead of Option type
- Comparing F# types with null
- Missing null checks on .NET interop values

## How to Fix

Use Option type instead of null:

```fsharp
let findItem id =
    if id > 0 then Some { Id = id }
    else None
```

Handle null from .NET:

```fsharp
let safeString (s: string) =
    if isNull s then "" else s
```

## Examples

```fsharp
let processValue (value: string option) =
    match value with
    | Some v when not (isNull v) -> v.Length
    | _ -> 0

let result = processValue (Some "hello")
```

## Related Errors

- [F# OptionBind](/languages/fsharp/fsharp-option-bind-error)
- [F# DotNetInterop](/languages/fsharp/fsharp-dotnet-interop-error)
