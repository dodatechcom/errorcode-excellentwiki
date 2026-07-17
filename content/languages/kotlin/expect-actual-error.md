---
title: "[Solution] Kotlin Expect/Actual Mismatch Error Fix"
description: "Fix Kotlin expect/actual mismatch errors. Learn why expect declarations fail and how to implement platform-specific code."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

## What This Error Means

An expect/actual mismatch error occurs when an expect declaration does not have a matching actual implementation in all target platforms. Kotlin Multiplatform uses expect/actual for platform-specific code.

## Common Causes

- Missing actual declaration
- Signature mismatch between expect and actual
- Wrong platform target
- Missing dependency

## How to Fix

```kotlin
// WRONG: Missing actual declaration
expect class Platform {
    fun getName(): String
}
// No actual implementation

// CORRECT: Provide actual implementation
// commonMain
expect class Platform {
    fun getName(): String
}

// androidMain
actual class Platform actual constructor() {
    actual fun getName(): String = "Android"
}

// iosMain
actual class Platform actual constructor() {
    actual fun getName(): String = "iOS"
}
```

```kotlin
// WRONG: Signature mismatch
expect fun getPlatformName(): String
actual fun getPlatformName(): Int  // Wrong return type

// CORRECT: Match signatures
expect fun getPlatformName(): String
actual fun getPlatformName(): String = "Android"
```

## Examples

```kotlin
// Example 1: Platform class
expect class Navigator {
    fun navigateTo(url: String)
}

// androidMain
actual class Navigator {
    actual fun navigateTo(url: String) {
        // Android implementation
    }
}

// Example 2: Platform function
expect fun getCurrentTime(): Long

// androidMain
actual fun getCurrentTime(): Long = System.currentTimeMillis()

// Example 3: Platform constant
expect val PLATFORM_NAME: String

// androidMain
actual val PLATFORM_NAME: String = "Android"
```

## Related Errors

- [Inline reified error](inline-reified-error) — reified type issue
- [Contracts error](contract-error) — contracts issue
- [Gradle Kotlin DSL error](gradle-kotlin-dsl-error) — Gradle error
