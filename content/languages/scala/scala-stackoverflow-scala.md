---
title: "[Solution] Scala StackOverflowError"
description: "Fix Scala StackOverflowError. Learn about stack depth issues and tail recursion in Scala."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `StackOverflowError` occurs when a method or function calls itself recursively too many times, exhausting the call stack. This is common with deep recursion without tail-call optimization.

## Common Causes

- Deep recursion without `@tailrec` annotation
- Missing base case in recursive function
- Circular method calls
- Very deep object graph traversal

## How to Fix

Use tail recursion with `@tailrec`:

```scala
// Wrong: not tail recursive
def factorial(n: Int): Int = {
  if (n <= 1) 1
  else n * factorial(n - 1) // Stack overflow for large n
}

// Correct: tail recursive
import scala.annotation.tailrec

@tailrec
def factorial(n: Int, acc: Int = 1): Int = {
  if (n <= 1) acc
  else factorial(n - 1, n * acc) // Tail recursive
}
```

Convert recursion to iteration:

```scala
// Wrong: recursive
def sumList(list: List[Int]): Int = {
  list match {
    case Nil => 0
    case head :: tail => head + sumList(tail)
  }
}

// Correct: use fold
def sumList(list: List[Int]): Int = list.foldLeft(0)(_ + _)
```

Ensure base case exists:

```scala
// Wrong: no base case
def loop(n: Int): Int = loop(n + 1)

// Correct: has base case
def countDown(n: Int): Int = {
  if (n <= 0) 0
  else countDown(n - 1)
}
```

## Examples

```scala
def infinite(): Int = infinite()
infinite() // StackOverflowError
```

## Related Errors

- [oom] — out of memory from large allocations
- [matcherror] — pattern match fails
