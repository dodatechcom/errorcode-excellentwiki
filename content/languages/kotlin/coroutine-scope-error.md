---
title: "[Solution] Kotlin CoroutineScope Cancelled Error Fix"
description: "Fix Kotlin CoroutineScope cancelled errors. Learn why scopes get cancelled and how to handle scope lifecycle."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A CoroutineScope cancelled error occurs when trying to launch a coroutine in a scope that has already been cancelled. This commonly happens in ViewModel or Activity after destruction.

## Common Causes

- Scope cancelled after component destroyed
- Launching coroutine after cancellation
- Missing SupervisorJob
- Wrong scope usage

## How to Fix

```kotlin
// WRONG: Launching in cancelled scope
class MyViewModel : ViewModel() {
    fun loadData() {
        viewModelScope.launch {
            // May fail if scope cancelled
        }
    }
}

// CORRECT: Check scope or use supervisorJob
class MyViewModel : ViewModel() {
    fun loadData() {
        if (viewModelScope.isActive) {
            viewModelScope.launch {
                // Safe to launch
            }
        }
    }
}
```

```kotlin
// WRONG: Not handling scope cancellation
fun processInScope(scope: CoroutineScope) {
    scope.launch {
        delay(5000)  // May be cancelled
        // Processing continues after cancel
    }
}

// CORRECT: Handle cancellation
fun processInScope(scope: CoroutineScope) {
    scope.launch {
        try {
            delay(5000)
            // Processing
        } catch (e: CancellationException) {
            // Handle cancellation
            throw e
        }
    }
}
```

## Examples

```kotlin
// Example 1: ViewModel scope
class MyViewModel : ViewModel() {
    fun loadData() {
        viewModelScope.launch {
            _state.value = Loading
            try {
                val data = repository.fetch()
                _state.value = Success(data)
            } catch (e: CancellationException) {
                throw e
            }
        }
    }
}

// Example 2: Custom scope with SupervisorJob
val scope = CoroutineScope(SupervisorJob() + Dispatchers.Main)

// Example 3: Scope lifecycle
fun onDestroy() {
    scope.cancel()
}
```

## Related Errors

- [CancellationException](cancellationexception-kotlin) — coroutine cancelled
- [kotlinx.coroutines error](kotlinx-coroutines-error) — coroutine error
- [Coroutine dispatcher error](coroutines-dispatcher-error) — dispatcher issue
