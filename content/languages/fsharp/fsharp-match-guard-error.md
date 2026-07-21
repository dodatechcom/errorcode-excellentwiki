---
title: "[Solution] F# Match Guard Error -- Incorrect When Clauses"
description: "Fix F# match guard errors when when clauses in pattern matching are syntactically wrong."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Match Guard Error

This error occurs when `when` guards in match expressions have incorrect syntax or reference unavailable bindings.

## Common Causes

- Missing `when` keyword before guard condition
- Guard expression causing side effects that affect matching
- Using mutable variables in guards that change during matching
- Guard condition evaluating to a non-boolean type

## How to Fix

### Write correct when clauses

```fsharp
// WRONG: missing when keyword
match value with
| x > 10 -> "large"  // syntax error

// CORRECT: use when keyword
match value with
| x when x > 10 -> "large"
| _ -> "small"
```

### Avoid side effects in guards

```fsharp
// WRONG: side effect in guard
let mutable counter = 0
match value with
| x when (counter <- counter + 1; x > 0) -> "positive"

// CORRECT: use separate logic
let result =
    counter <- counter + 1
    match value with
    | x when x > 0 -> "positive"
    | _ -> "non-positive"
```

## Examples

```fsharp
let classify age =
    match age with
    | a when a < 0 -> "invalid"
    | a when a < 18 -> "minor"
    | a when a < 65 -> "adult"
    | _ -> "senior"
```
