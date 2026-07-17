---
title: "[Solution] Kotlin Flow Collector Error Fix"
description: "Fix Kotlin Flow collector errors when collecting flows incorrectly."
languages: ["kotlin"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["flow", "collector", "StateFlow", "SharedFlow", "kotlin"]
weight: 5
---

# Flow: Collector Error Fix

A Kotlin Flow collector error occurs when a Flow is collected incorrectly, such as collecting from a non-suspending context or not handling exceptions.

## What This Error Means

Kotlin Flows are cold streams that emit values to collectors. Errors occur when collecting in wrong coroutine scope, not handling exceptions, or collecting the same flow from multiple collectors incorrectly.

## Common Causes

- Collecting flow outside coroutine scope
- Not handling exceptions in collector
- Collecting from multiple collectors causing race conditions
- Flow never completes (missing terminal operator)
- Collecting StateFlow without observing lifecycle

## How to Fix

### 1. Collect in proper scope

```kotlin
// WRONG: Collecting outside coroutine
val flow = flow { emit(1) }
flow.collect { println(it) }  // Not in coroutine

// CORRECT: Collect in coroutine scope
lifecycleScope.launch {
    flow.collect { println(it) }
}
```

### 2. Handle exceptions in collector

```kotlin
// CORRECT: Use catch operator
myFlow
    .catch { e -> println("Flow error: ${e.message}") }
    .collect { value -> println("Value: $value") }
```

### 3. Use stateIn for shared state

```kotlin
// CORRECT: Convert Flow to StateFlow for UI
val viewModel = viewModelScope.launch {
    repository.getData()
        .stateIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(5000),
            initialValue = emptyList()
        )
        .collect { data ->
            _uiState.value = UiState.Success(data)
        }
}
```

### 4. Collect once with shareIn

```kotlin
// CORRECT: Share flow among multiple collectors
val sharedFlow = myFlow.shareIn(
    scope = coroutineScope,
    started = SharingStarted.WhileSubscribed(),
    replay = 1
)
```

## Related Errors

- [Kotlinx Coroutines Error](kotlinx-coroutines-error-v2) — coroutine issues
- [Hilt Error](hilt-error-v2) — dependency injection
- [Room Error](room-error-v2) — database errors
