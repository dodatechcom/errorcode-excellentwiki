---
title: "[Solution] Swift Stack Overflow Fix"
description: "Fix Swift stack overflow errors. Learn why stack overflow occurs in recursion and how to prevent it."
languages: ["swift"]
severities: ["error"]
error-types: ["memory-error"]
tags: ["stack-overflow", "recursion", "memory", "swift"]
weight: 5
---

## What This Error Means

A stack overflow occurs when a program uses more stack memory than is available, typically caused by infinite or very deep recursion. Each function call adds a frame to the call stack, and exceeding the limit crashes the app.

## Common Causes

- Infinite recursion without base case
- Very deep recursive calls
- Large stack allocations
- Recursive closures without termination

## How to Fix

```swift
// WRONG: Infinite recursion
func countDown(n: Int) {
    countDown(n: n)  // No base case
}

// CORRECT: Add base case
func countDown(n: Int) {
    guard n > 0 else { return }
    print(n)
    countDown(n: n - 1)
}
```

```swift
// WRONG: Deep recursion on large input
func fibonacci(_ n: Int) -> Int {
    if n <= 1 { return n }
    return fibonacci(n - 1) + fibonacci(n - 2)  // Exponential calls
}

// CORRECT: Use iteration or memoization
func fibonacci(_ n: Int) -> Int {
    if n <= 1 { return n }
    var a = 0, b = 1
    for _ in 2...n {
        let temp = a + b
        a = b
        b = temp
    }
    return b
}
```

## Examples

```swift
// Example 1: Safe recursion with accumulator
func factorial(_ n: Int, accumulator: Int = 1) -> Int {
    guard n > 1 else { return accumulator }
    return factorial(n - 1, accumulator: n * accumulator)
}

// Example 2: Tail call optimization
func gcd(_ a: Int, _ b: Int) -> Int {
    guard b != 0 else { return a }
    return gcd(b, a % b)  // Tail recursive
}

// Example 3: Convert to iteration
func sum(_ numbers: [Int]) -> Int {
    var total = 0
    for number in numbers {
        total += number
    }
    return total
}
```

## Related Errors

- [Out of memory](out-of-memory-swift) — memory exhaustion
- [Memory access error](memory-access-error) — EXC_BAD_ACCESS
- [Integer overflow](integer-overflow-swift) — arithmetic overflow
