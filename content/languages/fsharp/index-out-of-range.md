---
title: "IndexOutOfRangeException"
description: "An IndexOutOfRangeException occurs when accessing an array or collection with an index outside its valid bounds."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `IndexOutOfRangeException` is thrown when you try to access an element of an array or collection using an index that is less than zero or greater than or equal to the collection's length.

## Common Causes

- Off-by-one errors in loops
- Using negative indices
- Accessing array beyond its length
- Incorrect index calculation

## How to Fix

```fsharp
// WRONG: Accessing beyond array bounds
let arr = [|1; 2; 3|]
let x = arr.[3]  // IndexOutOfRangeException

// CORRECT: Use valid index
let arr = [|1; 2; 3|]
let x = arr.[2]  // 3 (zero-indexed)
```

```fsharp
// WRONG: No bounds check
let getElement idx (arr: 'a array) = arr.[idx]

// CORRECT: Check bounds first
let getElement idx (arr: 'a array) =
    if idx >= 0 && idx < arr.Length then
        Some arr.[idx]
    else
        None
```

## Examples

```fsharp
// Example 1: Off by one
let arr = [|10; 20; 30|]
arr.[arr.Length]  // IndexOutOfRangeException

// Example 2: Negative index
let list = [1; 2; 3]
list.[-1]  // IndexOutOfRangeException

// Example 3: Empty collection
let empty = Array.empty<int>
empty.[0]  // IndexOutOfRangeException
```

## Related Errors

- [ArgumentException](/languages/fsharp/argument-exception)
- [NullReferenceException](/languages/fsharp/null-reference5)
