---
title: "[Solution] Kotlin select Expression — Multiple Await Clause Conflict"
description: "Fix Kotlin select expression conflicts with multiple await clauses. Learn correct select usage for channel and deferred operations."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1013
---

## What This Error Means

The `select` expression allows waiting for multiple suspendable operations simultaneously. Conflicts arise when multiple clauses match at once, clauses reference closed channels, or the select body modifies shared state unsafely.

## Common Causes

- Multiple channels ready simultaneously causing non-deterministic selection
- Selecting on a channel that gets closed before clause is evaluated
- Clause body throwing exceptions that aren't caught
- Using `onSend` on channels with different element types

```kotlin
// Multiple clauses may fire non-deterministically
select<Unit> {
    channel1.onReceive { process1(it) }
    channel2.onReceive { process2(it) }
    // Which one fires if both are ready? Non-deterministic
}
```

## How to Fix

**1. Handle all possible clause outcomes**

```kotlin
select<Unit> {
    channel1.onReceiveOrNull { value ->
        if (value != null) process1(value) else handleClose1()
    }
    channel2.onReceiveOrNull { value ->
        if (value != null) process2(value) else handleClose2()
    }
}
```

**2. Use onTimeout to avoid indefinite waits**

```kotlin
select<Unit> {
    channel.onReceive { process(it) }
    onTimeout(5000) {
        println("No data received within 5 seconds")
    }
}
```

**3. Process multiple channels sequentially**

```kotlin
// Instead of select, drain channels one at a time
for (msg in channel1) { process1(msg) }
for (msg in channel2) { process2(msg) }
```

**4. Use FairChannel or rendezvous for predictable ordering**

```kotlin
val channel = Channel<Int>(Channel.RENDEZVOUS)
// Guarantees one send matches one receive
```

## Examples

```kotlin
// Example 1: select with timeout
suspend fun fetchWithTimeout(
    primary: Channel<Data>,
    fallback: Channel<Data>,
    timeoutMs: Long
): Data = select {
    primary.onReceive { it }
    fallback.onReceive { it }
    onTimeout(timeoutMs) { throw TimeoutException() }
}

// Example 2: Select for send
select<Unit> {
    channel.onSend(result) { println("Sent") }
    onTimeout(1000) { println("Send timeout") }
}

// Example 3: Fair multiplexing
fun <T> multiplex(vararg channels: Channel<T>): Channel<T> = Channel(Channel.UNLIMITED).also { output ->
    CoroutineScope(SupervisorJob()).launch {
        channels.forEach { ch ->
            launch {
                for (item in ch) output.send(item)
            }
        }
    }
}
```

## Related Errors

- [Channel error](kotlin-channel-error) — channel communication error
- [CancellationException](cancellationexception-kotlin) — coroutine cancelled
- [Flow backpressure error](kotlin-flow-backpressure) — flow emission issue
