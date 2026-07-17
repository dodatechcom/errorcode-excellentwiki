---
title: "[Solution] Kotlin Destructuring Component Error Fix"
description: "Fix Kotlin destructuring component errors. Learn why componentN functions fail and how to implement them."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A destructuring component error occurs when the componentN() functions are not properly defined for an object. These functions are required for destructuring declarations.

## Common Causes

- Missing component functions
- Wrong component function signatures
- Components return wrong types
- Not using operator keyword

## How to Fix

```kotlin
// WRONG: Missing component functions
class User(val name: String, val age: Int)
val (name, age) = User("Alice", 30)  // Error

// CORRECT: Add component functions
class User(val name: String, val age: Int) {
    operator fun component1() = name
    operator fun component2() = age
}
val (name, age) = User("Alice", 30)
```

```kotlin
// WRONG: Wrong component count
data class Triple(val a: Int, val b: Int, val c: Int)
val (x, y) = Triple(1, 2, 3)  // OK but ignores c

// CORRECT: Match component count
val (x, y, z) = Triple(1, 2, 3)
```

## Examples

```kotlin
// Example 1: Manual component functions
class Range(val start: Int, val end: Int) {
    operator fun component1() = start
    operator fun component2() = end
}
val (start, end) = Range(1, 10)

// Example 2: Extension component functions
class User(val name: String, val age: Int)
operator fun User.component1() = name
operator fun User.component2() = age

val (name, age) = User("Alice", 30)

// Example 3: Pair and Triple
val pair = Pair("hello", 42)
val (str, num) = pair

val triple = Triple(1, 2, 3)
val (a, b, c) = triple
```

## Related Errors

- [Destructuring declaration error](destructuring-error) — destructuring issue
- [Destructuring iterator error](destructuring-iterator-error) — iterator issue
- [ClassCastException](classcastexception-kotlin) — type cast failed
