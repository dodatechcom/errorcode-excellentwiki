---
title: "[Solution] Deprecated Function Migration: data class with manual toString to auto-generated"
description: "Migrate from deprecated manual toString in data class to auto-generated."
deprecated_function: "data class User with override toString"
replacement_function: "data class User(val name: String)"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.0+"
---

# [Solution] Deprecated Function Migration: data class with manual toString to auto-generated

The `data class User with override toString` has been deprecated in favor of `data class User(val name: String)`.

## Migration Guide

Data classes auto-generate toString.

## Before (Deprecated)

```kotlin
data class User(val name: String) {
    override fun toString() = name
}
```

## After (Modern)

```kotlin
data class User(val name: String)
```

## Key Differences

- Data classes auto-generate toString
