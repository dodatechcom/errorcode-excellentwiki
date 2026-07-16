---
title: "[Solution] Kotlin InterruptedException — Thread Interrupt Fix"
description: "Fix Kotlin InterruptedException when a thread is interrupted during a blocking operation. Handle interrupts properly and check interrupt status."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["interruptedexception", "thread", "interrupt", "blocking", "sleep"]
weight: 5
---

# InterruptedException — Thread Interrupt Fix

An `InterruptedException` is thrown when a thread is interrupted while it's in a blocking operation like `Thread.sleep()`, `wait()`, `join()`, or I/O operations.

## Description

Java/Kotlin threads can be interrupted to signal them to stop. When a blocking operation detects the interrupt, it throws `InterruptedException` and clears the interrupt status. This is a checked exception in Java.

Common scenarios:

- **Thread.sleep interrupted** — another thread calls `thread.interrupt()`.
- **Blocking I/O interrupted** — reading from stream while thread is interrupted.
- **Lock acquisition interrupted** — `Lock.lockInterruptibly()` during interruption.
- **Coroutine cancellation** — coroutines use `InterruptedException` internally.

## Common Causes

```kotlin
// Cause 1: Thread.sleep interrupted
val thread = Thread {
    try {
        Thread.sleep(10000)  // InterruptedException if interrupted
        println("Done sleeping")
    } catch (e: InterruptedException) {
        println("Sleep interrupted")
    }
}
thread.start()
thread.interrupt()  // Causes InterruptedException

// Cause 2: Blocking in coroutine scope
val job = launch {
    Thread.sleep(5000)  // Blocks thread, may throw InterruptedException
}

// Cause 3: Waiting on condition
val lock = Any()
synchronized(lock) {
    lock.wait()  // InterruptedException if interrupted while waiting
}

// Cause 4: Blocking queue
val queue = LinkedBlockingQueue<String>()
queue.take()  // InterruptedException if interrupted while waiting
```

## Solutions

### Fix 1: Handle InterruptedException properly

```kotlin
// Wrong — swallowing interrupt
try {
    Thread.sleep(1000)
} catch (e: InterruptedException) {
    // Ignoring interrupt
}

// Correct — restore interrupt status
try {
    Thread.sleep(1000)
} catch (e: InterruptedException) {
    Thread.currentThread().interrupt()  // Restore interrupt status
    println("Interrupted, cleaning up...")
}
```

### Fix 2: Use cancellation-aware operations in coroutines

```kotlin
// Wrong — Thread.sleep in coroutine (blocks thread)
val job = launch {
    Thread.sleep(5000)
}

// Correct — use delay (cancellable)
val job = launch {
    delay(5000)  // Responds to coroutine cancellation
}
```

### Fix 3: Check interrupt status in loops

```kotlin
// Wrong — doesn't check for interruption
while (true) {
    processItem()
}

// Correct — check interrupt status
while (!Thread.currentThread().isInterrupted) {
    processItem()
}
```

### Fix 4: Use interruptible channels

```kotlin
// Wrong — blocking channel operation
val channel = Channel<Int>()
val value = channel.receive()  // May block indefinitely

// Correct — with timeout
val value = withTimeoutOrNull(5000) {
    channel.receive()
}
```

## Examples

```kotlin
import kotlin.concurrent.thread

fun main() {
    val worker = thread {
        try {
            println("Working...")
            Thread.sleep(2000)
            println("Done")
        } catch (e: InterruptedException) {
            println("Worker interrupted")
            Thread.currentThread().interrupt()
        }
    }

    Thread.sleep(500)
    println("Interrupting worker...")
    worker.interrupt()
    worker.join()
    println("Main done")
}
```

## Related Errors

- [CancellationException]({{< relref "/languages/kotlin/cancellation-exception" >}}) — coroutine cancellation mechanism.
- [ThreadDeath]({{< relref "/languages/kotlin/runtime-exception" >}}) — thread terminated.
- [IOException]({{< relref "/languages/kotlin/io-exception" >}}) — blocking I/O operation.
