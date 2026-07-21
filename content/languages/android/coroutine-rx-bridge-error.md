---
title: "Coroutine RxJava Bridge Error"
description: "Fix Kotlin coroutines and RxJava interop bridge errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Coroutines and RxJava do not interoperate correctly in Android

## Common Causes

- RxJava Observable not convertible to Flow
- Coroutine scope not matching RxJava scheduler
- Disposable not cancelled when coroutine cancelled
- Cold and hot stream behavior mismatch

## Fixes

- Use kotlinx-coroutines-rx3 for interop
- Convert Observable to Flow with asFlow()
- Use CoroutineScope from structured concurrency
- Handle cold vs hot stream differences

## Code Example

```kotlin
// RxJava to Coroutine:
val flow = apiService.getObservable().asFlow()

// Coroutine to RxJava:
val observable = flow.asObservable()

// In ViewModel:
viewModelScope.launch {
    apiService.getObservable()
        .asFlow()
        .catch { emit(emptyList()) }
        .collect { users -> _uiState.value = users }
}
```

# Dependencies:
# implementation 'org.jetbrains.kotlinx:kotlinx-coroutines-rx3:1.7.3'
# Use asFlow() and asObservable() for conversion
