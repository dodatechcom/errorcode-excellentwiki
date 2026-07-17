---
title: "[Solution] Kotlin CancellationException — Coroutine Cancellation Fix"
description: "Fix Kotlin CancellationException in coroutines. Learn how to properly handle coroutine cancellation and structured concurrency."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# CancellationException — Coroutine Cancellation

A `CancellationException` is thrown when a coroutine is cancelled, either explicitly or due to structured concurrency rules.

## Description

Kotlin coroutines support cancellation through structured concurrency. When a parent coroutine is cancelled, all child coroutines are cancelled too. `CancellationException` is special — it's handled by the coroutine framework and shouldn't be caught without rethrowing.

Common causes:

- **Explicit cancellation** — calling `cancel()` on a job
- **Timeout** — `withTimeout` or `withTimeoutOrNull`
- **Parent cancellation** — parent coroutine cancelled
- **User cancellation** — UI or user-initiated cancellation

## Common Causes

```kotlin
// Cause 1: Explicit cancellation
val job = scope.launch {
    delay(1000)
}
job.cancel()  // CancellationException

// Cause 2: Timeout
withTimeout(1000L) {
    delay(2000L)  // CancellationException
}

// Cause 3: Parent cancellation
scope.launch {
    launch {
        delay(1000)
    }
    delay(100)
}
// If scope is cancelled, child is also cancelled

// Cause 4: Structured concurrency
suspend fun fetchData() {
    coroutineScope {
        launch {
            delay(1000)
            throw CancellationException("Cancelled")
        }
    }
}
```

## How to Fix

### Fix 1: Check for cancellation

```kotlin
// Wrong
suspend fun longTask() {
    delay(1000)  // May throw CancellationException
}

// Correct
suspend fun longTask() {
    ensureActive()
    delay(1000)
}
```

### Fix 2: Handle cleanup properly

```kotlin
// Wrong
suspend fun process() {
    try {
        delay(1000)
    } catch (e: CancellationException) {
        // Bad: swallowing cancellation
    }
}

// Correct
suspend fun process() {
    try {
        delay(1000)
    } finally {
        // Cleanup code
        ensureActive()
    }
}
```

### Fix 3: Use `isActive` check

```kotlin
// Wrong
suspend fun longComputation() {
    repeat(1000) {
        // Long computation without checking
    }
}

// Correct
suspend fun longComputation() {
    repeat(1000) {
        ensureActive()
        // Long computation
    }
}
```

### Fix 4: Use `yield` for cooperative cancellation

```kotlin
// Wrong
suspend fun batchProcess(items: List<Item>) {
    items.forEach { process(it) }
}

// Correct
suspend fun batchProcess(items: List<Item>) {
    items.forEach { 
        yield()
        process(it) 
    }
}
```

## Examples

```kotlin
// Example 1: Proper cancellation handling
suspend fun fetchWithTimeout(url: String): String? {
    return withTimeoutOrNull(5000L) {
        // Network request
        "Response"
    }
}

// Example 2: Cancellation-aware processing
suspend fun processItems(items: List<Int>) = coroutineScope {
    items.map { item ->
        async {
            ensureActive()
            processItem(item)
        }
    }.awaitAll()
}
```

## Related Errors

- [IllegalStateException]({{< relref "/languages/kotlin/illegal-state" >}}) — invalid object state
- [TimeoutCancellationException]({{< relref "/languages/kotlin/timeout-exception" >}}) — coroutine timeout
- [JobCancellationException]({{< relref "/languages/kotlin/job-cancellation" >}}) — job cancelled
