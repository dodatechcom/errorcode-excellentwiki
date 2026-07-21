---
title: "Coroutine Actor Pattern Error"
description: "Fix Kotlin coroutine actor pattern implementation for sequential state access"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Coroutine actor pattern produces race conditions or deadlocks

## Common Causes

- Actor not properly serializing access to shared state
- Channel capacity too small causing sender to block
- Actor scope not properly managed
- Close signal not sent to actor coroutine

## Fixes

- Use actor with unlimited or buffered channel
- Send close signal when actor is no longer needed
- Use mutex for simple state protection
- Choose between actor and Mutex based on complexity

## Code Example

```kotlin
// Actor pattern for serial access
val counterActor = actor<Int>(capacity = Channel.UNLIMITED) {
    var count = 0
    for (msg in channel) {
        count += msg
        println("Count: $count")
    }
}

// Usage:
counterActor.send(1)
counterActor.send(2)
counterActor.close()

// Simpler alternative - Mutex:
val mutex = Mutex()
var counter = 0

suspend fun increment() = mutex.withLock {
    counter++
}
```

# Actor: serial processing of messages
# Mutex: simple mutual exclusion
# Channel capacity: BUFFERED, UNLIMITED, or fixed
