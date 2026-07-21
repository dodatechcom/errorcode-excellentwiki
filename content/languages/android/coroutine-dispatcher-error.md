---
title: "Coroutine Dispatcher Error"
description: "Fix Kotlin coroutine dispatcher errors for Android threading requirements"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Coroutine runs on wrong thread causing NetworkOnMainThreadException or UI freeze

## Common Causes

- Using Dispatchers.Default for IO operations
- Updating UI from background dispatcher
- Dispatchers.IO blocking main thread indirectly
- WithContext dispatcher not switching correctly

## Fixes

- Use Dispatchers.IO for network and disk operations
- Use Dispatchers.Main for UI updates
- Use withContext(Dispatchers.IO) for thread switching
- Never block main thread with runBlocking

## Code Example

```kotlin
// CORRECT dispatcher usage
viewModelScope.launch(Dispatchers.Main) {
    val data = withContext(Dispatchers.IO) {
        repository.fetchData()  // Network call
    }
    _uiState.value = UiState.Success(data)  // UI update on Main
}

// For Flow:
flow { emit(repository.fetchData()) }
    .flowOn(Dispatchers.IO)
    .collect { _uiState.value = it }
```

# Dispatchers.Main - UI operations
# Dispatchers.IO - network, disk, database
# Dispatchers.Default - CPU-intensive work
# Avoid runBlocking on any UI thread
