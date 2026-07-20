---
title: "FSharp PatternWildcardError"
description: "Fix pattern wildcard errors in F#."
languages: [F#]
error-types: ["Runtime", "Compile-time"]
severities: [Warning, Error]
weight: 1086
---

A pattern wildcard error occurs when wildcard patterns are used incorrectly in pattern matching.

## Common Causes

- Wildcard in wrong position
- Missing cases before wildcard
- Overly broad wildcard patterns

## How to Fix

Place wildcards at the end:

```fsharp
let describe x =
    match x with
    | 0 -> "zero"
    | n when n > 0 -> "positive"
    | _ -> "negative"  // wildcard catches rest
```

Use named patterns:

```fsharp
let process (value: int) =
    match value with
    | x -> x * 2  // binds to x
```

## Examples

```fsharp
let classify lst =
    match lst with
    | [] -> "empty"
    | [x] -> $"single: {x}"
    | x :: _ -> $"head is {x}"

let result = classify [1; 2; 3]
```

## Related Errors

- [F# MatchFailure](/languages/fsharp/fsharp-match-failure-error)
- [F# IncompletePattern](/languages/fsharp/fsharp-incomplete-pattern-error.md)
