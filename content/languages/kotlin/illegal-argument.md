---
title: "[Solution] Kotlin IllegalArgumentException — Invalid Argument Fix"
description: "Fix Kotlin IllegalArgumentException when a method receives an invalid argument. Validate inputs, use require/check, and handle edge cases."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["illegalargumentexception", "argument", "validation", "require", "check"]
weight: 5
---

# IllegalArgumentException — Invalid Argument Fix

An `IllegalArgumentException` is thrown when a method receives an argument that is appropriate in type but not acceptable in value. This is Kotlin's standard way to signal invalid input.

## Description

`IllegalArgumentException` is a common runtime exception used for input validation. Unlike `NullPointerException` (wrong reference) or `ClassCastException` (wrong type), this indicates the argument value is semantically wrong.

Common scenarios:

- **Negative values where positive is expected** — age, count, index.
- **Out-of-range values** — numbers outside allowed bounds.
- **Blank strings where content is required** — names, emails, URLs.
- **Invalid enum values** — passing an unsupported option.

## Common Causes

```kotlin
// Cause 1: Negative value where positive expected
fun setAge(age: Int) {
    if (age < 0) throw IllegalArgumentException("Age cannot be negative: $age")
    // ...
}

// Cause 2: Blank string where content required
fun processName(name: String) {
    if (name.isBlank()) throw IllegalArgumentException("Name cannot be blank")
    // ...
}

// Cause 3: Value outside allowed range
fun setBrightness(level: Int) {
    if (level !in 0..100) throw IllegalArgumentException("Brightness must be 0-100: $level")
}

// Cause 4: Null in non-nullable parameter (from Java interop)
fun processData(data: String) {
    // If called from Java with null, throws IllegalArgumentException
}
```

## Solutions

### Fix 1: Use `require` for precondition checks

```kotlin
// Wrong
fun setAge(age: Int) {
    if (age < 0) throw IllegalArgumentException("Age cannot be negative")
    // ...
}

// Correct
fun setAge(age: Int) {
    require(age >= 0) { "Age cannot be negative: $age" }
    // ...
}
```

### Fix 2: Use `check` for state validation

```kotlin
// Wrong
fun processItems(items: List<String>) {
    if (items.isEmpty()) throw IllegalArgumentException("List cannot be empty")
    // ...
}

// Correct
fun processItems(items: List<String>) {
    check(items.isNotEmpty()) { "List cannot be empty" }
    // ...
}
```

### Fix 3: Use default values and transforms instead of throwing

```kotlin
// Wrong
fun createUrl(host: String): String {
    if (host.isBlank()) throw IllegalArgumentException("Host cannot be blank")
    return "https://$host"
}

// Correct
fun createUrl(host: String): String {
    val safeHost = host.trim().ifBlank { "localhost" }
    return "https://$safeHost"
}
```

### Fix 4: Validate at call sites with defaults

```kotlin
// Wrong — caller must guess valid range
fun setVolume(level: Int) {
    require(level in 0..100) { "Volume must be 0-100" }
}

// Correct — clamp instead of throwing
fun setVolume(level: Int) {
    val safeLevel = level.coerceIn(0, 100)
    // Use safeLevel
}
```

## Examples

```kotlin
data class User(
    val name: String,
    val age: Int
) {
    init {
        require(name.isNotBlank()) { "Name cannot be blank" }
        require(age in 0..150) { "Age must be between 0 and 150" }
    }
}

fun main() {
    val valid = User("Alice", 30)
    // val invalid = User("", -1)  // IllegalArgumentException
}
```

## Related Errors

- [IllegalStateException]({{< relref "/languages/kotlin/illegal-state" >}}) — object is in wrong state for operation.
- [UnsupportedOperationException]({{< relref "/languages/kotlin/unsupported-operation" >}}) — operation not supported.
- [NullPointerException]({{< relref "/languages/kotlin/null-pointer" >}}) — null reference instead of invalid value.
