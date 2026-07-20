---
title: "[Solution] Kotlin tailrec Modifier on Non-Tail-Recursive Function"
description: "Fix Kotlin tailrec modifier errors. Learn what qualifies as tail recursion and how to refactor non-tail functions."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
weight: 1030
---

## What This Error Means

The `tailrec` modifier tells the compiler to optimize tail-recursive functions into loops. If the recursive call is not in tail position (not the last operation), the compiler produces an error.

## Common Causes

- Recursive call followed by additional computation
- Recursive call inside a conditional but not in all branches
- Using return with expression after recursive call
- Recursive call inside try/catch blocks

```kotlin
// ERROR: Not tail recursive — computation after recursive call
tailrec fun factorial(n: Int): Int {
    return if (n <= 1) 1 else n * factorial(n - 1)  // n * is post-call
}
```

## How to Fix

**1. Move recursive call to tail position with accumulator**

```kotlin
// CORRECT: Tail recursive with accumulator
tailrec fun factorial(n: Int, acc: Int = 1): Int {
    return if (n <= 1) acc else factorial(n - 1, n * acc)
}
```

**2. Refactor non-tail recursion to loop**

```kotlin
// WRONG: Not tail recursive
fun treeDepth(node: TreeNode?): Int {
    if (node == null) return 0
    return 1 + maxOf(treeDepth(node.left), treeDepth(node.right))
}

// CORRECT: Use iteration
fun treeDepth(root: TreeNode?): Int {
    var depth = 0
    val queue = ArrayDeque<TreeNode>()
    root?.let { queue.add(it) }
    while (queue.isNotEmpty()) {
        repeat(queue.size) { queue.removeFirst().also { it.left?.let(queue::add); it.right?.let(queue::add) } }
        depth++
    }
    return depth
}
```

**3. Use trampoline for mutual recursion**

```kotlin
sealed class Trampoline<out A> {
    data class Done<A>(val result: A) : Trampoline<A>()
    data class More<A>(val thunk: () -> Trampoline<A>) : Trampoline<A>()
}

fun <A> Trampoline<A>.run(): A = when (this) {
    is Trampoline.Done -> result
    is Trampoline.More -> thunk().run()
}
```

## Examples

```kotlin
// Example 1: Tail recursive Fibonacci
tailrec fun fibonacci(n: Int, a: Long = 0, b: Long = 1): Long {
    return when (n) {
        0 -> a
        1 -> b
        else -> fibonacci(n - 1, b, a + b)
    }
}

// Example 2: Tail recursive string reversal
tailrec fun reverse(s: String, acc: String = ""): String {
    return if (s.isEmpty()) acc else reverse(s.drop(1), s.first() + acc)
}

// Example 3: Tail recursive GCD
tailrec fun gcd(a: Int, b: Int): Int {
    return if (b == 0) a else gcd(b, a % b)
}
```

## Related Errors

- [StackOverflowError](stackoverflow-kotlin) — stack overflow
- [Inline function error](kotlin-inline-function-error) — inline issues
- [Operator overload](kotlin-operator-overload) — operator issues
