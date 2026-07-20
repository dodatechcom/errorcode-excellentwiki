---
title: "FSharp ChoiceTypeError"
description: "Fix Choice type errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1108
---

A Choice type error occurs when working with Choice<'T1,'T2> types incorrectly.

## Common Causes

- Mismatched Choice cases
- Missing pattern match arms for all cases
- Confusing Choice with discriminated unions

## How to Fix

Define and match Choice types:

```fsharp
let processResult result =
    match result with
    | Choice1Of2 value -> $"Success: {value}"
    | Choice2Of2 error -> $"Error: {error}"
```

Convert between types:

```fsharp
let toChoice (result: Result<'a, 'b>) =
    match result with
    | Ok x -> Choice1Of2 x
    | Error e -> Choice2Of2 e
```

## Examples

```fsharp
let divide x y =
    if y = 0 then Choice2Of2 "Division by zero"
    else Choice1Of2 (x / y)

let result = divide 10 2
let message = processResult result
```

## Related Errors

- [F# ResultBind](/languages/fsharp/fsharp-result-bind-error)
- [F# OptionBind](/languages/fsharp/fsharp-option-bind-error)
