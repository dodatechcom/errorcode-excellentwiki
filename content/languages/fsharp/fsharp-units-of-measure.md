---
title: "[Solution] F# Units of Measure Mismatch — Dimensional Analysis Error"
description: "Fix F# units of measure mismatch errors. Learn how to define, use, and convert units of measure in F# numeric computations."
languages: ["fsharp"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A units of measure mismatch error occurs when you try to combine values with incompatible units. F# units of measure are compile-time annotations that track dimensional analysis. Adding meters to seconds, or dividing a force by a length without converting units, produces this compile error.

## Why It Happens

The most common cause is performing arithmetic on values with different units. For example, adding a `float<m>` (meters) to a `float<s>` (seconds) is a type error because the units do not match.

Another frequent cause is using the wrong unit in a function parameter. If a function expects `float<kg>` and you pass `float<lb>`, the units do not match even though both are `float` at runtime.

Generic functions that do not have unit constraints may accept values with the wrong units. Without explicit unit annotations, the compiler cannot verify dimensional compatibility.

Unit conversion errors occur when you forget to convert between related units. For example, passing `float<km>` where `float<m>` is expected without multiplying by 1000.

Finally, using `1.0` (unitless) in calculations with measured values can cause unexpected unit propagation. The result may have different units than expected.

## How to Fix It

### Define units explicitly

```fsharp
[<Measure>] type m
[<Measure>] type s
[<Measure>] type kg

let distance: float<m> = 100.0<m>
let time: float<s> = 5.0<s>
let speed: float<m/s> = distance / time
```

### Use unit conversion functions

```fsharp
[<Measure>] type km
[<Measure>] type m

let kilometersToMeters (km: float<km>) : float<m> =
    km * 1000.0<m/km>

let distance = 5.0<km>
let inMeters = kilometersToMeters distance  // 5000.0<m>
```

### Add unit constraints to generic functions

```fsharp
let inline square<[<Measure>] 'u> (x: float<'u>) : float<'u²> =
    x * x

let area = square 3.0<m>  // Returns 9.0<m²>
```

### Handle unitless values carefully

```fsharp
// Use 1.0<_> for unitless multiplication
let scaled: float<m> = 5.0<m> * 1.0<_>
```

### Use runtime units when compile-time units are too restrictive

```fsharp
// When units are not known at compile time
let convert (value: float) (fromUnit: string) (toUnit: string) =
    match fromUnit, toUnit with
    | "m", "km"  -> value / 1000.0
    | "km", "m"  -> value * 1000.0
    | _          -> value
```

## Common Mistakes

- Forgetting that units are erased at runtime and do not affect performance
- Not converting between related units (like meters and kilometers)
- Using `float<m>` when `float<m²>` is needed for area calculations
- Assuming unitless `float` can be used interchangeably with `float<'u>`
- Not using `[<Measure>]` attributes on all unit types

## Related Pages

- [F# TypeMismatch Error](/languages/fsharp/fsharp-type-init-error/)
- [F# Record Type Mismatch](/languages/fsharp/fsharp-record-error/)
- [F# ArgumentException](/languages/fsharp/fsharp-argument-exception/)
