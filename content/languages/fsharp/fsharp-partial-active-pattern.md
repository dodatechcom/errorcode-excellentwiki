---
title: "FSharp PartialActivePattern"
description: "Fix partial active pattern errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1087
---

A partial active pattern error occurs when partial active patterns are not defined correctly.

## Common Causes

- Missing None case in partial active pattern
- Incorrect return type for active pattern
- Using active pattern outside match expression

## How to Fix

Define partial active patterns:

```fsharp
let (|DivisibleBy|_|) n x =
    if x % n = 0 then Some (x / n) else None

let classify x =
    match x with
    | DivisibleBy 3 _ -> "divisible by 3"
    | DivisibleBy 5 _ -> "divisible by 5"
    | _ -> "neither"
```

Use multiple active patterns:

```fsharp
let (|Even|Odd|) n =
    if n % 2 = 0 then Even else Odd
```

## Examples

```fsharp
let (|Positive|Negative|Zero|) x =
    if x > 0 then Positive
    elif x < 0 then Negative
    else Zero

let description =
    match 42 with
    | Positive -> "positive number"
    | Negative -> "negative number"
    | Zero -> "zero"
```

## Related Errors

- [F# MatchFailure](/languages/fsharp/fsharp-match-failure-error)
- [F# PatternWildcard](/languages/fsharp/fsharp-pattern-wildcard-error)
