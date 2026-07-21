---
title: "Groovy StackOverflowError in recursive closure"
description: "Fix Groovy StackOverflowError when recursive closures or method calls cause infinite call stack depth."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `StackOverflowError` occurs when method or closure calls recurse too deeply without a base case, exhausting the JVM call stack. In Groovy, this commonly happens with closures that reference themselves or with mutually recursive methods.

## Common Causes

- Closure that calls itself without a termination condition
- Two closures that call each other creating mutual recursion
- Infinite loop disguised as recursion
- Recursive method on large data structures without depth limit
- Using delegation in closures that creates unexpected recursion

## How to Fix

```groovy
// WRONG: Closure calls itself infinitely
def factorial = { int n ->
    n * factorial(n - 1)  // StackOverflowError at n=0
}
factorial(5)

// CORRECT: Add base case
def factorial
factorial = { int n ->
    if (n <= 1) 1 else n * factorial(n - 1)
}
factorial(5)  // 120
```

```groovy
// WRONG: Mutual recursion without limit
def isEven
def isOdd
isEven = { int n -> n == 0 ? true : isOdd(n - 1) }
isOdd = { int n -> n == 0 ? false : isEven(n - 1) }
isEven(100000)  // StackOverflowError

// CORRECT: Use iteration or modulo
def isEven = { int n -> n % 2 == 0 }
isEven(100000)  // true
```

## Examples

```groovy
// Example 1: Recursive tree traversal
class TreeNode {
    String name
    List<TreeNode> children = []
    
    void traverse() {
        println name
        children.each { it.traverse() }  // fine if tree is finite
    }
}

// Example 2: Recursive string builder
def buildString
buildString = { int depth ->
    depth == 0 ? "leaf" : "node(${buildString(depth - 1)})"
}
println buildString(3)

// Example 3: Trampolining for safe recursion
def trampoline
trampoline = { Closure cl, args ->
    def result = cl(*args)
    while (result instanceof Closure) {
        result = result()
    }
    result
}
```

## Related Errors

- [Out of memory error](groovy-memory-error) -- heap exhaustion
- [Infinite loop error](groovy-runtime-error) -- non-recursive infinite loops
