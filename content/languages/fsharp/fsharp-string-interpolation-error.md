---
title: "FSharp StringInterpolationError"
description: "Fix F# string interpolation errors."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1118
---

A string interpolation error occurs when using interpolation strings incorrectly in F#.

## Common Causes

- Missing dollar sign prefix for interpolation
- Wrong format specifiers in interpolated strings
- Escaping issues in interpolated expressions

## How to Fix

Use correct interpolation syntax:

```fsharp
let name = "Alice"
let age = 30
printfn $"Name: {name}, Age: {age}"
```

Use formatted interpolation:

```fsharp
printfn $"Value: {42}"  // "Value: 42"
printfn $"Percent: {0.75}"  // "Percent: 0.75"
```

## Examples

```fsharp
let processUser (name: string) (age: int) =
    let msg = $"User {name} is {age} years old"
    printfn "%s" msg

processUser "Alice" 30
```

## Related Errors

- [F# FormatException](/languages/fsharp/fsharp-formatexception)
- [F# TypeError](/languages/fsharp/fsharp-type-inference-error)
