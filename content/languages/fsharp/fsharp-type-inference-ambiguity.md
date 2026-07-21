---
title: "[Solution] F# Type Inference Ambiguity Error -- Conflicting Type Hints"
description: "Fix F# type inference ambiguity when the compiler cannot resolve conflicting type hints in expressions."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Type Inference Ambiguity Error

This error occurs when the F# type inference algorithm encounters conflicting constraints and cannot determine a unique type.

## Common Causes

- Multiple possible types for a polymorphic value in the same expression
- Mixing numeric literals with ambiguous types
- Using operators that work on multiple types without annotation
- Generic functions receiving conflicting type constraints

## How to Fix

### Add type annotations to resolve ambiguity

```fsharp
// WRONG: compiler cannot decide between int and float
let result = [1; 2; 3] |> List.average  // error: average requires float

// CORRECT: use float list explicitly
let result = [1.0; 2.0; 3.0] |> List.average
```

### Use type annotation at binding

```fsharp
let numbers: int list = [1; 2; 3]
let doubled = List.map (fun x -> x * 2) numbers
```

## Examples

```fsharp
let inline average (items: ^T list) : ^T =
    (^T: (static member Average: ^T list -> ^T) items)

let result = average [1.0; 2.0; 3.0]
```
