---
title: "[Solution] Deprecated Function Migration: Executors.newFixedThreadPool to Dispatchers.IO"
description: "Migrate from deprecated thread pool to Dispatchers.IO."
deprecated_function: "Executors.newFixedThreadPool(n)"
replacement_function: "Dispatchers.IO"
languages: ["kotlin"]
deprecated_since: "Kotlin Coroutines"
---

# [Solution] Deprecated Function Migration: Executors.newFixedThreadPool to Dispatchers.IO

The `Executors.newFixedThreadPool(n)` has been deprecated in favor of `Dispatchers.IO`.

## Migration Guide

Dispatchers.IO manages thread pool.

## Before (Deprecated)

```kotlin
val executor = Executors.newFixedThreadPool(4)
executor.submit { }
```

## After (Modern)

```kotlin
withContext(Dispatchers.IO) {
    // IO work
}
```

## Key Differences

- Dispatchers.IO manages thread pool
