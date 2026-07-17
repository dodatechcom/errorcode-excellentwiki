---
title: "NotSupportedException"
description: "A NotSupportedException occurs when an operation is not supported by the current implementation or object."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `NotSupportedException` is thrown when an operation is attempted that is not supported by the object or implementation. This is common with read-only collections, abstract types, or platform-specific operations.

## Common Causes

- Modifying read-only collections
- Calling abstract methods without implementation
- Platform-specific operations on wrong platform
- Unsupported encoding or format

## How to Fix

```fsharp
// WRONG: Modifying read-only collection
let readOnly = [|1; 2; 3|].AsReadOnly()
readOnly.[0] <- 10  // NotSupportedException

// CORRECT: Work with mutable collection
let mutable arr = [|1; 2; 3|]
arr.[0] <- 10  // works
```

```fsharp
// WRONG: Using unsupported method
let bytes = System.Text.Encoding.UTF8.GetBytes("hello")
let decoded = System.Text.Encoding.ASCII.GetString(bytes)  // may lose data

// CORRECT: Use supported encoding
let decoded = System.Text.Encoding.UTF8.GetString(bytes)
```

## Examples

```fsharp
// Example 1: ReadOnly collection
let list = [1; 2; 3] |> List.toSeq
let arr = Array.ofSeq list
arr.SetValue(10, 0)  // works, but:
let readOnly = arr.AsReadOnly()
readOnly.IsReadOnly  // true, can't modify

// Example 2: Unimplemented method
[<AbstractClass>]
type Shape() =
    abstract member Area: unit -> float
let s = Shape()  // Can't instantiate abstract class

// Example 3: Platform not supported
System.Environment.OSVersion.Platform  // may be PlatformID on wrong OS
```

## Related Errors

- [InvalidOperationException](/languages/fsharp/invalid-operation5)
- [ArgumentException](/languages/fsharp/argument-exception)
