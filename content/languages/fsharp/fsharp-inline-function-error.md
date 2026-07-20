---
title: "FSharp InlineFunctionError"
description: "Fix inline function errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1102
---

An inline function error occurs when using the inline keyword incorrectly.

## Common Causes

- Inline function with mutable local bindings
- Recursive inline without tail recursion
- Inlining functions with closures over mutable state

## How to Fix

Use inline for generic functions:

```fsharp
let inline add x y = x + y
let result = add 5 3      // int
let result2 = add 3.14 2.0  // float
```

Avoid inline with complex closures:

```fsharp
let inline process x = x * 2  // OK
// let inline complex x = let mutable m = x in ...  // Problematic
```

## Examples

```fsharp
let inline square (x: ^a) = x * x
let inline clamp min max value =
    if value < min then min
    elif value > max then max
    else value
```

## Related Errors

- [F# TailCall](/languages/fsharp/fsharp-tail-call-error)
- [F# FunctionCurrying](/languages/fsharp/fsharp-function-currying-error)
