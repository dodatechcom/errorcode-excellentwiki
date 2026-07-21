---
title: "[Solution] F# Struct Error -- Value Type Limitations"
description: "Fix F# struct errors when working with value types, including boxing, inheritance, and field constraints."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Struct Error

This error arises when F# structs are defined or used incorrectly, such as violating constraints on value types.

## Common Causes

- Structs cannot have default parameterless constructors
- Attempting to use discriminated unions as struct fields
- Structs do not support inheritance or interface implementations without [<Interface>]
- Mutability issues with struct copies

## How to Fix

### Define structs correctly

```fsharp
// WRONG: struct with default constructor
[<Struct>]
type Point() =     // error: cannot have parameterless constructor
    member val X = 0.0
    member val Y = 0.0

// CORRECT: use primary constructor with parameters
[<Struct>]
type Point(x: float, y: float) =
    member val X = x
    member val Y = y
```

### Handle struct boxing

```fsharp
[<Struct>]
type Vec2(x: float, y: float) =
    member val X = x
    member val Y = y

let v = Vec2(1.0, 2.0)
let boxed: obj = box v  // may box to heap
let unboxed: Vec2 = unbox boxed
```

## Examples

```fsharp
[<Struct>]
type Range(start: int, finish: int) =
    member val Start = start
    member val Finish = finish
    member this.Contains value =
        value >= start && value <= finish
```
