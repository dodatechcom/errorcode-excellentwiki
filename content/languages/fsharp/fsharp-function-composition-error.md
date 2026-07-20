---
title: "FSharp FunctionCompositionError"
description: "Fix function composition errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1096
---

A function composition error occurs when composing functions with incompatible types.

## Common Causes

- Output type of first function doesn't match input of second
- Wrong number of arguments in composed functions
- Type inference failures in composition chains

## How to Fix

Compose functions with matching types:

```fsharp
let addOne x = x + 1
let double x = x * 2
let addOneThenDouble = addOne >> double
let result = addOneThenDouble 5  // 12
```

Use << for reverse composition:

```fsharp
let doubleThenAddOne = double << addOne
```

## Examples

```fsharp
let process =
    (fun s -> s.Trim())
    >> (fun s -> s.ToLower())
    >> (fun s -> s.Replace(" ", "_"))

let result = process "  Hello World  "
```

## Related Errors

- [F# FunctionCurrying](/languages/fsharp/fsharp-function-currying-error)
- [F# PartialApplication](/languages/fsharp/fsharp-partial-application-error)
