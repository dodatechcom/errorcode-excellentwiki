---
title: "[Solution] Kotlin Coroutine Timed Out — TimeoutCancellationException Fix"
description: "Fix Kotlin coroutine timeout errors. Increase timeouts, use withTimeoutOrNull, or optimize the operation to complete faster."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["coroutine-timeout", "timeout", "withTimeout", "delay"]
weight: 5
---

# Coroutine Timed Out — TimeoutCancellationException Fix

A "Timed out waiting for" error occurs when a coroutine exceeds the time limit set by `withTimeout` or `withTimeoutOrNull`. This is a `TimeoutCancellationException`, a subclass of `CancellationException`.

## Description

`withTimeout` cancels the coroutine if it doesn't complete within the specified duration. The exception message includes the timeout value. `withTimeoutOrNull` returns `null` instead of throwing.

Common scenarios:

- **Slow network request** — API takes too long.
- **Long computation** — algorithm exceeds time budget.
- **Deadlock** — waiting for resource that never arrives.
- **Timeout too short** — legitimate operation needs more time.

## Common Causes

```kotlin
// Cause 1: Operation too slow
val result = withTimeout(1000) {
    slowApiCall()  // Takes 5 seconds
}

// Cause 2: No suspension point in timeout scope
val result = withTimeout(1000) {
    // Blocking loop without yield(), timeout never checked
    var sum = 0L
    for (i in 1..1_000_000_000) sum += i
}

// Cause 3: Nested timeout
val result = withTimeout(1000) {
    withTimeout(500) {
        delay(2000)  // Inner timeout fires first
    }
}

// Cause 4: Blocking call
val result = withTimeout(1000) {
    Thread.sleep(5000)  // Blocks thread
}
```

## Solutions

### Fix 1: Use withTimeoutOrNull for graceful handling

```kotlin
// Wrong — throws exception
val result = withTimeout(1000) {
    fetchData()
}

// Correct — returns null on timeout
val result = withTimeoutOrNull(1000) {
    fetchData()
}
if (result == null) {
    println("Timed out, using default")
}
```

### Fix 2: Increase timeout for legitimate operations

```kotlin
// Wrong — timeout too short
val result = withTimeout(100) {
    heavyComputation()
}

// Correct — appropriate timeout
val result = withTimeout(10_000) {
    heavyComputation()
}
```

### Fix 3: Add yield() in non-suspending loops

```kotlin
// Wrong — timeout never checked
val result = withTimeout(1000) {
    var sum = 0L
    for (i in 1..1_000_000_000) {
        sum += i
    }
    sum
}

// Correct — yield() allows cancellation check
val result = withTimeout(1000) {
    var sum = 0L
    for (i in 1..1_000_000_000) {
        sum += i
        if (i % 1_000_000 == 0) yield()
    }
    sum
}
```

### Fix 4: Use CancellableContext for blocking

```kotlin
// Wrong — Thread.sleep blocks thread
val result = withTimeout(1000) {
    Thread.sleep(5000)
}

// Correct — use delay (cancellable)
val result = withTimeout(1000) {
    delay(5000)
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
- [SocketTimeoutException]({{< relref "/languages/kotlin/socket-timeout" >}}) — network timeout.
