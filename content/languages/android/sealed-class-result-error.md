---
title: "Result Type Error"
description: "Fix sealed class Result type patterns for Android error handling"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Using sealed class Result type for error handling produces incorrect state transitions

## Common Causes

- Result type not covering all possible states
- Loading state not properly reset after success
- Error state carrying wrong exception type
- Result not properly collected in UI layer

## Fixes

- Define complete state hierarchy: Loading, Success, Error
- Reset loading state after each operation
- Use typed error classes for different failure modes
- Handle each state explicitly in UI collector

## Code Example

```kotlin
sealed class UiResult<out T> {
    data object Loading : UiResult<Nothing>()
    data class Success<T>(val data: T) : UiResult<T>()
    data class Error(val exception: Throwable) : UiResult<Nothing>()
}

// In ViewModel:
fun loadData() {
    _uiState.value = UiResult.Loading
    viewModelScope.launch {
        _uiState.value = try {
            val data = repository.fetchData()
            UiResult.Success(data)
        } catch (e: Exception) {
            UiResult.Error(e)
        }
    }
}

// In Compose:
when (val result = uiState) {
    is UiResult.Loading -> CircularProgressIndicator()
    is UiResult.Success -> Content(result.data)
    is UiResult.Error -> ErrorMessage(result.exception)
}
```

# Sealed class for exhaustive state handling
# Always handle Loading, Success, Error states
# Use when() in Compose for type-safe rendering
