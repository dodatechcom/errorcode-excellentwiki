---
title: "[Solution] Kotlin CancellationException Fix"
description: "Fix Kotlin CancellationException when coroutines are cancelled. Learn why coroutine cancellation happens and how to handle it."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A CancellationException is thrown when a coroutine is cancelled. This is the standard way to cancel coroutines in Kotlin coroutines, and it propagates through the coroutine hierarchy.

## Common Causes

- Job cancelled by parent coroutine
- Timeout exception (TimeoutCancellationException)
- Manual cancellation
- Structured concurrency cleanup

## How to Fix

```kotlin
// WRONG: Swallowing CancellationException
try {
    delay(1000)
} catch (e: Exception) {
    // Catches CancellationException too, breaking cancellation
}

// CORRECT: Re-throw CancellationException
try {
    delay(1000)
} catch (e: CancellationException) {
    throw e  // Re-throw to preserve cancellation
} catch (e: Exception) {
    // Handle other exceptions
}
```

```kotlin
// WRONG: Not using coroutineScope
fun processData() = runBlocking {
    launch {
        delay(1000)
        println("Done")
    }
    throw CancellationException("Cancelled")
    // Launched coroutine continues!
}

// CORRECT: Use coroutineScope
fun processData() = runBlocking {
    coroutineScope {
        launch {
            delay(1000)
            println("Done")
        }
        throw CancellationException("Cancelled")
        // Both coroutines cancelled
    }
}
```

## Examples

```kotlin
// Example 1: Manual cancellation
val job = launch {
    repeat(1000) { i ->
        println("Job: $i")
        delay(500)
    }
}
delay(2000)
job.cancel()

// Example 2: Timeout
try {
    withTimeout(1000) {
        delay(2000)
    }
} catch (e: TimeoutCancellationException) {
    println("Timed out")
}

// Example 3: Cleanup in finally
val job = launch {
    try {
        longRunningOperation()
    } finally {
        // Cleanup code
        println("Cleaning up")
    }
}
```

## Related Errors

- [TimeoutException](timeoutexception-kotlin) — coroutine timeout
- [IllegalStateException](illegalstateexception-kotlin) — invalid state
- [Job cancellation] — structured concurrency cleanup
