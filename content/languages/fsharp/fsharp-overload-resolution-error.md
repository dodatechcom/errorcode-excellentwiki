---
title: "FSharp OverloadResolutionError"
description: "Fix overload resolution errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1120
---

An overload resolution error occurs when the compiler cannot choose between overloaded methods.

## Common Causes

- Multiple matching overloads with similar signatures
- Missing type information to disambiguate
- Generic overloads with overlapping constraints

## How to Fix

Provide explicit type information:

```fsharp
let result = System.Convert.ToInt32(42.0 :> obj)
```

Use type annotations to resolve:

```fsharp
let processValue (x: int) = x * 2
let processValue (x: float) = x * 2.0

let result = processValue (42 : int)  // explicit type
```

## Examples

```fsharp
let toString (x: obj) =
    match x with
    | :? int as n -> string n
    | :? float as f -> string f
    | :? string as s -> s
    | _ -> x.ToString()
```

## Related Errors

- [F# ResolveType](/languages/fsharp/fsharp-resolve-type-error)
- [F# LetBinding](/languages/fsharp/fsharp-let-binding-type-inference)
