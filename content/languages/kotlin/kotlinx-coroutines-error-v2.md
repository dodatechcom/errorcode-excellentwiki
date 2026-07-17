---
title: "[Solution] Kotlinx Coroutines Cancellation Propagation Error Fix"
description: "Fix kotlinx.coroutines cancellation propagation errors when coroutines are not cancelled properly."
languages: ["kotlin"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Kotlinx Coroutines: Cancellation Propagation Error Fix

A kotlinx.coroutines cancellation error occurs when coroutine cancellation doesn't propagate correctly through structured concurrency.

## What This Error Means

Coroutines support cooperative cancellation. When a parent coroutine is cancelled, children should be cancelled too. Errors occur when cancellation checks are missing or non-cancellable dispatchers prevent cancellation.

## Common Causes

- Not checking for cancellation (`isActive`)
- Using `runBlocking` in coroutine context
- Blocking I/O inside coroutine without yielding
- Non-cancellable dispatcher preventing cleanup
- Exception handler swallowing CancellationException

## How to Fix

### 1. Check for cancellation regularly

```kotlin
// WRONG: Long-running without cancellation check
suspend fun processData() {
    repeat(10000) { i ->
        heavyComputation(i)  // Never checks isActive
    }
}

// CORRECT: Check for cancellation
suspend fun processData() = coroutineScope {
    repeat(10000) { i ->
        ensureActive()
        heavyComputation(i)
    }
}
```

### 2. Use non-blocking I/O

```kotlin
// WRONG: Blocking inside coroutine
suspend fun fetchData() = withContext(Dispatchers.Default) {
    Thread.sleep(1000)  // Blocks thread, can't be cancelled
}

// CORRECT: Use suspend function
suspend fun fetchData() = withContext(Dispatchers.Default) {
    delay(1000)  // Cancellable delay
}
```

### 3. Handle CancellationException properly

```kotlin
// WRONG: Swallowing CancellationException
val handler = CoroutineExceptionHandler { _, _ -> }

// CORRECT: Never catch CancellationException
val handler = CoroutineExceptionHandler { _, throwable ->
    if (throwable !is CancellationException) {
        println("Error: ${throwable.message}")
    }
}
```

### 4. Clean up resources in finally

```kotlin
// CORRECT: Use finally for cleanup
suspend fun processWithCleanup() {
    val resource = acquireResource()
    try {
        withContext(Dispatchers.IO) {
            resource.use { it.process() }
        }
    } finally {
        resource.close()
    }
}
```

## Related Errors

- [Flow Error](flow-error-v2) — Flow collection errors
- [Koin Error](koin-error-v2) — DI issues
- [Room Error](room-error-v2) — database errors
