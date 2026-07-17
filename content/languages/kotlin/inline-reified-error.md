---
title: "[Solution] Kotlin Reified Type Parameter Error Fix"
description: "Fix Kotlin reified type parameter errors. Learn why reified types fail and how to use inline reified functions."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["reified", "inline", "type-parameter", "kotlin"]
weight: 5
---

## What This Error Means

A reified type parameter error occurs when using reified types incorrectly. Reified types preserve generic type information at runtime, but only work with inline functions.

## Common Causes

- Not in inline function
- Using reified in non-inline context
- Wrong type check at runtime
- Missing reified modifier

## How to Fix

```kotlin
// WRONG: Reified in non-inline function
fun <T> checkType(value: Any): Boolean {
    return value is T  // Error: T is erased
}

// CORRECT: Use reified inline function
inline fun <reified T> checkType(value: Any): Boolean {
    return value is T  // T preserved at runtime
}
```

```kotlin
// WRONG: Not using inline
fun <reified T> filter(list: List<Any>): List<T> {
    return list.filterIsInstance<T>()  // Error: not inline
}

// CORRECT: Use inline
inline fun <reified T> filter(list: List<Any>): List<T> {
    return list.filterIsInstance<T>()
}
```

## Examples

```kotlin
// Example 1: Type check
inline fun <reified T> isType(value: Any): Boolean {
    return value is T
}
isType<String>("hello")  // true
isType<Int>("hello")     // false

// Example 2: Filter by type
inline fun <reified T> List<Any>.filterType(): List<T> {
    return filterIsInstance<T>()
}
val mixed = listOf(1, "two", 3.0, "four")
val strings = mixed.filterType<String>()  // ["two", "four"]

// Example 3: Intent extras
inline fun <reified T> Intent.getExtra(key: String): T? {
    return extras?.get(key) as? T
}
```

## Related Errors

- [Inline class error](inline-class-error) — inline class issue
- [Inline reified error] — reified type issue
- [Expect actual error](expect-actual-error) — expect/actual mismatch
