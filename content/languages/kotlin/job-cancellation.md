---
title: "[Solution] Kotlin JobCancellationException — Job Cancel Fix"
description: "Fix Kotlin JobCancellationException when a coroutine job is cancelled. Handle structured concurrency, check job status, and propagate cancellation."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["jobcancellationexception", "coroutine", "job", "cancel"]
weight: 5
---

# JobCancellationException — Job Cancel Fix

A `JobCancellationException` is thrown when a coroutine job is cancelled. This is a subclass of `CancellationException` and is specifically thrown when `job.cancel()` or `job.cancelAndJoin()` is called.

## Description

Every coroutine has a `Job` that represents its lifecycle. When a job is cancelled (either explicitly or via structured concurrency), all coroutines in that scope receive a `JobCancellationException`. The coroutine should clean up and terminate.

Common scenarios:

- **Explicit job cancellation** — `job.cancel()` called by user code.
- **Structured concurrency** — parent job cancelled, children follow.
- **Exception propagation** — unhandled exception cancels the job.
- **Scope cancellation** — `CoroutineScope.cancel()` cancels all children.

## Common Causes

```kotlin
// Cause 1: Explicit cancellation
val job = launch {
    delay(10000)
    println("Done")
}
job.cancel()  // JobCancellationException thrown in coroutine

// Cause 2: Parent scope cancelled
val scope = CoroutineScope(Dispatchers.Default)
scope.launch {
    delay(10000)
}
scope.cancel()  // All children receive JobCancellationException

// Cause 3: Exception in sibling coroutine
scope.launch {
    throw RuntimeException("Error in sibling")  // Cancels the job
}
// Other coroutines in same scope receive JobCancellationException

// Cause 4: Timeout
val job = launch {
    withTimeout(1000) {
        delay(5000)  // JobCancellationException after 1 second
    }
}
```

## Solutions

### Fix 1: Check job isActive before work

```kotlin
// Wrong — no cancellation check
val job = launch {
    while (true) {
        heavyComputation()
    }
}

// Correct — check isActive
val job = launch {
    while (isActive) {
        heavyComputation()
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

### Fix 3: Handle cancellation in specific scopes

```kotlin
// Wrong — exception in one scope cancels all
val scope = CoroutineScope(Dispatchers.Default)
scope.launch {
    throw RuntimeException("Error")  // Cancels entire scope
}

// Correct — use isolated scopes
val scope1 = CoroutineScope(Dispatchers.Default)
val scope2 = CoroutineScope(Dispatchers.Default)
scope1.launch {
    throw RuntimeException("Error")  // Only cancels scope1
}
```

### Fix 4: Use SupervisorJob for independent children

```kotlin
// Wrong — regular Job cancels all children on failure
val scope = CoroutineScope(Job())
scope.launch {
    throw RuntimeException("Error")  // Cancels all siblings
}

// Correct — SupervisorJob makes children independent
val scope = CoroutineScope(SupervisorJob())
scope.launch {
    throw RuntimeException("Error")  // Only this child fails
}
scope.launch {
    println("This still runs")  // Not affected
}
```

## Examples

```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    val job = launch {
        try {
            repeat(1000) { i ->
                println("Working $i...")
                delay(100)
            }
        } catch (e: CancellationException) {
            println("Cleaning up...")
            // Re-throw for proper cancellation propagation
            throw e
        }
    }

    delay(500)
    println("Requesting cancellation...")
    job.cancelAndJoin()
    println("Job completed")
}
```

## Related Errors

- [CancellationException]({{< relref "/languages/kotlin/cancellation-exception" >}}) — general coroutine cancellation.
- [TimeoutCancellationException]({{< relref "/languages/kotlin/timeout-exception" >}}) — timeout caused cancellation.
- [IllegalStateException]({{< relref "/languages/kotlin/illegal-state" >}}) — job in wrong state.
