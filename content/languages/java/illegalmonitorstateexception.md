---
title: "[Solution] Java IllegalMonitorStateException — Synchronization Fix"
description: "Fix Java IllegalMonitorStateException by properly synchronizing before calling wait(), notify(), or notifyAll() on monitored objects."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# IllegalMonitorStateException — Synchronization Fix

An `IllegalMonitorStateException` is thrown when a thread attempts to call `wait()`, `notify()`, or `notifyAll()` on an object without holding the object's monitor (i.e., without being inside a `synchronized` block on that object).

## Description

The Java monitor mechanism requires that a thread must own the monitor (via `synchronized`) before calling wait/notify methods. This exception indicates a synchronization bug where the thread calling these methods does not hold the lock.

## Common Causes

```java
// Cause 1: Calling wait() without synchronized block
Object lock = new Object();
lock.wait();  // IllegalMonitorStateException — not synchronized

// Cause 2: Calling notify() on wrong object
synchronized (lockA) {
    lockB.notify();  // Wrong — must notify on the same object you synchronized on
}

// Cause 3: Calling wait() on this without synchronization
public class Producer {
    public void waitForData() throws InterruptedException {
        wait();  // IllegalMonitorStateException — need synchronized(this)
    }
}

// Cause 4: Incorrect synchronized block scope
synchronized (lock) {
    // synchronized block ends here
}
lock.wait();  // After synchronized block — exception
```

## Solutions

```java
// Fix 1: Always synchronize before calling wait()
Object lock = new Object();
synchronized (lock) {
    lock.wait();  // correct — holding the monitor
}

// Fix 2: Use synchronized method
public class SharedResource {
    private boolean dataReady = false;

    public synchronized void waitForData() throws InterruptedException {
        while (!dataReady) {
            wait();  // correct — method is synchronized
        }
    }

    public synchronized void setDataReady() {
        dataReady = true;
        notify();  // correct — same monitor
    }
}

// Fix 3: Use CountDownLatch as modern alternative
CountDownLatch latch = new CountDownLatch(1);

// Wait thread
latch.await();

// Signal thread
latch.countDown();

// Fix 4: Use BlockingQueue for producer-consumer
BlockingQueue<String> queue = new LinkedBlockingQueue<>();

// Producer
queue.put("data");

// Consumer
String data = queue.take();
```

## Examples

```java
// This triggers IllegalMonitorStateException
public class Broken {
    private Object lock = new Object();

    public void waitForSignal() throws InterruptedException {
        lock.wait();  // NOT synchronized — throws exception
    }

    public void sendSignal() {
        lock.notify();
    }
}
```

## Related Exceptions

- [InterruptedException]({{< relref "/languages/java/interruptedexception" >}}) — thread interrupted while waiting
- [IllegalStateException]({{< relref "/languages/java/illegalstateexception" >}}) — object in wrong state
- [NullPointerException](../nullpointerexception) — calling wait/notify on null
