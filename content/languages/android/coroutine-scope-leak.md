---
title: "Coroutine Scope Leak"
description: "Fix Kotlin coroutine scope leaks and lifecycle-aware coroutine management"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Coroutines outlive their intended scope causing memory leaks

## Common Causes

- Using GlobalScope.launch for background work
- CoroutineScope not cancelled in onDestroy
- Launching in lifecycle without lifecycleScope
- CoroutineJob not stored for cancellation

## Fixes

- Use lifecycleScope for Activity/Fragment
- Use viewModelScope for ViewModel
- Cancel coroutineJob in cleanup methods
- Avoid GlobalScope entirely

## Code Example

```kotlin
// WRONG: GlobalScope leaks
GlobalScope.launch {
    repository.fetchData()  // Never cancelled!
}

// CORRECT: lifecycle-aware scope
lifecycleScope.launch {
    repository.fetchData()  // Cancelled when lifecycle destroyed
}

// In ViewModel:
viewModelScope.launch {
    repository.fetchData()  // Cancelled when ViewModel cleared
}
```

# Use lifecycleScope.launch { } for UI work
# Use viewModelScope.launch { } for business logic
# Both auto-cancel at appropriate lifecycle events
