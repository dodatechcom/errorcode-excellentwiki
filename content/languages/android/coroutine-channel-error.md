---
title: "Coroutine Channel Error"
description: "Fix Kotlin coroutine Channel and Flow backpressure errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Channel operations fail with closed channel or backpressure issues

## Common Causes

- Sending to a closed channel
- Channel buffer overflow without overflow strategy
- Receive never called causing sender to suspend
- Using Channel when Flow would be more appropriate

## Fixes

- Check channel isOpen before sending
- Configure buffer and overflow strategy
- Always have matching receive calls
- Prefer Flow for cold data streams

## Code Example

```kotlin
// Buffer and overflow strategy
val channel = Channel<Int>(capacity = 10, onBufferOverflow = BufferOverflow.DROP_OLDEST)

// Sender
launch {
    for (i in 1..100) {
        channel.send(i)  // Drops oldest if buffer full
    }
    channel.close()
}

// Receiver
launch {
    for (value in channel) {
        process(value)
    }
}
```

# Channel is hot (eagerly active)
# Flow is cold (lazy, only runs on collect)
# Use Flow for most reactive patterns
