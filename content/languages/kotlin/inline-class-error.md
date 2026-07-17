---
title: "[Solution] Kotlin Inline Class Error Fix"
description: "Fix Kotlin inline class errors. Learn why inline classes fail and how to use value classes properly."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["inline-class", "value-class", "wrapper", "kotlin"]
weight: 5
---

## What This Error Means

An inline class error occurs when inline classes (value classes) are used incorrectly. Inline classes wrap a single value for type safety without runtime overhead, but have restrictions.

## Common Causes

- Multiple properties in inline class
- Not single-value wrapper
- Generic type parameter
- Nullable wrapped value

## How to Fix

```kotlin
// WRONG: Multiple properties
@JvmInline
value class User(val name: String, val age: Int)  // Error

// CORRECT: Single property only
@JvmInline
value class Email(val value: String)
```

```kotlin
// WRONG: Nullable value
@JvmInline
value class Name(val value: String?)  // May work but discouraged

// CORRECT: Non-null value
@JvmInline
value class Name(val value: String)
```

## Examples

```kotlin
// Example 1: Basic inline class
@JvmInline
value class UserId(val id: Long)

fun getUser(id: UserId) = // ...
getUser(UserId(123))  // Type safe

// Example 2: Type-safe IDs
@JvmInline
value class OrderId(val value: Long)
@JvmInline
value class ProductId(val value: Long)

// Cannot mix OrderId and ProductId

// Example 3: Inline class with validation
@JvmInline
value class Email(val value: String) {
    init {
        require(value.contains("@")) { "Invalid email" }
    }
}
```

## Related Errors

- [Typealias resolution error](typealias-error) — typealias issue
- [ClassCastException](classcastexception-kotlin) — type cast failed
- [IllegalArgumentException](illegalargumentexception) — invalid argument
