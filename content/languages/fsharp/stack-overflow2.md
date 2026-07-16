---
title: "StackOverflowException"
description: "A StackOverflowException occurs when the call stack overflows due to infinite recursion or very deep recursion."
languages: ["fsharp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["stack", "overflow", "recursion", "stackoverflowexception"]
weight: 5
---

## What This Error Means

A `StackOverflowException` is thrown when the runtime stack overflows because of too many nested method calls. This typically happens with infinite recursion or very deep recursive calls.

## Common Causes

- Infinite recursion without base case
- Recursive function that never terminates
- Very deep recursion on large data
- Mutual recursion without termination

## How to Fix

```fsharp
// WRONG: No base case
let rec factorial n =
    n * factorial (n - 1)  // StackOverflowException

// CORRECT: Add base case
let rec factorial n =
    if n <= 0 then 1
    else n * factorial (n - 1)
```

```fsharp
// WRONG: Very deep recursion
let rec count n =
    if n = 0 then 0
    else 1 + count (n - 1)
count 1000000  // May cause StackOverflowException

// CORRECT: Use tail recursion or iteration
let count n =
    let rec loop n acc =
        if n = 0 then acc
        else loop (n - 1) (acc + 1)
    loop n 0
```

## Examples

```fsharp
// Example 1: Infinite recursion
let rec f() = f()
f()  // StackOverflowException

// Example 2: Missing base case
let rec sum lst =
    match lst with
    | x :: xs -> x + sum xs
    | [] -> 0
sum [1..10000000]  // StackOverflowException

// Example 3: Mutual recursion
let rec isEven n = if n = 0 then true else isOdd (n - 1)
and isOdd n = if n = 0 then false else isEven (n - 1)
isEven 1000000  // StackOverflowException
```

## Related Errors

- [OutOfMemoryException](/languages/fsharp/out-of-memory2)
- [IndexOutOfRangeException](/languages/fsharp/index-out-of-range)
