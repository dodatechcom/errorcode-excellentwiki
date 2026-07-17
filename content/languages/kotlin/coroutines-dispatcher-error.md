---
title: "[Solution] Kotlin Coroutine Dispatcher Error Fix"
description: "Fix Kotlin coroutine dispatcher errors. Learn why dispatcher switching fails and how to use dispatchers properly."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A coroutine dispatcher error occurs when a coroutine uses the wrong dispatcher for its operation. Using the main dispatcher for IO operations or vice versa can cause ANR or performance issues.

## Common Causes

- Blocking operation on Main dispatcher
- UI update from IO dispatcher
- Missing dispatcher in test
- Wrong dispatcher scope

## How to Fix

```kotlin
// WRONG: Blocking on Main
viewModelScope.launch {
    val data = database.query()  // Blocks Main thread
}

// CORRECT: Switch to IO
viewModelScope.launch {
    val data = withContext(Dispatchers.IO) {
        database.query()
    }
    _state.value = data
}
```

```kotlin
// WRONG: UI update from IO
launch(Dispatchers.IO) {
    val data = fetch()
    textView.text = data  // UI update from IO
}

// CORRECT: Switch to Main for UI
launch(Dispatchers.IO) {
    val data = fetch()
    withContext(Dispatchers.Main) {
        textView.text = data
    }
}
```

## Examples

```kotlin
// Example 1: Available dispatchers
Dispatchers.Main      // Android main thread
Dispatchers.IO        // IO operations
Dispatchers.Default   // CPU-intensive
Dispatchers.Unconfined // Current thread

// Example 2: Custom dispatcher
val myDispatcher = Executors.newFixedThreadPool(4).asCoroutineDispatcher()

// Example 3: Test dispatcher
val testDispatcher = UnconfinedTestDispatcher()
val testScope = TestScope(testDispatcher)
```

## Related Errors

- [CancellationException](cancellationexception-kotlin) — coroutine cancelled
- [kotlinx.coroutines error](kotlinx-coroutines-error) — coroutine error
- [Flow collection error](flow-error) — Flow issue
