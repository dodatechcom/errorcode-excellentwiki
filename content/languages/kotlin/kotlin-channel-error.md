---
title: "[Solution] Kotlin Channel Closed Send/Receive, Buffer Overflow"
description: "Fix Kotlin channel errors including closed send/receive and buffer overflow. Learn trySend, tryReceive, and channel capacity patterns."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1014
---

## What This Error Means

Channel errors occur when sending to a closed channel, receiving from a closed channel, or exceeding channel buffer capacity. These are common in producer-consumer patterns with coroutines.

## Common Causes

- Sending to a channel after `close()` has been called
- Calling `receive()` on a closed, empty channel
- Buffer overflow with `BUFFERED` or fixed-capacity channels
- Using `send()` on a full `CONFLATED` channel with wrong element type

```kotlin
val channel = Channel<Int>()
channel.close()
channel.send(1)  // ClosedSendChannelException
```

## How to Fix

**1. Use trySend/tryReceive for non-blocking operations**

```kotlin
// WRONG: Suspending send may throw
channel.send(data)

// CORRECT: Non-blocking with result check
val result = channel.trySend(data)
if (result.isFailure) {
    handleSendFailure(result.exceptionOrNull())
}
```

**2. Check channel state before operations**

```kotlin
if (!channel.isClosedForSend) {
    channel.send(data)
}
```

**3. Handle closed channel on receive side**

```kotlin
// WRONG: Throws on closed channel
val value = channel.receive()

// CORRECT: Use receiveOrNull
val value = channel.receiveOrNull()
if (value == null) {
    println("Channel closed, no more data")
}
```

**4. Choose appropriate channel capacity**

```kotlin
// Rendezvous (zero capacity) — requires direct handoff
val rendezvous = Channel<Int>()

// Buffered — default 64 elements
val buffered = Channel<Int>(Channel.BUFFERED)

// Unlimited — no backpressure
val unlimited = Channel<Int>(Channel.UNLIMITED)

// Conflated — keeps latest only
val conflated = Channel<Int>(Channel.CONFLATED)
```

## Examples

```kotlin
// Example 1: Safe producer with trySend
launch {
    for (item in data) {
        val result = channel.trySend(item)
        if (result.isClosed) break
    }
}

// Example 2: Consumer with iterator
launch {
    for (value in channel) {
        process(value)
    }
    // Channel automatically closes when iteration completes
}

// Example 3: Fan-out pattern with multiple consumers
val workChannel = Channel<Work>(100)
repeat(4) { workerId ->
    launch {
        for (work in workChannel) {
            process(work, workerId)
        }
    }
}
```

## Related Errors

- [CancellationException](cancellationexception-kotlin) — coroutine cancelled
- [kotlinx.coroutines error](kotlinx-coroutines-error) — coroutine error
- [Flow backpressure error](kotlin-flow-backpressure) — flow emission issue
