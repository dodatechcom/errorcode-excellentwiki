---
title: "[Solution] Kotlin NonCancellable Context Misuse"
description: "Fix Kotlin NonCancellable context misuse and uninterruptible suspend functions. Learn proper cancellation handling patterns."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1012
---

## What This Error Means

NonCancellable is a CoroutineContext element that prevents coroutine cancellation. Misusing it causes coroutines to run even after cancellation, leading to resource leaks and zombie coroutines.

## Common Causes

- Wrapping entire coroutine body in `withContext(NonCancellable)`
- Using NonCancellable for long-running work instead of catch-and-rethrow
- Not using NonCancellable for critical cleanup (correct usage but often forgotten)
- Combining NonCancellable with blocking operations

```kotlin
// WRONG: Entire work is uninterruptible
launch {
    withContext(NonCancellable) {
        while (true) { delay(1000) }  // Never stops
    }
}
```

## How to Fix

**1. Only use NonCancellable for critical cleanup**

```kotlin
// CORRECT: Only cleanup is non-cancellable
launch {
    try {
        doWork()
    } finally {
        withContext(NonCancellable) {
            cleanupResources()  // Must complete
        }
    }
}
```

**2. Ensure long operations can be interrupted**

```kotlin
// WRONG: Uninterruptible long operation
launch {
    withContext(NonCancellable) {
        processLargeDataset()  // Runs to completion even on cancel
    }
}

// CORRECT: Check for cancellation
launch {
    for (item in dataset) {
        ensureActive()  // Throws CancellationException if cancelled
        processItem(item)
    }
}
```

**3. Use withTimeout for bounded work**

```kotlin
launch {
    try {
        withTimeout(5000) {
            criticalWork()
        }
    } catch (e: TimeoutCancellationException) {
        fallback()
    }
}
```

**4. Use yield() to allow cancellation checks**

```kotlin
launch {
    repeat(1000) {
        processChunk(it)
        yield()  // Allows cancellation check between iterations
    }
}
```

## Examples

```kotlin
// Example 1: Safe cleanup pattern
suspend fun safeProcess() {
    val resource = acquireResource()
    try {
        processWithResource(resource)
    } finally {
        withContext(NonCancellable) {
            resource.close()
        }
    }
}

// Example 2: NonCancellable for state update
launch {
    try {
        val result = fetchData()
        _uiState.value = Success(result)
    } catch (e: CancellationException) {
        withContext(NonCancellable) {
            _uiState.value = Error("Cancelled")
        }
        throw e
    }
}

// Example 3: Cooperative cancellation
suspend fun cooperativeWork(items: List<Int>) {
    items.chunked(100).forEach { chunk ->
        ensureActive()
        chunk.forEach { process(it) }
    }
}
```

## Related Errors

- [CancellationException](cancellationexception-kotlin) — coroutine cancelled
- [Job cancellation error](job-cancellation) — job cancelled
- [Coroutine timeout](coroutine-timeout) — timeout exceeded
