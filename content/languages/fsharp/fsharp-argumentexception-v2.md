---
title: "[Solution] F# ArgumentException"
description: "Fix F# ArgumentException when function arguments are invalid. Validate inputs and use guard clauses."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `ArgumentException` is thrown when a function receives an argument that doesn't meet its requirements, such as null for non-nullable parameters, empty strings, or values outside valid ranges.

## Common Causes

- Null passed to non-nullable parameter
- Empty string where non-empty expected
- Value outside valid range
- Wrong argument type
- Invalid format or encoding

## How to Fix

```fsharp
// WRONG: No argument validation
let processName (name: string) =
    printfn "Name: %s" name
// Fails if name is null

// CORRECT: Validate arguments
let processName (name: string) =
    if System.String.IsNullOrEmpty(name) then
        invalidArg (nameof name) "Name cannot be null or empty"
    printfn "Name: %s" name
```

```fsharp
// WRONG: No range check
let divide a b = a / b  // DivisionByZero if b = 0

// CORRECT: Guard clause
let divide a b =
    if b = 0.0 then invalidArg (nameof b) "Cannot divide by zero"
    a / b
```

```fsharp
// WRONG: Not validating collection
let firstElement (items: 'a list) =
    items.[0]  // IndexOutOfRangeException if empty

// CORRECT: Use pattern matching
let firstElement items =
    match items with
    | [] -> invalidArg (nameof items) "List is empty"
    | x :: _ -> x
```

## Examples

```fsharp
// Example 1: Argument validation helper
let require condition paramName message =
    if not condition then invalidArg paramName message

// Usage:
let processAge age =
    require (age >= 0 && age <= 150) (nameof age) "Age must be 0-150"

// Example 2: Option with default
let headOrDefault defaultVal items =
    match items with
    | [] -> defaultVal
    | x :: _ -> x

// Example 3: Checked arithmetic
let safeDivide a b =
    if b = 0 then None
    else Some (a / b)
```

## Related Errors

- [fsharp-indexoutofrange]({{< relref "/languages/fsharp/fsharp-indexoutofrange" >}}) — index out of range
- [fsharp-nullreference]({{< relref "/languages/fsharp/fsharp-nullreference" >}}) — null reference
- [fsharp-formatexception]({{< relref "/languages/fsharp/fsharp-formatexception" >}}) — format exception
