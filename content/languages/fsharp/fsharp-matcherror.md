---
title: "MatchFailureException in F#"
description: "F# raises MatchFailureException when a pattern match expression doesn't match the input value"
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `MatchFailureException` is thrown when a `match` expression doesn't have a case that matches the input value. F# pattern matching should be exhaustive.

## Common Causes

- Non-exhaustive pattern matching
- Missing wildcard case in match expression
- Not all union cases covered
- Using `with` keyword incorrectly

## How to Fix

Add wildcard case:

```fsharp
let describe x =
    match x with
    | 1 -> "one"
    | 2 -> "two"
    | _ -> "other"
```

Cover all union cases:

```fsharp
type Shape = Circle of float | Square of float

let area shape =
    match shape with
    | Circle r -> 3.14 * r * r
    | Square s -> s * s
```

Use `function` keyword with all cases:

```fsharp
let classify = function
    | x when x > 0 -> "positive"
    | x when x < 0 -> "negative"
    | _ -> "zero"
```

## Examples

```fsharp
let getValue x =
    match x with
    | 0 -> "zero"
    | 1 -> "one"
// MatchFailureException for x = 2
```

## Related Errors

- [NullReferenceException]({{< relref "/languages/fsharp/null-reference5" >}})
- [IndexOutOfRangeException]({{< relref "/languages/fsharp/index-out-of-range" >}})
