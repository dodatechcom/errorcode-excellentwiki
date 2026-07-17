---
title: "[Solution] Kotlin Channel Send/Receive Error Fix"
description: "Fix Kotlin Channel errors when sending or receiving. Learn why Channel operations fail and how to use Channels properly."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Channel error occurs when send or receive operations on a Channel fail. Channels are used for coroutine communication and can fail due to capacity issues or closed channels.

## Common Causes

- Sending to closed channel
- Receiving from closed channel
- Channel capacity exceeded
- Wrong channel type

## How to Fix

```kotlin
// WRONG: Sending to closed channel
val channel = Channel<Int>()
channel.close()
channel.send(1)  // ClosedSendChannelException

// CORRECT: Check if closed
if (!channel.isClosedForSend) {
    channel.send(1)
}
```

```kotlin
// WRONG: Receiving from closed channel
val channel = Channel<Int>()
channel.close()
val value = channel.receive()  // ClosedReceiveChannelException

// CORRECT: Use receiveOrNull
val value = channel.receiveOrNull()  // null if closed
```

## Examples

```kotlin
// Example 1: Basic Channel
val channel = Channel<Int>()

launch {
    for (i in 1..5) {
        channel.send(i)
    }
    channel.close()
}

launch {
    for (value in channel) {
        println(value)
    }
}

// Example 2: Buffered channel
val channel = Channel<Int>(capacity = 10)

// Example 3: Rendezvous channel
val channel = Channel<Int>()  // capacity = 0
```

## Related Errors

- [Flow collection error](flow-error) — Flow issue
- [kotlinx.coroutines error](kotlinx-coroutines-error) — coroutine error
- [CoroutineScope cancelled error](coroutine-scope-error) — scope cancelled
