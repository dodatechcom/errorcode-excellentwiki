---
title: "[Solution] Java IllegalThreadStateException — Thread Lifecycle Fix"
description: "Fix Java IllegalThreadStateException by not restarting threads, using ExecutorService for task management, and following proper thread lifecycle."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["illegalthreadstateexception", "thread", "lifecycle", "concurrency"]
weight: 5
---

# IllegalThreadStateException — Thread Lifecycle Fix

An `IllegalThreadStateException` is thrown when a thread operation is attempted that is not valid for the thread's current state. The most common case is attempting to start a thread that has already been started and completed (or is still running).

## Description

A `Thread` can only be started once. Once a thread has completed execution (either by returning from `run()` or due to an exception), it cannot be restarted. Calling `start()` on a thread that is already alive (running, waiting, or terminated) throws this exception.

## Common Causes

```java
// Cause 1: Restarting a completed thread
Thread t = new Thread(() -> System.out.println("Running"));
t.start();
t.start();  // IllegalThreadStateException — already started

// Cause 2: Starting a thread that is already running
Thread t = new Thread(() -> {
    while (true) { /* long running task */ }
});
t.start();
Thread.sleep(100);
t.start();  // IllegalThreadStateException — still running

// Cause 3: Starting a daemon thread flag after start
Thread t = new Thread(() -> {});
t.start();
t.setDaemon(true);  // IllegalThreadStateException — thread already started

// Cause 4: Interrupting a thread in invalid state
Thread t = new Thread(() -> {});
t.interrupt();  // Can cause IllegalThreadStateException in some contexts
```

## Solutions

```java
// Fix 1: Create a new thread instance instead of restarting
Thread oldThread = new Thread(() -> System.out.println("Running"));
oldThread.start();
oldThread.join();

Thread newThread = new Thread(() -> System.out.println("Running again"));
newThread.start();  // correct — new thread instance

// Fix 2: Use ExecutorService for reusable thread pools
ExecutorService executor = Executors.newFixedThreadPool(4);
executor.submit(() -> System.out.println("Task 1"));
executor.submit(() -> System.out.println("Task 2"));
executor.shutdown();

// Fix 3: Set thread properties before starting
Thread t = new Thread(() -> System.out.println("Running"));
t.setDaemon(true);  // set before start
t.setPriority(Thread.MAX_PRIORITY);  // set before start
t.start();

// Fix 4: Use Runnable with ExecutorService instead of raw threads
ExecutorService executor = Executors.newSingleThreadExecutor();
Runnable task = () -> System.out.println("Executing task");
executor.submit(task);
executor.submit(task);  // can reuse — executor manages threads
```

## Examples

```java
// This triggers IllegalThreadStateException
public class Worker {
    private Thread workerThread;

    public void start() {
        workerThread = new Thread(this::doWork);
        workerThread.start();
    }

    public void restart() {
        workerThread.start();  // IllegalThreadStateException if already started
    }

    private void doWork() {
        System.out.println("Working...");
    }
}
```

## Related Exceptions

- [InterruptedException]({{< relref "/languages/java/interruptedexception" >}}) — thread interrupted while sleeping/waiting
- [IllegalStateException]({{< relref "/languages/java/illegalstateexception" >}}) — general invalid state
- [UnsupportedOperationException](../unsupportedoperationexception) — operation not supported
