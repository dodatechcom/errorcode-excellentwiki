---
title: "[Solution] F# Partial Application Error -- Incomplete Function Application"
description: "Fix F# partial application errors when functions are not fully applied and produce unexpected types."
languages: ["fsharp"]
error-types: ["compile-time"]
severities: ["error"]
---

# F# Partial Application Error

This error occurs when a multi-argument function is partially applied, resulting in a function type instead of the expected value.

## Common Causes

- Forgetting that currying produces intermediate functions
- Passing a partially applied function where a value is expected
- Misunderstanding tupled vs. curried function signatures
- Using a multi-argument lambda without proper application

## How to Fix

### Fully apply when needed

```fsharp
// WRONG: partial application returns a function
let add a b = a + b
let result = add 5  // result is int -> int, not int

// CORRECT: provide all arguments
let result = add 5 3  // result is int
```

### Use tupled functions for multi-arg needs

```fsharp
let add (a, b) = a + b
let result = add (5, 3)  // explicit tupled call

// Or partially apply intentionally
let addFive = add (5, _)
```

## Examples

```fsharp
let format name age = sprintf "%s is %d" name age
let formatAlice = format "Alice"
let result = formatAlice 30  // "Alice is 30"
```
