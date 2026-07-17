---
title: "MatchFailureException"
description: "A MatchFailureException occurs when a pattern match in a match expression doesn't match the input value."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `MatchFailureException` is thrown when a `match` expression doesn't have a case that matches the input value. F# pattern matching should be exhaustive, but when it isn't, this exception is raised at runtime.

## Common Causes

- Non-exhaustive pattern matching
- Missing wildcard case in match expression
- Not all union cases covered
- Using `with` keyword incorrectly

## How to Fix

```fsharp
// WRONG: Missing case for 3
let describe x =
    match x with
    | 1 -> "one"
    | 2 -> "two"
    // MatchFailureException if x = 3

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
    // MatchFailureException for Square

// CORRECT: Cover all cases
let area shape =
    match shape with
    | Circle r -> 3.14 * r * r
    | Square s -> s * s
```

## Examples

```fsharp
// Example 1: Integer match
let getValue x =
    match x with
    | 0 -> "zero"
    | 1 -> "one"
    // MatchFailureException for x = 2

// Example 2: List match
let head lst =
    match lst with
    | x :: xs -> x
    // MatchFailureException for empty list

// Example 3: Option match
let unwrap opt =
    match opt with
    | Some x -> x
    // MatchFailureException for None
```

## Related Errors

- [NullReferenceException](/languages/fsharp/null-reference5)
- [IndexOutOfRangeException](/languages/fsharp/index-out-of-range)
