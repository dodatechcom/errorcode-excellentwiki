---
title: "[Solution] Java InterruptedException — Thread Interrupt Fix"
description: "Fix Java InterruptedException by properly handling thread interrupts, restoring interrupt status, and using interrupt-aware APIs instead of swallowing the exception."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
tags: ["interruptedexception", "thread", "interrupt", "concurrency"]
weight: 5
---

# InterruptedException — Thread Interrupt Fix

An `InterruptedException` is thrown when a thread is interrupted while it is sleeping, waiting, or otherwise blocked in an interruptible operation. It is a checked exception and signals that another thread has requested the current thread to stop.

## Description

This exception is part of Java's concurrency API. It fires when `Thread.interrupt()` is called on a thread that is in one of these states:

- `Thread.sleep()`
- `Object.wait()`
- `Thread.join()`
- Blocking `I/O` (e.g., `InputStream.read()`)
- `Lock.lockInterruptibly()`
- `Future.get()`

The critical detail: **catching and swallowing `InterruptedException` clears the interrupt flag**, silently preventing higher-level code from detecting the interrupt.

## Common Causes

```java
// Cause 1: Swallowing InterruptedException (most common bug)
try {
    Thread.sleep(1000);
} catch (InterruptedException e) {
    // Bad: interrupt flag is now cleared
}

// Cause 2: Calling interruptible method without handling the exception
public void waitForData(Queue<String> queue) throws InterruptedException {
    String data = queue.take();  // InterruptedException if interrupted
}

// Cause 3: Thread pool task ignoring interrupts
ExecutorService executor = Executors.newSingleThreadExecutor();
executor.submit(() -> {
    while (running) {
        processNext();  // May block and throw InterruptedException
    }
});

// Cause 4: Nested interruptible calls without re-interrupting
public void loadData() {
    try {
        Thread.sleep(5000);  // InterruptedException
        fetchFromDatabase();  // Another interruptible call
    } catch (InterruptedException e) {
        // Forgot to re-interrupt — interrupt is lost
    }
}
```

## Solutions

### Fix 1: Re-set the interrupt flag when catching InterruptedException

```java
// Wrong — swallows the interrupt
try {
    Thread.sleep(1000);
} catch (InterruptedException e) {
    log.warn("Sleep interrupted");
}

// Correct — preserves the interrupt status
try {
    Thread.sleep(1000);
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();  // Re-set the flag
    log.warn("Sleep interrupted");
}
```

### Fix 2: Propagate the exception instead of catching it

```java
// Correct — let the caller decide how to handle the interrupt
public void pollQueue() throws InterruptedException {
    String item = queue.poll(5, TimeUnit.SECONDS);
    if (item != null) {
        process(item);
    }
}
```

### Fix 3: Use `Thread.currentThread().interrupt()` in catch blocks

```java
public void run() {
    while (!Thread.currentThread().isInterrupted()) {
        try {
            Task task = taskQueue.take();
            task.execute();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();  // Restore interrupt
            break;  // Exit the loop
        }
    }
    cleanup();
}
```

### Fix 4: Use `ExecutorService.shutdownNow()` to interrupt tasks

```java
ExecutorService executor = Executors.newFixedThreadPool(4);
executor.submit(this::processData);

// To stop gracefully
executor.shutdownNow();  // Sends interrupt to all running tasks
executor.awaitTermination(10, TimeUnit.SECONDS);
```

## Prevention Checklist

- Never catch `InterruptedException` without either re-setting the interrupt flag or re-throwing.
- Declare `throws InterruptedException` on methods that call interruptible APIs.
- Use `Thread.currentThread().interrupt()` in catch blocks to preserve the interrupt.
- Check `Thread.currentThread().isInterrupted()` in long-running loops.

## Related Errors

- [ThreadDeath](../threaddeath) — deprecated thread termination mechanism.
- [IllegalMonitorStateException](../illegalmonitorenterexception) — related to synchronization failures.
- [IOException](../ioexception) — blocking I/O may throw InterruptedException indirectly.
