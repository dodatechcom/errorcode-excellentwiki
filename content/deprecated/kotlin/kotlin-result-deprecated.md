---
title: "[Solution] Deprecated Function Migration: try-catch to Result type"
description: "Migrate from deprecated try-catch to Result type."
deprecated_function: "try { } catch (e: Exception) { }"
replacement_function: "runCatching { }"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.3+"
---

# [Solution] Deprecated Function Migration: try-catch to Result type

The `try { } catch (e: Exception) { }` has been deprecated in favor of `runCatching { }`.

## Migration Guide

runCatching returns Result type.

## Before (Deprecated)

```kotlin
val result = try {
    fetchData()
} catch (e: Exception) {
    null
}
```

## After (Modern)

```kotlin
val result = runCatching { fetchData() }
```

## Key Differences

- runCatching returns Result type
