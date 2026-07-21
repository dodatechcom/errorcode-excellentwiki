---
title: "Coroutine Exception Handler Error"
description: "Fix Kotlin coroutine uncaught exception handler configuration in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Unhandled coroutine exceptions crash the app or go unreported

## Common Causes

- No CoroutineExceptionHandler installed
- Exception in launch{} not caught
- Async{} exception not awaited
- ExceptionHandler only catches non-cancellation exceptions

## Fixes

- Install CoroutineExceptionHandler at scope level
- Use try/catch within coroutine for expected errors
- Always call await() on Deferred
- ExceptionHandler cannot prevent cancellation

## Code Example

```kotlin
val exceptionHandler = CoroutineExceptionHandler { _, throwable ->
    viewModelScope.launch {
        _uiState.value = UiState.Error(throwable.message ?: "Unknown error")
    }
}

viewModelScope.launch(exceptionHandler) {
    val result = repository.fetchData()  // Exception caught here
}

// For multiple coroutines:
val scope = CoroutineScope(Dispatchers.Main + exceptionHandler)
```

# CoroutineExceptionHandler replaces default crash
# It receives exceptions that are not caught by try/catch
# Cannot be used with runBlocking
