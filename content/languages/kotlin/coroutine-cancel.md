---
title: "[Solution] Kotlin Coroutine Was Cancelled — Cancellation Fix"
description: "Fix Kotlin coroutine cancellation errors. Understand structured concurrency, handle CancellationException, and propagate cancellation correctly."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Coroutine Was Cancelled — Cancellation Fix

A "Coroutine was cancelled" error occurs when a coroutine is terminated by its parent scope or by an explicit cancel call. This is the standard mechanism for cooperative coroutine cancellation.

## Description

Kotlin coroutines use structured concurrency where child coroutines are bound to their parent scope. When the parent is cancelled or an exception propagates, all children receive a `CancellationException`. The coroutine should clean up and terminate gracefully.

Common scenarios:

- **Parent scope cancelled** — `scope.cancel()` cancels all children.
- **Structured concurrency** — parent job cancelled, children follow.
- **Timeout exceeded** — `withTimeout` cancels on timeout.
- **Exception in sibling** — unhandled exception cancels the scope.
- **Explicit cancel** — `job.cancel()` or `job.cancelAndJoin()`.

## Common Causes

```kotlin
// Cause 1: Parent scope cancelled
val scope = CoroutineScope(Dispatchers.Default)
scope.launch {
    delay(10000)  // Cancelled when scope is cancelled
}
scope.cancel()

// Cause 2: Timeout
val job = launch {
    withTimeout(1000) {
        delay(5000)  // Cancelled after 1 second
    }
}

// Cause 3: Exception in sibling coroutine
val scope = CoroutineScope(Job())
scope.launch {
    throw RuntimeException("Error")  // Cancels entire scope
}
scope.launch {
    delay(1000)  // Also cancelled
}

// Cause 4: Not responding to cancellation
val job = launch {
    while (true) {  // Never checks isActive
        process()
    }
}
```

## Solutions

### Fix 1: Use isActive for long-running coroutines

```kotlin
// Wrong — never checks for cancellation
val job = launch {
    while (true) {
        process()  // Can't be cancelled
    }
}

// Correct — check isActive
val job = launch {
    while (isActive) {
        process()  // Responds to cancellation
    }
}
```

### Fix 2: Use try-finally for cleanup

```kotlin
// Wrong — resource not released on cancel
val job = launch {
    val resource = acquireResource()
    doWork()
    resource.close()  // May not run
}

// Correct — use finally
val job = launch {
    val resource = acquireResource()
    try {
        doWork()
    } finally {
        resource.close()  // Always runs
    }
}
```

### Fix 3: Re-throw CancellationException

```kotlin
// Wrong — swallowing CancellationException
val job = launch {
    try {
        doWork()
    } catch (e: Exception) {
        println("Error: ${e.message}")  // Catches CancellationException
    }
}

// Correct — rethrow CancellationException
val job = launch {
    try {
        doWork()
    } catch (e: CancellationException) {
        throw e  // Proper cancellation propagation
    } catch (e: Exception) {
        println("Error: ${e.message}")
    }
}
```

### Fix 4: Use isolated scopes for independent work

```kotlin
// Wrong — one failure cancels all
val scope = CoroutineScope(Job())
scope.launch { throw RuntimeException("Error") }
scope.launch { delay(1000) }  // Also cancelled

// Correct — SupervisorJob makes children independent
val scope = CoroutineScope(SupervisorJob())
scope.launch { throw RuntimeException("Error") }
scope.launch { println("I still run") }  // Not affected
```

## Examples

```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    val job = launch {
        try {
            repeat(10) { i ->
                println("Working $i...")
                delay(500)
            }
        } catch (e: CancellationException) {
            println("Coroutine cancelled, cleaning up...")
            throw e
        }
    }

    delay(1200)
    println("Requesting cancellation...")
    job.cancelAndJoin()
    println("Done")
}
```

## Related Errors

- [CancellationException]({{< relref "/languages/kotlin/cancellation-exception" >}}) — general coroutine cancellation.
- [JobCancellationException]({{< relref "/languages/kotlin/job-cancellation" >}}) — job-level cancellation.
- [TimeoutCancellationException]({{< relref "/languages/kotlin/timeout-exception" >}}) — timeout caused cancellation.
