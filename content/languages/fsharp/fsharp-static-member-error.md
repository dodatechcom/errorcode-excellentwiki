---
title: "[Solution] F# Static Member Error -- Invalid Static Definitions"
description: "Fix F# static member errors when defining or calling static members on types incorrectly."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Static Member Error

This error occurs when static members are defined or invoked incorrectly on F# types.

## Common Causes

- Calling static members without the type name
- Defining static members without the `static` keyword
- Using instance member syntax for static methods
- Missing `member _.` syntax for computed properties

## How to Fix

### Use correct static member syntax

```fsharp
// WRONG: missing static keyword
type Calculator =
    member Add a b = a + b  // instance, not static

// CORRECT: add static keyword
type Calculator =
    static member Add(a, b) = a + b

// Call with type name
let result = Calculator.Add(2, 3)
```

### Use static members on modules

```fsharp
module MathHelpers =
    let inline square (x: ^T) =
        (^T: (static member (*): ^T * ^T -> ^T) (x, x))
```

## Examples

```fsharp
type Point =
    { X: float; Y: float }
    static member Origin = { X = 0.0; Y = 0.0 }
    static member Distance(a, b) =
        sqrt ((a.X - b.X) ** 2 + (a.Y - b.Y) ** 2)

let origin = Point.Origin
let dist = Point.Distance(origin, { X = 3.0; Y = 4.0 })
```
