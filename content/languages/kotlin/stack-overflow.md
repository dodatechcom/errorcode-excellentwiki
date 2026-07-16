---
title: "[Solution] Kotlin StackOverflowError — Infinite Recursion Fix"
description: "Fix Kotlin StackOverflowError when recursion depth exceeds the stack limit. Convert to iteration, add base cases, and use tail recursion."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["stackoverflowerror", "recursion", "stack", "tailrec"]
weight: 5
---

# StackOverflowError — Infinite Recursion Fix

A `StackOverflowError` is thrown when the call stack overflows due to excessive recursive calls. Each method call adds a frame to the stack, and when the limit is exceeded, the JVM crashes.

## Description

The JVM has a fixed stack size (typically 512KB–1MB). Each recursive call adds a stack frame. When recursion is too deep or infinite, the stack overflows. Unlike Python's `RecursionError`, Java/Kotlin's `StackOverflowError` is an `Error`, not an exception, and is harder to catch.

Common scenarios:

- **Missing base case** — recursion never terminates.
- **Base case unreachable** — wrong condition prevents termination.
- **Circular object references** — object A references B which references A.
- **Deep but valid recursion** — tree traversal on very deep trees.

## Common Causes

```kotlin
// Cause 1: Missing base case
fun countdown(n: Int) {
    println(n)
    countdown(n - 1)  // StackOverflowError: never stops
}

// Cause 2: Base case unreachable
fun factorial(n: Int): Long {
    if (n == 0) return 1
    return n * factorial(n - 1)
}
factorial(-5)  // Never reaches 0, infinite recursion

// Cause 3: Circular references
class Node(val value: Int, var next: Node? = null)
val a = Node(1)
val b = Node(2)
a.next = b
b.next = a  // Circular reference

// Cause 4: Mutual recursion without base case
fun isEven(n: Int): Boolean = if (n == 0) true else isOdd(n - 1)
fun isOdd(n: Int): Boolean = if (n == 0) false else isEven(n - 1)
isEven(-1)  // Infinite recursion
```

## Solutions

### Fix 1: Add a proper base case

```kotlin
// Wrong
fun countdown(n: Int) {
    println(n)
    countdown(n - 1)
}

// Correct
fun countdown(n: Int) {
    if (n <= 0) {
        println("Done!")
        return
    }
    println(n)
    countdown(n - 1)
}
```

### Fix 2: Use tail recursion with `tailrec`

```kotlin
// Wrong — recursive, uses stack
fun factorial(n: Int): Long {
    if (n == 0) return 1
    return n * factorial(n - 1)
}

// Correct — tail recursive, optimized to loop
tailrec fun factorial(n: Int, acc: Long = 1): Long {
    if (n == 0) return acc
    return factorial(n - 1, n * acc)
}
```

### Fix 3: Convert recursion to iteration

```kotlin
// Wrong — recursive Fibonacci
fun fibonacci(n: Int): Int {
    if (n <= 1) return n
    return fibonacci(n - 1) + fibonacci(n - 2)
}

// Correct — iterative approach
fun fibonacci(n: Int): Int {
    if (n <= 1) return n
    var a = 0
    var b = 1
    for (i in 2..n) {
        val temp = a + b
        a = b
        b = temp
    }
    return b
}
```

### Fix 4: Detect circular references

```kotlin
// Wrong — no cycle detection
fun traverse(node: Node?) {
    if (node != null) {
        println(node.value)
        traverse(node.next)
    }
}

// Correct — track visited nodes
fun traverse(start: Node?) {
    val visited = mutableSetOf<Node>()
    var current = start
    while (current != null) {
        if (!visited.add(current)) {
            println("Cycle detected at ${current.value}")
            return
        }
        println(current.value)
        current = current.next
    }
}
```

## Examples

```kotlin
// This will cause StackOverflowError:
// fun recurse(): Unit = recurse()
// recurse()

// Tail-recursive version (no stack overflow)
tailrec fun countDown(n: Int) {
    if (n <= 0) return
    println(n)
    countDown(n - 1)  // Tail call, optimized to loop
}

fun main() {
    countDown(100000)  // Works fine with tailrec
}
```

## Related Errors

- [OutOfMemoryError]({{< relref "/languages/kotlin/out-of-memory" >}}) — heap memory exhausted.
- [CancellationException]({{< relref "/languages/kotlin/cancellation-exception" >}}) — coroutine cancelled.
- [RuntimeException]({{< relref "/languages/kotlin/runtime-exception" >}}) — general runtime error.
