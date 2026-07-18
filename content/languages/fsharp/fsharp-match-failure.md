---
title: "[Solution] F# MatchFailureException — No Matching Pattern in Match Expression"
description: "Fix F# MatchFailureException when no pattern matches. Learn exhaustive pattern matching, wildcard cases, and discriminated union coverage."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `MatchFailureException` is thrown when a `match` expression encounters a value that no case handles. The error message shows the file, line number, and column where the incomplete match is located. F# relies on exhaustive pattern matching and warns at compile time, but runtime matches can still fail.

## Why It Happens

The most frequent cause is a match expression that is not exhaustive. F# issues a warning for incomplete matches, but if warnings are suppressed or the match is on a dynamic value, the error surfaces at runtime.

Another common cause is using `function` syntax without covering all cases. The `function` keyword creates a partial function that only handles the patterns you define. Passing it to a method like `List.iter` that supplies unexpected values triggers the exception.

Pattern matching on discriminated unions without covering all cases is another source. When a new case is added to the union, all existing matches must be updated.

Guard clauses (`when`) can also cause this error. If a pattern matches structurally but the guard condition rejects the value, and there is no fallback case, the match fails.

Finally, matching on `option` types without handling both `Some` and `None` is a frequent oversight that produces this error.

## How to Fix It

### Always include a wildcard case

```fsharp
let describe x =
    match x with
    | 1 -> "one"
    | 2 -> "two"
    | _ -> "other"
```

### Cover all discriminated union cases

```fsharp
type Shape =
    | Circle of float
    | Square of float
    | Rectangle of float * float

let area shape =
    match shape with
    | Circle r          -> 3.14 * r * r
    | Square s          -> s * s
    | Rectangle (w, h)  -> w * h
```

### Handle Option types completely

```fsharp
let processValue opt =
    match opt with
    | Some value -> sprintf "Got: %A" value
    | None       -> "No value"
```

### Use the `function` keyword with all cases

```fsharp
let classify =
    function
    | x when x > 0  -> "positive"
    | x when x < 0  -> "negative"
    | _              -> "zero"
```

### Use `with` for additional matching

```fsharp
let handleResult result =
    match result with
    | Ok value      -> printfn "Success: %A" value
    | Error (ex : System.InvalidOperationException) ->
        printfn "Invalid operation: %s" ex.Message
    | Error ex ->
        printfn "Error: %s" ex.Message
```

## Common Mistakes

- Suppressing F# compiler warnings about incomplete pattern matches
- Adding a new union case without updating all match expressions
- Using `when` guards without a fallback for rejected values
- Not matching on `None` when handling `Option` types
- Assuming `match` on an enum will catch future enum values

## Related Pages

- [F# NullReferenceException](/languages/fsharp/fsharp-nullreference/)
- [F# IndexOutOfRangeException](/languages/fsharp/fsharp-indexoutofrange/)
- [F# Discriminated Union Error](/languages/fsharp/fsharp-discriminated-union/)
