---
title: "ArgumentException"
description: "An ArgumentException occurs when a method receives an invalid argument."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["argument", "invalid", "parameter", "argumentexception"]
weight: 5
---

## What This Error Means

An `ArgumentException` is thrown when a method is called with an argument that doesn't meet its requirements. This can happen when the argument is null, out of range, or of the wrong type.

## Common Causes

- Passing null where non-null is required
- Argument outside valid range
- Wrong type of argument
- Invalid string format

## How to Fix

```fsharp
// WRONG: Not validating input
let processName (name: string) =
    printfn "Hello, %s!" (name.ToUpper())  // ArgumentException if null

// CORRECT: Validate input
let processName (name: string) =
    if System.String.IsNullOrEmpty(name) then
        failwith "Name cannot be null or empty"
    printfn "Hello, %s!" (name.ToUpper())
```

```fsharp
// WRONG: No bounds checking
let getElement idx (arr: 'a array) =
    arr.[idx]  // ArgumentOutOfRangeException

// CORRECT: Check bounds
let getElement idx (arr: 'a array) =
    if idx < 0 || idx >= arr.Length then
        failwithf "Index %d out of range 0..%d" idx (arr.Length - 1)
    arr.[idx]
```

## Examples

```fsharp
// Example 1: Null argument
let s : string = null
s.ToUpper()  // ArgumentNullException

// Example 2: Invalid enum value
let color = enum<System.ConsoleColor> 999  // ArgumentOutOfRangeException

// Example 3: Negative count
Array.zeroCreate<int> -1  // ArgumentOutOfRangeException
```

## Related Errors

- [IndexOutOfRangeException](/languages/fsharp/index-out-of-range)
- [InvalidOperationException](/languages/fsharp/invalid-operation5)
