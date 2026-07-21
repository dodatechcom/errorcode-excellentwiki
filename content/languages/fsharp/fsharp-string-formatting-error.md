---
title: "[Solution] F# String Formatting Error -- Printf Specifier Mismatch"
description: "Fix F# printf formatting errors when format specifiers do not match argument types."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# String Formatting Error

This error occurs when the format string in printf, sprintf, or similar functions contains specifiers that do not match the supplied arguments.

## Common Causes

- Wrong specifier for the argument type (e.g., %d for a string)
- Extra or missing arguments relative to specifiers
- Using %f without specifying precision
- Mixing up %O (object) with typed specifiers

## How to Fix

### Match specifiers to types

```fsharp
// WRONG: %d expects int, receives string
printfn "%d" "hello"

// CORRECT: use %s for strings
printfn "%s" "hello"
```

### Provide all required arguments

```fsharp
// WRONG: two specifiers, one argument
printfn "Name: %s, Age: %d" "Alice"

// CORRECT: supply matching arguments
printfn "Name: %s, Age: %d" "Alice" 30
```

## Examples

```fsharp
let name = "Alice"
let age = 30
let balance = 1234.56
printfn "%s is %d years old with $%.2f" name age balance

// Pad and align
printfn "%-20s %10d %8.2f" "Product" 42 99.99
```
