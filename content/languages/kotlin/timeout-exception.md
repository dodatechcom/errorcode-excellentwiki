---
title: "[Solution] Kotlin TimeoutCancellationException — Coroutine Timeout Fix"
description: "Fix Kotlin TimeoutCancellationException when a coroutine exceeds its time limit. Increase timeout, use withTimeoutOrNull, or optimize the operation."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["timeoutcancellationexception", "coroutine", "timeout", "withtimeout"]
weight: 5
---

# TimeoutCancellationException — Coroutine Timeout Fix

A `TimeoutCancellationException` is thrown when a coroutine exceeds the time limit specified by `withTimeout` or `withTimeoutOrNull`. This is a subclass of `CancellationException`.

## Description

Kotlin's `withTimeout` function cancels the coroutine if it doesn't complete within the specified duration. The exception includes the timeout value. `withTimeoutOrNull` returns `null` instead of throwing.

Common scenarios:

- **Slow network request** — API call takes too long.
- **Long-running computation** — algorithm exceeds time budget.
- **Deadlock detection** — waiting for a resource that never becomes available.
- **Resource cleanup timeout** — shutdown doesn't complete in time.

## Common Causes

```kotlin
// Cause 1: Operation takes longer than timeout
val result = withTimeout(1000) {
    slowNetworkCall()  // Takes 5 seconds, timeout after 1 second
}

// Cause 2: No cancellation point in timeout scope
val result = withTimeout(1000) {
    // This loop has no suspension point, timeout never checked
    var sum = 0L
    for (i in 1..1_000_000_000) sum += i
}

// Cause 3: Nested timeout
val result = withTimeout(1000) {
    withTimeout(500) {
        delay(2000)  // Inner timeout fires first
    }
}

// Cause 4: Blocking call inside withTimeout
val result = withTimeout(1000) {
    Thread.sleep(5000)  // Blocks thread, doesn't respond to cancellation
}
```

## Solutions

### Fix 1: Use withTimeoutOrNull for graceful handling

```kotlin
// Wrong — throws TimeoutCancellationException
val result = withTimeout(1000) {
    fetchData()
}

// Correct — returns null on timeout
val result = withTimeoutOrNull(1000) {
    fetchData()
}
if (result == null) {
    println("Request timed out, using default")
}
```

### Fix 2: Increase timeout for legitimate slow operations

```kotlin
// Wrong — timeout too short
val result = withTimeout(100) {
    heavyComputation()  // Takes 5 seconds
}

// Correct — appropriate timeout
val result = withTimeout(10_000) {
    heavyComputation()
}
```

### Fix 3: Add cancellation checks in non-suspending loops

```kotlin
// Wrong — timeout never checked
val result = withTimeout(1000) {
    var sum = 0L
    for (i in 1..1_000_000_000) {
        sum += i  // No suspension point
    }
    sum
}

// Correct — add yield() for cancellation checks
val result = withTimeout(1000) {
    var sum = 0L
    for (i in 1..1_000_000_000) {
        sum += i
        if (i % 1_000_000 == 0) yield()  // Allows cancellation check
    }
    sum
}
```

### Fix 4: Use CancellableContext for blocking calls

```kotlin
// Wrong — Thread.sleep doesn't respond to cancellation
val result = withTimeout(1000) {
    Thread.sleep(5000)
}

// Correct — use delay (cancellable) or interrupt
val result = withTimeout(1000) {
    delay(5000)  // Cancellable
}

// If you must use blocking
val result = withTimeout(1000) {
    withContext(Dispatchers.IO) {
        Thread.sleep(5000)  // May still block, but different thread
    }
}
```

## Examples

```kotlin
import kotlinx.coroutines.*

suspend fun fetchData(): String {
    delay(2000)  // Simulate slow network
    return "data"
}

fun main() = runBlocking {
    // Handle timeout gracefully
    val result = withTimeoutOrNull(1000) {
        fetchData()
    }

    when (result) {
        null -> println("Timed out, using cached data")
        else -> println("Got: $result")
    }
}
```

## Related Errors

- [CancellationException]({{< relref "/languages/kotlin/cancellation-exception" >}}) — general coroutine cancellation.
- [JobCancellationException]({{< relref "/languages/kotlin/job-cancellation" >}}) — job-level cancellation.
- [CancellationException]({{< relref "/languages/kotlin/cancellation-exception" >}}) — timeout causes cancellation.
