---
title: "[Solution] Kotlin Extension Function Resolution Error Fix"
description: "Fix Kotlin extension function resolution errors. Learn why extension functions fail and how to resolve overloads."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

An extension function resolution error occurs when the compiler cannot determine which extension function to use, or when the extension function is not available for the given type.

## Common Causes

- Ambiguous extension functions
- Missing import
- Wrong receiver type
- Generic type mismatch

## How to Fix

```kotlin
// WRONG: Ambiguous extension functions
fun String.exclaim() = "$this!"
fun Any.exclaim() = "$this!!"

println("hello".exclaim())  // Ambiguous

// CORRECT: Use fully qualified call
println("hello".String.exclaim())  // Not valid syntax
// Or rename to avoid ambiguity
fun String.exclaimString() = "$this!"
```

```kotlin
// WRONG: Missing import
// Extension function defined in another file
// Not imported

// CORRECT: Import the extension
import com.example.exclaim
println("hello".exclaim())
```

## Examples

```kotlin
// Example 1: Basic extension function
fun String.isPalindrome(): Boolean {
    return this == this.reversed()
}

println("madam".isPalindrome())  // true

// Example 2: Extension on nullable type
fun String?.defaultIfNull(default: String): String {
    return this ?: default
}

val name: String? = null
println(name.defaultIfNull("Unknown"))  // "Unknown"

// Example 3: Generic extension
fun <T> T.isNotNull(): Boolean {
    return this != null
}
```

## Related Errors

- [Unresolved reference error] — function not found
- [ClassCastException](classcastexception-kotlin) — type cast failed
- [TypeCastException](typecastexception-kotlin) — type cast failed
