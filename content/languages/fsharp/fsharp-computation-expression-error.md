---
title: "[Solution] F# Computation Expression Error -- Fixing Builder Issues"
description: "Fix F# computation expression errors when custom builders are missing methods or have incorrect signatures."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Computation Expression Error

This error occurs when a computation expression builder does not implement the required methods for the constructs you use.

## Common Causes

- Missing Bind or Return methods on custom builders
- Using async constructs without the async builder
- Incorrect return type on builder methods
- Missing Zero method when using if without else

## How to Fix

### Implement required builder methods

```fsharp
// WRONG: missing Return method
type MyBuilder() =
    member _.Bind(m, f) = f m

let x = myBuilder { return 42 }  // error

// CORRECT: implement Return
type MyBuilder() =
    member _.Bind(m, f) = f m
    member _.Return(x) = x
    member _.Zero() = ()
```

### Add Zero for if-without-else

```fsharp
type LoggingBuilder() =
    member _.Bind(m, f) =
        printfn "Binding"
        f m
    member _.Return(x) = x
    member _.Zero() = ()

let log = LoggingBuilder {
    if true then  // needs Zero
        printfn "yes"
}
```

## Examples

```fsharp
type MaybeBuilder() =
    member _.Bind(x, f) =
        match x with
        | Some v -> f v
        | None -> None
    member _.Return(x) = Some x
    member _.ReturnFrom(x) = x
    member _.Zero() = None

let maybe = MaybeBuilder()

let result = maybe {
    let! a = Some 10
    let! b = Some 20
    return a + b
}
```
