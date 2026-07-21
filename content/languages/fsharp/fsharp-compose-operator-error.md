---
title: "[Solution] F# Compose Operator Error -- Function Composition Issues"
description: "Fix F# compose operator errors when the << or >> operators are misused or produce type mismatches."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Compose Operator Error

This error occurs when the `>>` or `<<` compose operators are used with functions whose input and output types do not align.

## Common Causes

- Output type of the first function does not match input type of the second
- Using compose with multi-argument functions without currying
- Direction of composition is reversed
- Missing parentheses causing incorrect grouping

## How to Fix

### Ensure type alignment

```fsharp
// WRONG: string -> int composed with float -> string (type mismatch)
let f: string -> int = fun s -> s.Length
let g: float -> string = fun f -> f.ToString()
let bad = g >> f  // error: float -> int does not chain properly

// CORRECT: align types
let f: int -> string = fun n -> string n
let g: float -> int = fun f -> int f
let good = g >> f  // float -> string
```

### Use parentheses for clarity

```fsharp
let process =
    (fun x -> x + 1)
    >> (fun x -> x * 2)
    >> (fun x -> string x)

let result = process 5  // "12"
```

## Examples

```fsharp
let double x = x * 2
let increment x = x + 1
let stringify x = string x

let pipeline = double >> increment >> stringify
let result = pipeline 5  // "11"
```
