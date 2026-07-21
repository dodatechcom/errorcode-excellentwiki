---
title: "[Solution] F# Discriminated Union Error -- Missing Pattern Match Cases"
description: "Fix F# discriminated union errors when pattern matching does not cover all union cases."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["warning"]
---

# F# Discriminated Union Error

This warning occurs when a match expression does not handle every case of a discriminated union, which can lead to match failures at runtime.

## Common Causes

- Omitting cases from a pattern match on a discriminated union
- Using a wildcard `_` that silently hides uncovered cases
- Adding new union cases without updating all match expressions
- Incorrectly ordered patterns where a wildcard catches everything

## How to Fix

### Cover all cases explicitly

```fsharp
type Shape =
    | Circle of float
    | Rectangle of float * float
    | Triangle of float * float * float

// WARNING: not all cases covered
let area shape =
    match shape with
    | Circle r -> System.Math.PI * r * r
    | Rectangle (w, h) -> w * h

// CORRECT: handle all cases
let area shape =
    match shape with
    | Circle r -> System.Math.PI * r * r
    | Rectangle (w, h) -> w * h
    | Triangle (a, b, c) ->
        let s = (a + b + c) / 2.0
        sqrt (s * (s - a) * (s - b) * (s - c))
```

## Examples

```fsharp
type Result<'T, 'E> =
    | Ok of 'T
    | Error of 'E

let describe = function
    | Ok value -> sprintf "Success: %A" value
    | Error err -> sprintf "Failed: %A" err
```
