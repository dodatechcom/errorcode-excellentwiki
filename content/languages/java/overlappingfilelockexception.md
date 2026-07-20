---
title: "[Solution] Java OverlappingFileLockException — NIO File Lock Fix"
description: "Fix Java OverlappingFileLockException by checking existing locks, releasing before reacquiring, and using tryLock() for non-blocking acquisition."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# OverlappingFileLockException — NIO File Lock Fix

An `OverlappingFileLockException` is thrown when an attempt is made to acquire a file lock that overlaps an existing lock held by the same JVM on the same file region. This includes attempts to acquire a lock on a region that overlaps an existing lock, or a whole-file lock when a region lock is held.

## Description

`java.nio.channels.OverlappingFileLockException` is an unchecked exception extending `java.lang.IllegalStateException`. It is thrown by `FileChannel.lock()` and `FileChannel.tryLock()` when:

- A lock is already held by the same JVM on overlapping bytes of the same file
- A whole-file lock is requested while a region lock exists (or vice versa)
- The same thread attempts to reacquire a lock on an already-locked region

Note: Different JVMs can lock overlapping regions of the same file — this exception is only for locks within the same JVM.

Common message variants:

- `java.nio.channels.OverlappingFileLockException`
- `Overlapping file locks`

## Common Causes

```java
// Cause 1: Acquiring a second lock on the same region
FileChannel channel = FileChannel.open(path, StandardOpenOption.READ, StandardOpenOption.WRITE);
FileLock lock1 = channel.lock(0, Long.MAX_VALUE, false);
FileLock lock2 = channel.lock(0, 100, false);  // OverlappingFileLockException

// Cause 2: Locking the whole file when a region lock exists
FileChannel ch1 = FileChannel.open(path, StandardOpenOption.READ, StandardOpenOption.WRITE);
FileLock regionLock = ch1.lock(10, 20, false);
FileLock wholeLock = ch1.lock();  // OverlappingFileLockException

// Cause 3: Same channel reacquiring lock without releasing
FileChannel channel = FileChannel.open(path, StandardOpenOption.READ, StandardOpenOption.WRITE);
FileLock lock = channel.lock();
lock = channel.lock();  // OverlappingFileLockException

// Cause 4: Different channels from the same JVM on the same file
FileChannel ch1 = FileChannel.open(path, StandardOpenOption.READ, StandardOpenOption.WRITE);
FileChannel ch2 = FileChannel.open(path, StandardOpenOption.READ, StandardOpenOption.WRITE);
FileLock lock1 = ch1.lock(0, 100, false);
FileLock lock2 = ch2.lock(0, 50, false);  // OverlappingFileLockException
```

## Solutions

### Fix 1: Release the existing lock before acquiring a new one

```java
FileChannel channel = FileChannel.open(path, StandardOpenOption.READ, StandardOpenOption.WRITE);
FileLock lock = channel.lock(0, 100, false);

// Release before reacquiring
lock.release();
FileLock newLock = channel.lock(0, 200, false);
```

### Fix 2: Use tryLock() for non-blocking lock acquisition

```java
FileChannel channel = FileChannel.open(path, StandardOpenOption.READ, StandardOpenOption.WRITE);
FileLock existingLock = channel.tryLock(0, 100, false);

if (existingLock != null) {
    // Lock acquired successfully
    try {
        processFile(channel);
    } finally {
        existingLock.release();
    }
} else {
    // Lock is held by another process/JVM — retry or skip
    System.out.println("File is locked by another process");
}
```

### Fix 3: Track lock state to prevent reacquisition

```java
public class FileLockManager {
    private final FileChannel channel;
    private volatile FileLock currentLock;

    public synchronized void acquireLock(long position, long size, boolean shared)
            throws IOException {
        if (currentLock != null && currentLock.isValid()) {
            if (overlaps(currentLock.position(), currentLock.size(), position, size)) {
                throw new IllegalStateException("Lock already held on overlapping region");
            }
        }
        currentLock = channel.lock(position, size, shared);
    }

    public synchronized void releaseLock() throws IOException {
        if (currentLock != null && currentLock.isValid()) {
            currentLock.release();
            currentLock = null;
        }
    }

    private boolean overlaps(long pos1, long size1, long pos2, long size2) {
        return pos1 < pos2 + size2 && pos2 < pos1 + size1;
    }
}
```

### Fix 4: Use whole-file locking with care

```java
FileChannel channel = FileChannel.open(path, StandardOpenOption.READ, StandardOpenOption.WRITE);

try {
    FileLock lock = channel.lock();  // Lock entire file
    try {
        processFile(channel);
    } finally {
        lock.release();
    }
} catch (OverlappingFileLockException e) {
    // File already locked by this JVM
    System.err.println("File is already locked in this JVM");
}
```

## Prevention Checklist

- Release file locks as soon as the protected operation completes.
- Use `tryLock()` instead of `lock()` when you need non-blocking behavior.
- Track which regions of a file are locked within your application.
- Avoid holding locks across long operations or method boundaries.
- Use try-with-resources or finally blocks to guarantee lock release.

## Related Errors

- [ClosedChannelException](../closedchannelexception) — lock on a closed channel.
- [AsynchronousCloseException](../asynchronouscloseexception) — channel closed during blocking lock.
- [NonWritableChannelException](../nonwritablechannelexception) — lock requires write access.
