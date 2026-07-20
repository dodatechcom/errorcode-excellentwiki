---
title: "[Solution] Kotlin AbortFlowException: Flow is aborted"
description: "Fix kotlinx.coroutines.flow.internal.AbortFlowException errors caused by Flow backpressure issues. Learn how to properly handle Flow collection and terminal operators."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# AbortFlowException: Flow is aborted

An `AbortFlowException` is thrown internally by kotlinx.coroutines when a `Flow` collector aborts collection, typically due to backpressure or misuse of terminal operators.

## Error Message

```
kotlinx.coroutines.flow.internal.AbortFlowException: Flow is aborted
```

## Description

This is an internal exception thrown by the Flow operator pipeline. It occurs when a collector signals that it no longer wants to receive emissions, often due to exceeding buffer capacity, cancelling the collector's scope, or using incompatible operators. You should not catch this exception directly. Instead, fix the Flow chain that triggers it.

## Common Causes

- Buffer overflow without buffering strategy
- Collecting a Flow in a cancelled scope
- Using `take()` or `first()` that completes early while upstream emits
- Conflating or buffering Flow with insufficient capacity
- Multiple collectors on a single `SharedFlow` without replay

## Solutions

### Solution 1: Use buffer operators to prevent overflow

Add `buffer()` operators between slow producers and consumers to decouple them.

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*

fun slowProducer(): Flow<Int> = flow {
    for (i in 1..100) {
        delay(100) // Slow emission
        emit(i)
    }
}

fun main() = runBlocking {
    slowProducer()
        .buffer(capacity = 50) // Buffer between producer and consumer
        .collect { value ->
            println("Collected: $value")
            delay(200) // Slow collection
        }
}
```

### Solution 2: Use conflate to skip intermediate values

When only the latest value matters, use `conflate()` to merge or skip intermediate emissions.

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*

fun main() = runBlocking {
    val numbers = flow {
        for (i in 1..10) {
            delay(10)
            emit(i)
        }
    }

    numbers
        .conflate() // Drops intermediate values when collector is slow
        .collect { value ->
            delay(50) // Simulate slow processing
            println("Received: $value")
        }
}
```

### Solution 3: Use proper terminal operators

Ensure terminal operators like `first()`, `take()`, and `single()` are used correctly so the upstream Flow knows when to stop.

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*

fun main() = runBlocking {
    val numbers = flow {
        for (i in 1..10) {
            emit(i)
        }
    }

    // Use first() to get only the first matching element
    val firstEven = numbers.first { it % 2 == 0 }
    println("First even: $firstEven")

    // Use take() to limit emissions
    numbers.take(3).collect { println(it) }
}
```

## Prevention Tips

- Always use `buffer()`, `conflate()`, or `debounce()` when producer and consumer have different speeds
- Never catch `AbortFlowException` directly — fix the upstream Flow instead
- Use `stateIn` and `shareIn` for sharing Flows across multiple collectors
- Test Flow chains with `flowOf()` and known data sizes before production

## Related Errors

- [IllegalStateException]({{< relref "/languages/kotlin/illegal-state" >}}) — invalid state in Flow collection.
- [CancellationException]({{< relref "/languages/kotlin/cancellation-exception" >}}) — coroutine scope cancelled during collection.
- [TimeoutCancellationException]({{< relref "/languages/kotlin/timeout-exception" >}}) — timeout while collecting a Flow.
