---
title: "[Solution] F# Units of Measure Error — How to Fix"
description: "Fix F# units of measure errors. Learn how to define, use, and convert units of measure for type-safe numerical computations in your F# projects."
languages: ["fsharp"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

F# units of measure allow you to attach physical units (like meters, seconds, or kilograms) to numeric types for compile-time dimensional analysis. When the units do not match or the measure definitions are incorrect, the compiler raises an error.

The most common cause is performing operations with incompatible units. Adding a value measured in meters to a value measured in seconds is a type error because the units do not match.

Another frequent cause is missing unit annotations on values. If a function returns a `float` without a unit annotation, the result cannot participate in unit-checked calculations.

Unit conversion errors occur when you try to assign a value with one unit to a variable with a different unit. The compiler prevents this because the units are part of the type.

Complex unit expressions that result in dimensionally inconsistent types cause errors. For example, dividing a `float<meter>` by a `float<second>` gives `float<meter/second>`, but assigning that to a `float<meter>` variable fails.

Measure definitions that reference undefined measures cause errors. If you define `[<Measure>] type velocity = meter / second` but `meter` and `second` are not defined, the compilation fails.

Generic code that does not account for units of measure may fail when used with measured types. The type parameter `'T` in a generic function cannot be substituted with `float<meter>` if the function performs operations that assume unitless numbers.

## Common Error Messages

```
error FS0001: The type 'float<meter>' does not match the type 'float<second>'
```

```
error FS0039: The type 'meter' is not defined in this unit of measure
```

```
error FS0001: This expression was expected to have type 'float' but here has type 'float<meter>'
```

```
error FS0001: Units of measure mismatch: expected 'float<meter>' but got 'float<second>'
```

## How to Fix It

### Define units of measure correctly

```fsharp
[<Measure>] type meter
[<Measure>] type second
[<Measure>] type kilogram

// Compound units
[<Measure>] type newton = kilogram * meter / second^2
[<Measure>] type joule = newton * meter
[<Measure>] type watt = joule / second
```

### Annotate values with their units

```fsharp
let distance: float<meter> = 100.0<meter>
let time: float<second> = 9.58<second>
let speed: float<meter/second> = distance / time
```

### Convert between compatible units

```fsharp
[<Measure>] type foot
[<Measure>] type inch

let footToInch (f: float<foot>) : float<inch> = f * 12.0<inch/foot>

let myHeight: float<foot> = 6.0<foot>
let heightInInches: float<inch> = footToInch myHeight
```

### Handle unit-generic functions

```fsharp
// Unit-generic function
let square (x: float<'u>) : float<'u^2> = x * x

let area: float<meter^2> = square 5.0<meter>

// Multiple type parameters with units
let distanceRatio (d1: float<'u>) (d2: float<'u>) : float = d1 / d2
```

### Use measure abbreviations for convenience

```fsharp
[<Measure>] type m    // meter
[<Measure>] type s    // second
[<Measure>] type kg   // kilogram

let velocity: float<m/s> = 9.8<m/s>
let mass: float<kg> = 75.0<kg>
let force: float<kg*m/s^2> = mass * velocity / 1.0<s>
```

## Common Scenarios

- Building a physics simulation that requires dimensional analysis
- Creating financial calculations with currency units
- Writing scientific computing code that needs to track units through calculations

## Prevent It

- Always annotate numeric values with their units when working with dimensional quantities
- Define all required measures before using them in type annotations
- Use unit-generic functions to write reusable code that works with any unit system
