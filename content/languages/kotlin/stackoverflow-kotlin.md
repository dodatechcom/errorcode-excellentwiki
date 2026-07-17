---
title: "[Solution] Kotlin StackOverflowError — Infinite Recursion Fix"
description: "Fix Kotlin StackOverflowError from infinite recursion. Learn how to identify and prevent recursive calls that exhaust the stack."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# StackOverflowError — Infinite Recursion

A `StackOverflowError` occurs when a method calls itself infinitely, exhausting the call stack.

## Description

Kotlin methods use the call stack to store local variables and return addresses. Infinite recursion fills the stack, causing a crash. This typically happens with missing base cases in recursive functions.

Common causes:

- **Missing base case** — recursive function never stops
- **Indirect recursion** — two methods calling each other
- **Infinite loop with recursion** — recursive call in loop
- **Missing break condition** — recursion without termination

## Common Causes

```kotlin
// Cause 1: Missing base case
fun factorial(n: Int): Int {
    return n * factorial(n - 1)  // StackOverflowError
}

// Cause 2: Indirect recursion
fun a() { b() }
fun b() { a() }  // StackOverflowError

// Cause 3: Infinite loop with recursion
fun process(n: Int) {
    if (n > 0) {
        process(n)  // Same n, infinite recursion
    }
}

// Cause 4: Missing break
fun traverse(node: Node) {
    for (child in node.children) {
        traverse(child)  // May cause StackOverflowError
    }
}
```

## How to Fix

### Fix 1: Add base case

```kotlin
// Wrong
fun factorial(n: Int): Int {
    return n * factorial(n - 1)  // No base case
}

// Correct
fun factorial(n: Int): Int {
    if (n <= 1) return 1  // Base case
    return n * factorial(n - 1)
}
```

### Fix 2: Use iteration instead

```kotlin
// Wrong
fun sum(n: Int): Int {
    if (n <= 0) return 0
    return n + sum(n - 1)  // May overflow for large n
}

// Correct
fun sum(n: Int): Int {
    var total = 0
    for (i in 1..n) {
        total += i
    }
    return total
}
```

### Fix 3: Use tail recursion

```kotlin
// Wrong
fun fibonacci(n: Int): Int {
    if (n <= 1) return n
    return fibonacci(n - 1) + fibonacci(n - 2)  // Not tail recursive
}

// Correct
tailrec fun fibonacci(n: Int, a: Int = 0, b: Int = 1): Int {
    if (n <= 0) return a
    return fibonacci(n - 1, b, a + b)
}
```

### Fix 4: Use explicit stack

```kotlin
// Wrong
fun traverse(node: Node) {
    for (child in node.children) {
        traverse(child)
    }
}

// Correct
fun traverse(root: Node) {
    val stack = ArrayDeque<Node>()
    stack.addLast(root)
    while (stack.isNotEmpty()) {
        val node = stack.removeLast()
        process(node)
        stack.addAll(node.children.reversed())
    }
}
```

## Examples

```kotlin
// Example 1: Tail-recursive factorial
tailrec fun factorial(n: Int, accumulator: Int = 1): Int {
    return if (n <= 1) accumulator
    else factorial(n - 1, n * accumulator)
}

// Example 2: Iterative tree traversal
fun traverseTree(root: TreeNode) {
    val queue = ArrayDeque<TreeNode>()
    queue.addLast(root)
    while (queue.isNotEmpty()) {
        val node = queue.removeFirst()
        process(node)
        node.children.forEach { queue.addLast(it) }
    }
}
```

## Related Errors

- [OutOfMemoryError]({{< relref "/languages/kotlin/out-of-memory" >}}) — heap memory exhausted
- [ConcurrentModificationException]({{< relref "/languages/kotlin/concurrent-modification" >}}) — concurrent collection modification
- [IllegalArgumentException]({{< relref "/languages/kotlin/illegal-argument" >}}) — invalid argument
