---
title: "[Solution] Deprecated Function Migration: sealed class to sealed interface"
description: "Migrate from deprecated sealed class to sealed interface."
deprecated_function: "sealed class Result"
replacement_function: "sealed interface Result"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.5+"
---

# [Solution] Deprecated Function Migration: sealed class to sealed interface

The `sealed class Result` has been deprecated in favor of `sealed interface Result`.

## Migration Guide

Sealed interfaces are more flexible.

## Before (Deprecated)

```kotlin
sealed class Result {
    class Success(val data: Any) : Result()
    class Error(val error: Throwable) : Result()
}
```

## After (Modern)

```kotlin
sealed interface Result {
    class Success(val data: Any) : Result
    class Error(val error: Throwable) : Result
}
```

## Key Differences

- Sealed interfaces are more flexible
