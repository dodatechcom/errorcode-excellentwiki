---
title: "[Solution] F# Overloaded Function Error -- Ambiguous Call Resolution"
description: "Fix F# overloaded function errors when the compiler cannot resolve which overloaded member to call."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Overloaded Function Error

This error occurs when a call to an overloaded function is ambiguous and the compiler cannot determine the correct overload.

## Common Causes

- Calling .NET methods with multiple overloads without type annotation
- Implicit conversions not available in F# for overload resolution
- Using generic methods where type inference is insufficient
- Mixing value types and reference types in overload candidates

## How to Fix

### Provide explicit type annotations

```fsharp
// WRONG: ambiguous overload
let result = Seq.length [1;2;3]  // OK but...

let parsed = System.Int32.Parse("42")  // may be ambiguous

// CORRECT: annotate to guide resolution
let parsed : int = System.Int32.Parse("42")
```

### Use explicit casts

```fsharp
let value = box 42 :?> int
let text = value.ToString()
```

## Examples

```fsharp
open System

let parseValue (s: string) : int =
    Int32.Parse(s, Globalization.NumberStyles.Integer)

let formatValue (n: int) : string =
    n.ToString("N0")
```
