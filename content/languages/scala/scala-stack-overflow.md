---
title: "[Solution] Scala StackOverflowError — Infinite Recursion Detected"
description: "Fix Scala StackOverflowError in recursive calls. Learn tail recursion optimization, @tailrec annotation, and iterative alternatives."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `StackOverflowError` is thrown when the JVM call stack overflows due to excessive recursion. Each recursive call adds a frame to the call stack, and when the stack exceeds its configured limit (typically 512KB to 1MB), the JVM throws this error. The error message shows the repeating call pattern in the stack trace.

## Why It Happens

The most common cause is a recursive function that is not in tail position. When a function performs work after the recursive call (like `n * factorial(n-1)`), the compiler cannot optimize it into a loop, and each call consumes stack space.

Mutually recursive functions (where function A calls B and B calls A) can also overflow the stack even if each individual call appears to be in tail position, because the JVM does not perform tail-call optimization across method boundaries.

Recursive data structures like deeply nested trees or linked lists can cause stack overflow when processed with recursive traversal functions. A tree with tens of thousands of nested levels will overflow even a correctly tail-recursive function if the recursion is not truly in tail position.

Another common cause is accidentally creating infinite recursion by calling a method on an object that calls back into itself. For example, a `toString` method that references a field whose own `toString` calls the parent's `toString`.

## How to Fix It

### Use @tailrec for tail-recursive functions

```scala
import scala.annotation.tailrec

// Wrong — not tail recursive
def factorial(n: Int): Int =
  if (n <= 1) 1 else n * factorial(n - 1)

// Correct — tail recursive
@tailrec
def factorial(n: Int, acc: Int = 1): Int =
  if (n <= 1) acc else factorial(n - 1, n * acc)
```

### Convert recursive algorithms to iterative

```scala
// Wrong — recursive Fibonacci
def fib(n: Int): Int =
  if (n <= 1) n else fib(n - 1) + fib(n - 2)

// Correct — iterative Fibonacci
def fib(n: Int): Int = {
  var (a, b) = (0, 1)
  for (_ <- 2 to n) {
    val temp = a + b
    a = b
    b = temp
  }
  if (n == 0) 0 else b
}
```

### Use trampolining for mutual recursion

```scala
import scala.util.control.TailCalls._

def isEven(n: Int): TailRec[Boolean] =
  if (n == 0) done(true) else tailcall(isOdd(n - 1))

def isOdd(n: Int): TailRec[Boolean] =
  if (n == 0) done(false) else tailcall(isEven(n - 1))

isEven(100000).result // Returns true without stack overflow
```

### Increase stack size as a temporary fix

```bash
java -Xss2m -jar myapp.jar
```

## Common Mistakes

- Writing recursive functions without the `@tailrec` annotation
- Performing computation after the recursive call instead of in an accumulator
- Using mutual recursion without trampolining
- Assuming the JVM performs tail-call optimization like the CLR or BEAM
- Not checking recursion depth with large input sizes

## Related Pages

- [Scala OutOfMemoryError](/languages/scala/scala-out-of-memory/)
- [Scala MatchError](/languages/scala/match-error/)
- [Scala Future Failure](/languages/scala/scala-future-failure/)
