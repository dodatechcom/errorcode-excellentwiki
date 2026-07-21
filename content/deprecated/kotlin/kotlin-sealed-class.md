---
title: "[Solution] Deprecated Function Migration: enum classes to sealed classes"
description: "Migrate from enum-based state to sealed classes for type safety in Kotlin."
deprecated_function: "enum class for states"
replacement_function: "sealed class"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.0+"
---

# [Solution] Deprecated Function Migration: enum classes to sealed classes

The `enum class for states` has been deprecated in favor of `sealed class`.

## Migration Guide

Sealed classes allow subclasses with different data, better for state machines.

## Before (Deprecated)

```kotlin
enum class NetworkState {
    Loading, Success, Error
}

fun handleState(state: NetworkState) {
    when (state) {
        NetworkState.Loading -> showLoading()
        NetworkState.Success -> showContent()
        NetworkState.Error -> showError()
    }
}
```

## After (Modern)

```kotlin
sealed class NetworkState {
    object Loading : NetworkState()
    data class Success(val data: List<Item>) : NetworkState()
    data class Error(val message: String) : NetworkState()
}

fun handleState(state: NetworkState) {
    when (state) {
        is NetworkState.Loading -> showLoading()
        is NetworkState.Success -> showContent(state.data)
        is NetworkState.Error -> showError(state.message)
    }
}
```

## Key Differences

- Sealed classes have subclasses, not enum values
- Each subclass can hold different data
- when exhaustively matches all cases
- Better for state with data
