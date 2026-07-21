---
title: "[Solution] Deprecated Function Migration: data class wrapper to value class"
description: "Migrate from deprecated data class wrapper to value class."
deprecated_function: "data class UserId(val value: String)"
replacement_function: "@JvmInline value class UserId(val value: String)"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.5+"
---

# [Solution] Deprecated Function Migration: data class wrapper to value class

The `data class UserId(val value: String)` has been deprecated in favor of `@JvmInline value class UserId(val value: String)`.

## Migration Guide

value class has zero overhead.

## Before (Deprecated)

```kotlin
data class UserId(val value: String)
```

## After (Modern)

```kotlin
@JvmInline
value class UserId(val value: String)
```

## Key Differences

- value class has zero overhead
