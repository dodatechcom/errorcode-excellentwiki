---
title: "[Solution] F# MatchFailureException Match Failed"
description: "Fix F# MatchFailureException when pattern match doesn't cover all cases. Make matches exhaustive with wildcard defaults."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["match", "pattern", "failure", "matchfailureexception", "fsharp"]
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

```fsharp
// WRONG: Missing default case
let describe x =
    match x with
    | 1 -> "one"
    | 2 -> "two"
// MatchFailureException for x = 3

// CORRECT: Add wildcard case
let describe x =
    match x with
    | 1 -> "one"
    | 2 -> "two"
    | _ -> "other"
```

```fsharp
// WRONG: Not all union cases covered
type Shape = Circle of float | Square of float

let area shape =
    match shape with
    | Circle r -> 3.14 * r * r
// Missing: Square case

// CORRECT: Cover all cases
let area shape =
    match shape with
    | Circle r -> 3.14 * r * r
    | Square s -> s * s
```

```fsharp
// WRONG: Using function keyword without all cases
let classify = function
    | x when x > 0 -> "positive"
// Missing: x <= 0 case

// CORRECT: Use function keyword with all cases
let classify = function
    | x when x > 0 -> "positive"
    | x when x < 0 -> "negative"
    | _ -> "zero"
```

## Examples

```fsharp
// Example 1: Match with Option type
let processOption opt =
    match opt with
    | Some value -> printfn "Got: %A" value
    | None -> printfn "Nothing"

// Example 2: Nested pattern matching
let describePoint (x, y) =
    match x, y with
    | 0, 0 -> "origin"
    | _, 0 -> "on x-axis"
    | 0, _ -> "on y-axis"
    | _ -> "quadrant"

// Example 3: Active patterns
let (|Even|Odd|) n = if n % 2 = 0 then Even else Odd

let classify n =
    match n with
    | Even -> "even"
    | Odd -> "odd"
```

## Related Errors

- [fsharp-nullreference]({{< relref "/languages/fsharp/fsharp-nullreference" >}}) — null reference
- [fsharp-indexoutofrange]({{< relref "/languages/fsharp/fsharp-indexoutofrange" >}}) — index out of range
- [fsharp-notfoundexception]({{< relref "/languages/fsharp/fsharp-notfoundexception" >}}) — key not found
