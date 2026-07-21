---
title: "[Solution] Deprecated Function Migration: Thread.stop/suspend/resume to interruption"
description: "Migrate from deprecated Thread.stop/suspend/resume to thread interruption in Java."
deprecated_function: "Thread.stop(), Thread.suspend()"
replacement_function: "Thread.interrupt()"
languages: ["java"]
deprecated_since: "Java 1.2+"
---

# [Solution] Deprecated Function Migration: Thread.stop/suspend/resume to interruption

The `Thread.stop(), Thread.suspend()` has been deprecated in favor of `Thread.interrupt()`.

## Migration Guide

Thread.stop() releases all locks immediately. Use thread interruption with cooperative checks instead.

## Before (Deprecated)

```java
Thread t = new Thread(() -> {
    while (true) doWork();
});
t.start();
t.suspend();  // Can cause deadlocks
t.resume();
t.stop();     // Releases locks mid-operation
```

## After (Modern)

```java
Thread t = new Thread(() -> {
    while (!Thread.currentThread().isInterrupted()) {
        doWork();
    }
});
t.start();

// Graceful pause -- cooperative
t.interrupt();

// For blocking operations
try {
    TimeUnit.SECONDS.sleep(10);
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
}
```

## Key Differences

- Thread.stop() deprecated (removed in Java 18+)
- Thread.suspend()/resume() deprecated
- Use interrupt flag for cooperative cancellation
