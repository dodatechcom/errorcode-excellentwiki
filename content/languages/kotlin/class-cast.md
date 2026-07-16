---
title: "[Solution] Kotlin ClassCastException — Type Cast Fix"
description: "Fix Kotlin ClassCastException when an object cannot be cast to the target type. Use safe casts, type checks, and proper generics."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["classcastexception", "cast", "type", "is", "as"]
weight: 5
---

# ClassCastException — Type Cast Fix

A `ClassCastException` is thrown when you attempt to cast an object to a type that it is not an instance of. This commonly occurs with unsafe casts using the `as` operator.

## Description

Kotlin's `as` operator performs an unchecked cast at runtime. If the object is not an instance of the target type, the cast fails with `ClassCastException`. This is common when working with generic types, Java interop, or heterogeneous collections.

Common scenarios:

- **Unsafe `as` cast** — casting without checking the type first.
- **Java generic type erasure** — `List<String>` becomes `List<*>` at runtime.
- **Incorrect type assumption** — treating a `Dog` as a `Cat`.
- **Platform types from Java** — Kotlin cannot verify Java return types.

## Common Causes

```kotlin
// Cause 1: Unsafe cast with as
val obj: Any = "hello"
val number: Int = obj as Int  // ClassCastException: String cannot be cast to Integer

// Cause 2: Generic type erasure
val list: List<*> = listOf("a", "b", "c")
val strings: List<String> = list as List<String>  // Unsafe cast (warning), may fail later

// Cause 3: Wrong type in heterogeneous collection
val items: List<Any> = listOf("hello", 42, true)
val number: String = items[1] as String  // ClassCastException: Integer cannot be cast to String

// Cause 4: Java interop returning wrong type
val javaMap: Map<String, Any> = getJavaMap()
val value: String = javaMap["key"] as String  // May not be a String
```

## Solutions

### Fix 1: Use safe cast `as?`

```kotlin
// Wrong
val obj: Any = "hello"
val number: Int = obj as Int  // ClassCastException

// Correct
val number: Int? = obj as? Int  // Returns null instead of throwing
```

### Fix 2: Check type before casting

```kotlin
// Wrong
fun process(obj: Any) {
    val str = obj as String  // May throw
}

// Correct
fun process(obj: Any) {
    if (obj is String) {
        println(obj.length)  // Smart cast to String
    }
}
```

### Fix 3: Use `when` for multiple type checks

```kotlin
// Wrong
fun describe(obj: Any): String {
    return (obj as Number).toString()  // May throw
}

// Correct
fun describe(obj: Any): String {
    return when (obj) {
        is String -> "String: $obj"
        is Number -> "Number: $obj"
        is Boolean -> "Boolean: $obj"
        else -> "Unknown: $obj"
    }
}
```

### Fix 4: Handle generic type erasure properly

```kotlin
// Wrong — generic type is erased at runtime
fun <T> process(list: List<T>) {
    val first = list[0] as String  // ClassCastException if T is not String
}

// Correct — use reified type parameters
inline fun <reified T> process(list: List<T>) {
    val first = list[0]
    if (first is String) {
        println(first.length)
    }
}
```

## Examples

```kotlin
fun main() {
    val items: List<Any> = listOf("hello", 42, 3.14, true)

    for (item in items) {
        val result = when (item) {
            is String -> "String of length ${item.length}"
            is Int -> "Integer: ${item * 2}"
            is Double -> "Double: ${item + 1.0}"
            is Boolean -> "Boolean: ${!item}"
            else -> "Unknown type"
        }
        println(result)
    }
}
```

## Related Errors

- [NullPointerException]({{< relref "/languages/kotlin/null-pointer" >}}) — null dereference instead of cast error.
- [IllegalArgumentException]({{< relref "/languages/kotlin/illegal-argument" >}}) — wrong argument type passed.
- [Type mismatch]({{< relref "/languages/kotlin/type-mismatch" >}}) — compile-time type mismatch.
