---
title: "[Solution] Java FileLockInterruptionException — File Lock Interrupt Fix"
description: "Fix Java FileLockInterruptionException by handling interruption gracefully, releasing locks properly, and coordinating interrupts with locking."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# FileLockInterruptionException — File Lock Interrupt Fix

A `FileLockInterruptionException` is thrown when a thread is interrupted while waiting to acquire a file lock. This is a checked exception specific to the `java.nio.channels` file locking mechanism.

## Description

`java.nio.channels.FileLockInterruptionException` extends `AsynchronousCloseException` and is thrown by `FileChannel.lock()` and `FileChannel.tryLock()` when the waiting thread receives an interrupt. The lock acquisition is cancelled and the channel remains open.

Common message variants:

- `java.nio.channels.FileLockInterruptionException`
- `Interrupted while waiting for lock`

## Common Causes

```java
// Cause 1: Interrupting thread waiting for exclusive lock
FileChannel channel = FileChannel.open(path, StandardOpenOption.WRITE);
Thread t = new Thread(() -> {
    try {
        FileLock lock = channel.lock();  // Blocks if lock held by another process
    } catch (FileLockInterruptionException e) {
        // Interrupted while waiting
    }
});
t.start();
t.interrupt();  // Interrupts the waiting thread

// Cause 2: Executor shutdown interrupts lock acquisition
ExecutorService pool = Executors.newSingleThreadExecutor();
pool.submit(() -> {
    try (FileChannel ch = FileChannel.open(path, StandardOpenOption.WRITE)) {
        FileLock lock = ch.lock();  // Blocks
        // Work with locked file
    }
});
pool.shutdownNow();  // Interrupts thread — FileLockInterruptionException

// Cause 3: tryLock() with interrupt during contention
FileChannel ch1 = FileChannel.open(path, StandardOpenOption.WRITE);
FileChannel ch2 = FileChannel.open(path, StandardOpenOption.WRITE);
FileLock lock1 = ch1.lock();  // Holds lock

// ch2.tryLock() should return null, but lock() would block
// Using lock() on ch2 — then interrupting
Thread t = new Thread(() -> {
    try {
        FileLock lock2 = ch2.lock();  // Blocks waiting for lock1
    } catch (FileLockInterruptionException e) {
        // Interrupted
    }
});
t.start();
t.interrupt();

// Cause 4: Distributed lock file contention
// Multiple processes competing for same lock file
// Thread interrupted during long wait
```

## Solutions

### Fix 1: Handle FileLockInterruptionException with proper cleanup

```java
FileChannel channel = FileChannel.open(path, StandardOpenOption.WRITE);
FileLock lock = null;

try {
    lock = channel.lock();
    // Work with locked file
    processFile(channel);
} catch (FileLockInterruptionException e) {
    Thread.currentThread().interrupt();  // Preserve interrupt status
    System.err.println("Lock acquisition interrupted");
} finally {
    if (lock != null && lock.isValid()) {
        lock.release();
    }
    channel.close();
}
```

### Fix 2: Use tryLock() with non-blocking acquisition

```java
FileChannel channel = FileChannel.open(path, StandardOpenOption.WRITE);
try {
    FileLock lock = channel.tryLock();  // Returns null immediately if unavailable
    if (lock == null) {
        System.out.println("Could not acquire lock — file is locked");
        return;
    }
    try {
        processFile(channel);
    } finally {
        lock.release();
    }
} catch (IOException e) {
    // Handle lock failure
}
```

### Fix 3: Use tryLock with timeout via polling

```java
public static FileLock lockWithTimeout(FileChannel channel,
        long timeoutMs) throws IOException, InterruptedException {
    long deadline = System.currentTimeMillis() + timeoutMs;
    int delay = 100;

    while (System.currentTimeMillis() < deadline) {
        FileLock lock = channel.tryLock();
        if (lock != null) return lock;

        Thread.sleep(delay);
        delay = Math.min(delay * 2, 1000);
    }
    throw new IOException("Could not acquire lock within " + timeoutMs + "ms");
}

// Usage
try (FileChannel channel = FileChannel.open(path, StandardOpenOption.WRITE)) {
    FileLock lock = lockWithTimeout(channel, 5000);
    try {
        processFile(channel);
    } finally {
        lock.release();
    }
}
```

### Fix 4: Coordinate interrupts with lock lifecycle

```java
public class LockManager {
    private final AtomicBoolean shuttingDown = new AtomicBoolean(false);

    public void executeWithLock(Path path, Runnable task) throws IOException {
        if (shuttingDown.get()) {
            throw new IOException("Lock manager is shutting down");
        }

        try (FileChannel channel = FileChannel.open(path,
                StandardOpenOption.WRITE)) {
            FileLock lock = channel.lock();
            try {
                task.run();
            } finally {
                lock.release();
            }
        } catch (FileLockInterruptionException e) {
            if (!shuttingDown.get()) {
                Thread.currentThread().interrupt();
            }
            // Expected during shutdown — don't rethrow
        }
    }

    public void shutdown() {
        shuttingDown.set(true);
    }
}
```

### Fix 5: Use try-finally to guarantee lock release

```java
FileChannel channel = null;
FileLock lock = null;

try {
    channel = FileChannel.open(path, StandardOpenOption.WRITE);
    lock = channel.lock();
    processFile(channel);
} catch (FileLockInterruptionException e) {
    Thread.currentThread().interrupt();
} finally {
    if (lock != null && lock.isValid()) {
        try { lock.release(); } catch (IOException e) { /* log */ }
    }
    if (channel != null) {
        try { channel.close(); } catch (IOException e) { /* log */ }
    }
}
```

## Prevention Checklist

- Always release `FileLock` in a `finally` block or use try-with-resources.
- Use `tryLock()` instead of `lock()` when interruptibility is a concern.
- Handle `FileLockInterruptionException` by re-setting the interrupt flag.
- Check `lock.isValid()` before calling `lock.release()`.
- Avoid interrupting threads that are waiting for file locks when possible.

## Related Errors

- [OverlappingFileLockException](../overlappingfilelockexception) — locking overlapping regions in same JVM.
- [ClosedByInterruptException](../closedbyinterruptexception) — channel closed by interrupt.
- [AsynchronousCloseException](../asynchronouscloseexception) — channel closed during blocking operation.
- [IOException](../ioexception) — parent class for all I/O failures.
