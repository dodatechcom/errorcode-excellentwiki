---
title: "[Solution] Deprecated Function Migration: GlobalScope to structured concurrency"
description: "Migrate from deprecated GlobalScope to structured concurrency."
deprecated_function: "GlobalScope.launch { }"
replacement_function: "viewModelScope.launch { }"
languages: ["kotlin"]
deprecated_since: "Kotlin Coroutines"
---

# [Solution] Deprecated Function Migration: GlobalScope to structured concurrency

The `GlobalScope.launch { }` has been deprecated in favor of `viewModelScope.launch { }`.

## Migration Guide

GlobalScope leaks coroutines.

## Before (Deprecated)

```kotlin
GlobalScope.launch {
    fetchData()
}
```

## After (Modern)

```kotlin
viewModelScope.launch {
    fetchData()
}
```

## Key Differences

- structured concurrency prevents leaks
