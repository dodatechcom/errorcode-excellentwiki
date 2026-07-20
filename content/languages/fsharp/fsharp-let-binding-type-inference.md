---
title: "FSharp LetBindingTypeInference"
description: "Fix let binding type inference errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1081
---

A let binding type inference error occurs when the compiler cannot infer the type of a binding.

## Common Causes

- Using untyped literals in complex expressions
- Missing type annotations on parameters
- Ambiguous overloaded functions

## How to Fix

Add explicit type annotations:

```fsharp
let numbers: int list = [1; 2; 3]
let add (x: int) (y: int) = x + y
let result: float = 3.14 * 2.0
```

Use typed collections:

```fsharp
let processItems (items: string list) =
    items |> List.map (fun s -> s.Length)
```

## Examples

```fsharp
let greet (name: string) =
    $"Hello, {name}!"

let add x y = x + y
let result = add 5 3  // int inferred
```

## Related Errors

- [F# TypeError](/languages/fsharp/fsharp-type-inference-error)
- [F# OverloadResolution](/languages/fsharp/fsharp-overload-resolution-error)
