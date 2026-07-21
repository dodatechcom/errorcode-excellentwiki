---
title: "[Solution] Deprecated Function Migration: GlobalScope.launch to structured concurrency"
description: "Migrate from deprecated GlobalScope.launch to structured concurrency."
deprecated_function: "GlobalScope.launch"
replacement_function: "viewModelScope / lifecycleScope"
languages: ["kotlin"]
deprecated_since: "Kotlin coroutines"
---

# [Solution] Deprecated Function Migration: GlobalScope.launch to structured concurrency

The `GlobalScope.launch` has been deprecated in favor of `viewModelScope / lifecycleScope`.

## Migration Guide

GlobalScope launches unstructured coroutines

GlobalScope can cause coroutine leaks.

## Before (Deprecated)

```kotlin
GlobalScope.launch {
    val data = fetchData()
    updateUI(data)
}
```

## After (Modern)

```kotlin
viewModelScope.launch {
    val data = fetchData()
    _data.value = data
}
```

## Key Differences

- viewModelScope cancels when ViewModel cleared
- lifecycleScope cancels on Activity destroy
