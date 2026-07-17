---
title: "[Solution] Scala StackOverflowError in Recursion"
description: "Fix Scala StackOverflowError in recursive functions. Convert to tail recursion or use iterative approaches."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["stack-overflow", "recursion", "tail-recursion", "jvm", "scala"]
weight: 5
---

## What This Error Means

A `StackOverflowError` occurs when the JVM runs out of stack space due to deep or infinite recursion. Each recursive call adds a frame to the call stack, and the stack has a fixed size.

## Common Causes

- Unbounded recursion without base case
- Non-tail-recursive function
- Very deep recursion (>10,000 levels)
- Mutual recursion without tail-call optimization

## How to Fix

```scala
// WRONG: Non-tail-recursive (recursive call is not last expression)
def factorial(n: BigInt): BigInt = {
  if (n <= 0) 1
  else n * factorial(n - 1)  // Not tail-recursive
}
factorial(100000)  // StackOverflowError

// CORRECT: Tail-recursive with accumulator
def factorial(n: BigInt): BigInt = {
  @annotation.tailrec
  def loop(n: BigInt, acc: BigInt): BigInt = {
    if (n <= 0) acc
    else loop(n - 1, n * acc)  // Tail-recursive
  }
  loop(n, 1)
}
```

```scala
// WRONG: Deep tree recursion
def depth(node: TreeNode): Int = {
  if (node == null) 0
  else 1 + Math.max(depth(node.left), depth(node.right))
}

// CORRECT: Use explicit stack (iterative)
def depth(root: TreeNode): Int = {
  var maxDepth = 0
  var stack = List((root, 1))
  while (stack.nonEmpty) {
    val (node, d) = stack.head
    stack = stack.tail
    maxDepth = Math.max(maxDepth, d)
    if (node.left != null) stack = (node.left, d + 1) :: stack
    if (node.right != null) stack = (node.right, d + 1) :: stack
  }
  maxDepth
}
```

```scala
// WRONG: Mutual recursion
def isEven(n: Int): Boolean = if (n == 0) true else isOdd(n - 1)
def isOdd(n: Int): Boolean = if (n == 0) false else isEven(n - 1)

// CORRECT: Use trampoline
import scala.util.control.TailCalls._

def isEven(n: Int): TailRec[Boolean] =
  if (n == 0) done(true) else tailcall(isOdd(n - 1))

def isOdd(n: Int): TailRec[Boolean] =
  if (n == 0) done(false) else tailcall(isEven(n - 1))
```

## Examples

```scala
// Example 1: Convert recursive to iterative
// Recursive
def sumList(list: List[Int]): Int = list match {
  case Nil => 0
  case h :: t => h + sumList(t)
}

// Iterative
def sumList(list: List[Int]): Int = {
  var sum = 0
  var remaining = list
  while (remaining.nonEmpty) {
    sum += remaining.head
    remaining = remaining.tail
  }
  sum
}

// Example 2: @tailrec annotation catches non-tail calls at compile time
@annotation.tailrec
def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)

// Example 3: Use fold for recursion elimination
def factorial(n: Int): BigInt = (1 to n).foldLeft(BigInt(1))(_ * _)
```

## Related Errors

- [scala-outofmemory]({{< relref "/languages/scala/scala-outofmemory" >}}) — out of memory
- [scala-matcherror]({{< relref "/languages/scala/scala-matcherror" >}}) — pattern match failed
- [scala-nullpointer]({{< relref "/languages/scala/scala-nullpointer" >}}) — null pointer
