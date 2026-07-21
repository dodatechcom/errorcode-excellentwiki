---
title: "[Solution] Deprecated Function Migration: Java null checks to Kotlin null safety"
description: "Migrate from deprecated Java null checking to Kotlin null safety operators."
deprecated_function: "if (x != null) x.method()"
replacement_function: "x?.method()"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.0+"
---

# [Solution] Deprecated Function Migration: Java null checks to Kotlin null safety

The `if (x != null) x.method()` has been deprecated in favor of `x?.method()`.

## Migration Guide

Kotlin's null safety eliminates NullPointerExceptions at compile time.

## Before (Deprecated)

```kotlin
if (user != null) {
    val name = user.getName()
    if (name != null) {
        println(name.length)
    }
}
```

## After (Modern)

```kotlin
val name = user?.name
val length = user?.name?.length

// Elvis operator for defaults
val name = user?.name ?: "Unknown"

// let for null-safe blocks
user?.let {
    println(it.name.length)
}
```

## Key Differences

- ?. for safe calls
- ?: for default values (Elvis operator)
- !! for non-null assertion (use sparingly)
- let {} for null-safe operations
