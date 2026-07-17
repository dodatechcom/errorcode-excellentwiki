---
title: "[Solution] Kotlin Type Mismatch — Compile-Time Type Fix"
description: "Fix Kotlin type mismatch errors at compile time. Use proper type casting, nullable types, and generics to resolve type conflicts."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# Type Mismatch — Compile-Time Type Fix

A type mismatch error occurs at compile time when Kotlin's type system detects an incompatible type. This is a compile error, not a runtime exception, and must be fixed before the code can run.

## Description

Kotlin has a strict type system that catches type errors during compilation. Type mismatch happens when you assign a value of one type to a variable of a different type without proper conversion.

Common scenarios:

- **Assigning wrong type** — `val x: Int = "hello"`.
- **Returning wrong type from function** — function declared to return `String` returns `Int`.
- **Passing wrong type to function** — argument type doesn't match parameter type.
- **Generic type mismatch** — `List<String>` where `List<Int>` is expected.

## Common Causes

```kotlin
// Cause 1: Direct type assignment
val number: Int = "42"  // Type mismatch: inferred type is String but Int was expected

// Cause 2: Wrong return type
fun getNumber(): Int {
    return "42"  // Type mismatch: String cannot be returned as Int
}

// Cause 3: Wrong argument type
fun process(value: Int) {
    println(value)
}
process("42")  // Type mismatch: String is not Int

// Cause 4: Generic type mismatch
val strings: List<String> = listOf(1, 2, 3)  // Type mismatch: Int is not String
```

## Solutions

### Fix 1: Use explicit type conversion

```kotlin
// Wrong
val number: Int = "42"

// Correct
val number: Int = "42".toInt()

// Or use safe conversion
val number: Int? = "42".toIntOrNull()
```

### Fix 2: Use proper return types

```kotlin
// Wrong
fun getNumber(): Int {
    return "42"
}

// Correct
fun getNumber(): String {
    return "42"
}

// Or convert
fun getNumber(): Int {
    return "42".toInt()
}
```

### Fix 3: Convert arguments before passing

```kotlin
// Wrong
fun process(value: Int) {
    println(value)
}
process("42")

// Correct
process("42".toInt())

// Or make function accept String
fun process(value: String) {
    println(value.toIntOrNull() ?: 0)
}
```

### Fix 4: Use proper generic types

```kotlin
// Wrong
val strings: List<String> = listOf(1, 2, 3)

// Correct
val strings: List<String> = listOf("1", "2", "3")

// Or use mapped list
val strings: List<String> = listOf(1, 2, 3).map { it.toString() }
```

## Examples

```kotlin
fun main() {
    // Common type mismatch fixes

    // String to Int
    val num1: Int = "42".toInt()

    // Int to String
    val str1: String = 42.toString()

    // Any to specific type with smart cast
    val obj: Any = "hello"
    if (obj is String) {
        println(obj.length)  // Smart cast to String
    }

    // Nullable handling
    val nullable: String? = "hello"
    val length: Int = nullable?.length ?: 0
}
```

## Related Errors

- [ClassCastException]({{< relref "/languages/kotlin/class-cast" >}}) — wrong type cast at runtime.
- [NumberFormatException]({{< relref "/languages/kotlin/number-format" >}}) — string to number conversion failed.
- [Unresolved reference]({{< relref "/languages/kotlin/unresolved-reference" >}}) — name not found.
