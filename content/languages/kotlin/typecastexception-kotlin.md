---
title: "[Solution] Kotlin TypeCastException Fix"
description: "Fix Kotlin TypeCastException when type casting fails. Learn why casting fails and how to use safe casts."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A TypeCastException is thrown when a type cast fails at runtime. This is the exception thrown by the `as` operator when the object is not of the target type.

## Common Causes

- Using `as` operator on incompatible types
- Platform type mismatches from Java
- Generic type erasure causing wrong casts
- Null cast to non-null type

## How to Fix

```kotlin
// WRONG: Forced cast on wrong type
val value: Any = "hello"
val number = value as Int  // TypeCastException

// CORRECT: Use safe cast
val number = value as? Int  // null
```

```kotlin
// WRONG: Casting null to non-null
val value: Any? = null
val str = value as String  // TypeCastException

// CORRECT: Use safe cast or nullable type
val str = value as? String  // null
```

```kotlin
// WRONG: Wrong generic cast
val list: List<Any> = listOf(1, 2, 3)
val strings = list as List<String>  // May fail

// CORRECT: Filter by type
val strings = list.filterIsInstance<String>()
```

## Examples

```kotlin
// Example 1: Safe vs forced cast
val value: Any = 42
val safeCast = value as? String  // null
val forcedCast = value as Int  // 42

// Example 2: Smart cast
fun process(value: Any) {
    if (value is String) {
        println(value.length)  // Smart cast to String
    }
}

// Example 3: Non-null assertion
val nullable: String? = "hello"
val nonNull = nullable as String  // Works
val nullValue: String? = null
val broken = nullValue as String  // TypeCastException
```

## Related Errors

- [ClassCastException](classcastexception-kotlin) — type cast failed
- [NullPointerException](nullpointerexception-kotlin) — null access
- [IllegalArgumentException](illegalargumentexception) — invalid argument
