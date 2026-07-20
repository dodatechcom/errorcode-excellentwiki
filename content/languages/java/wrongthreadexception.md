---
title: "[Solution] Java WrongThreadException — Lock Ownership Violation Fix"
description: "Fix Java WrongThreadException by acquiring locks in the correct thread, using Thread.currentThread() checks, and ensuring proper lock ownership before calling synchronized methods."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 70
---

# WrongThreadException — Lock Ownership Violation Fix

A `WrongThreadException` is thrown when a thread attempts to call a method that requires lock ownership on a lock that it does not hold. This is common with `StampedLock`, `ReentrantLock`, and `Condition` APIs when the calling thread differs from the thread that acquired the lock.

## Description

`java.util.concurrent.locks.WrongThreadException` extends `IllegalMonitorStateException`. Common variants include:

- `java.util.concurrent.locks.WrongThreadException: Current thread is not owner`
- `java.util.concurrent.locks.WrongThreadException: attempt to unlock read lock, not locked by current thread`
- `java.util.concurrent.locks.WrongThreadException: Thread is not the owner of Condition`

This exception was introduced in Java 8 and is thrown by `StampedLock`, `ReentrantReadWriteLock`, and `Condition` when thread ownership is violated.

## Common Causes

```java
// Cause 1: StampedLock unlock from wrong thread
StampedLock lock = new StampedLock();
Thread t1 = new Thread(() -> {
    long stamp = lock.writeLock();
    // lock held by t1
});
Thread t2 = new Thread(() -> {
    lock.unlockWrite(stamp);  // WrongThreadException: t2 doesn't own the lock
});

// Cause 2: ReentrantLock unlock without holding it
ReentrantLock lock = new ReentrantLock();
Thread t2 = new Thread(() -> {
    lock.unlock();  // WrongThreadException: lock not acquired by t2
});

// Cause 3: Condition signal from wrong thread
ReentrantLock lock = new ReentrantLock();
Condition cond = lock.newCondition();
Thread t2 = new Thread(() -> {
    cond.signal();  // WrongThreadException: t2 doesn't hold the lock
});

// Cause 4: StampedLock optimistic read followed by write attempt
StampedLock lock = new StampedLock();
long stamp = lock.tryOptimisticRead();
// ... some work
// Attempting to upgrade optimistic read to write lock directly
lock.writeLock();  // This is fine, but if validation fails and you try to unlock, WrongThreadException

// Cause 5: Shared lock release from a thread that holds exclusive lock
StampedLock lock = new StampedLock();
long writeStamp = lock.writeLock();
// Wrong: trying to unlock a shared lock with a write stamp
lock.unlockRead(writeStamp);  // WrongThreadException
```

## Solutions

### Fix 1: Ensure lock ownership before unlocking

```java
ReentrantLock lock = new ReentrantLock();

public void safeUnlock() {
    if (lock.isHeldByCurrentThread()) {
        lock.unlock();
    } else {
        throw new IllegalStateException("Cannot unlock: current thread does not own the lock");
    }
}
```

### Fix 2: Use try-finally with the same thread acquiring and releasing

```java
StampedLock lock = new StampedLock();

public void readData() {
    long stamp = lock.tryOptimisticRead();
    // Read shared data
    if (!lock.validate(stamp)) {
        stamp = lock.readLock();  // Fallback to pessimistic read
        try {
            // Read shared data
        } finally {
            lock.unlockRead(stamp);
        }
    }
}
```

### Fix 3: Use Thread.currentThread() checks for lock ownership

```java
public class SharedResource {
    private final ReentrantLock lock = new ReentrantLock();
    private final Thread ownerThread = Thread.currentThread();

    public void releaseLock() {
        if (Thread.currentThread() != ownerThread) {
            throw new WrongThreadException("Only the owning thread can release this lock");
        }
        lock.unlock();
    }
}
```

### Fix 4: Use StampedLock with proper stamp handling

```java
StampedLock lock = new StampedLock();

public void transfer(Runnable task) {
    long stamp = lock.writeLock();
    try {
        task.run();
    } finally {
        lock.unlockWrite(stamp);  // Same stamp used for lock and unlock
    }
}
```

## Prevention Checklist

- Always use the same `stamp` value for both locking and unlocking operations
- Never pass lock stamps across threads
- Call `lock.isHeldByCurrentThread()` before `unlock()` when lock ownership is uncertain
- Use `try-finally` blocks to guarantee unlock on the same thread
- Avoid sharing `StampedLock` instances across threads for unlock operations

## Related Errors

- [IllegalMonitorStateException](/languages/java/illegalstateexception/) — Parent class of WrongThreadException
- [InterruptedException](/languages/java/interruptedioexception/) — Thread interrupted during lock wait
- [TimeoutException](/languages/java/timeoutexception/) — Lock acquisition timed out
