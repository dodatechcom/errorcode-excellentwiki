---
title: "[Solution] F# Measure Error -- Unit of Measure Mismatch"
description: "Fix F# unit of measure errors when incompatible physical units are combined in expressions."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Measure Error

This error occurs when values with incompatible units of measure are used together in an expression.

## Common Causes

- Adding values with different units (e.g., meters + seconds)
- Forgetting to annotate literal values with their unit
- Using unmeasured literals where measured values are expected
- Missing `[<Measure>]` annotations on type definitions

## How to Fix

### Annotate literals

```fsharp
[<Measure>] type m
[<Measure>] type s

// WRONG: int literal not annotated
let distance: float<m> = 10.0 + 5.0  // OK, but...

// WRONG: mixing units
let speed: float<m/s> = 10.0<m> + 5.0<s>  // error

// CORRECT: matching units
let combined: float<m> = 10.0<m> + 5.0<m>
```

### Use conversion functions

```fsharp
[<Measure>] type km
[<Measure>] type m

let kmToM (x: float<km>) : float<m> = x * 1000.0<m/km>
```

## Examples

```fsharp
[<Measure>] type kg
[<Measure>] type m
[<Measure>] type s

let force (mass: float<kg>) (accel: float<m/s^2>) : float<kg*m/s^2> =
    mass * accel

let weight = force 10.0<kg> 9.81<m/s^2>
```
