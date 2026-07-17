---
title: "[Solution] Kotlin TimeoutException Fix"
description: "Fix Kotlin TimeoutException when coroutine operations exceed time limits. Learn why timeouts occur and how to handle them."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["timeoutexception", "timeout", "coroutine", "kotlin"]
weight: 5
---

## What This Error Means

A TimeoutException (TimeoutCancellationException) is thrown when a coroutine operation exceeds its specified time limit. This is commonly caused by withTimeout or withTimeoutOrNull.

## Common Causes

- Slow network requests
- Deadlock in coroutine
- Long-running operation without timeout
- Wrong timeout value

## How to Fix

```kotlin
// WRONG: No timeout on potentially slow operation
runBlocking {
    val data = fetchFromNetwork()  // May hang forever
}

// CORRECT: Use withTimeout
runBlocking {
    try {
        val data = withTimeout(5000) {
            fetchFromNetwork()
        }
    } catch (e: TimeoutCancellationException) {
        println("Request timed out")
    }
}
```

```kotlin
// WRONG: Catching all exceptions including cancellation
try {
    withTimeout(1000) {
        delay(2000)
    }
} catch (e: Exception) {
    // Catches CancellationException too
}

// CORRECT: Use withTimeoutOrNull for graceful handling
val result = withTimeoutOrNull(1000) {
    delay(2000)
    "Result"
}
// result is null if timed out
```

## Examples

```kotlin
// Example 1: Basic timeout
runBlocking {
    val result = withTimeout(1000) {
        delay(500)
        "Done"
    }
    println(result)  // "Done"
}

// Example 2: Graceful timeout
val result = withTimeoutOrNull(1000) {
    delay(2000)
    "Done"
}
println(result)  // null

// Example 3: Retry with timeout
suspend fun fetchWithRetry(retries: Int = 3): String {
    repeat(retries) { attempt ->
        try {
            return withTimeout(5000) {
                fetchFromNetwork()
            }
        } catch (e: TimeoutCancellationException) {
            if (attempt == retries - 1) throw e
            delay(1000 * (attempt + 1))
        }
    }
    throw CancellationException("All retries failed")
}
```

## Related Errors

- [CancellationException](cancellationexception-kotlin) — coroutine cancelled
- [IllegalStateException](illegalstateexception-kotlin) — invalid state
- [IllegalArgumentException](illegalargumentexception) — invalid argument
