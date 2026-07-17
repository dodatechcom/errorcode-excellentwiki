---
title: "StackOverflowException"
description: "A StackOverflowException occurs when the call stack exceeds its maximum depth due to infinite or very deep recursion."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `StackOverflowException` is thrown when a function calls itself recursively without reaching a base case, causing the call stack to exceed its memory limit.

## Common Causes

- Infinite recursion with no base case
- Mutual recursion without termination
- Very deep recursion on large data structures
- Missing termination condition

## How to Fix

```scala
// WRONG: No base case
def factorial(n: Int): Int = n * factorial(n - 1)  // StackOverflowException

// CORRECT: Add base case
def factorial(n: Int): Int =
  if (n <= 0) 1
  else n * factorial(n - 1)
```

```scala
// WRONG: Deep recursion
def sumList(xs: List[Int]): Int = xs match {
  case Nil => 0
  case h :: t => h + sumList(t)  // StackOverflowException for large lists
}

// CORRECT: Use tail recursion
@scala.annotation.tailrec
def sumList(xs: List[Int], acc: Int = 0): Int = xs match {
  case Nil => acc
  case h :: t => sumList(t, acc + h)
}
```

## Examples

```scala
// Example 1: Infinite recursion
def f(): Int = f()
f()  // StackOverflowException

// Example 2: Missing base case
def count(n: Int): Int = 1 + count(n - 1)
count(1000000)  // StackOverflowException

// Example 3: Mutual recursion
def isEven(n: Int): Boolean = if (n == 0) true else isOdd(n - 1)
def isOdd(n: Int): Boolean = if (n == 0) false else isEven(n - 1)
isEven(1000000)  // StackOverflowException
```

## Related Errors

- [OutOfMemoryException](/languages/scala/out-of-memory3)
- [IndexOutOfBoundsException](/languages/scala/index-out-of-bound)
