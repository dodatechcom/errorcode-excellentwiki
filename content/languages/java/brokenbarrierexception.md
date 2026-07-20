---
title: "[Solution] Java BrokenBarrierException — CyclicBarrier Broken Fix"
description: "Fix Java BrokenBarrierException by handling barrier reset, implementing error recovery, checking barrier party count, and using await with timeout."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 76
---

# BrokenBarrierException — CyclicBarrier Broken Fix

A `BrokenBarrierException` is thrown when a thread calls `await()` on a `CyclicBarrier` that has been broken. A barrier breaks when one of the waiting threads is interrupted, times out, or the barrier action throws an exception.

## Description

`java.util.concurrent.BrokenBarrierException` extends `Exception`. Common variants include:

- `java.util.concurrent.BrokenBarrierException`
- `java.util.concurrent.BrokenBarrierException: null`

When any thread waiting on a `CyclicBarrier` encounters an error (interruption, timeout, or barrier action failure), the barrier is broken and all other waiting threads receive `BrokenBarrierException`.

## Common Causes

```java
// Cause 1: One thread timed out, breaking the barrier
CyclicBarrier barrier = new CyclicBarrier(3);
Thread t1 = new Thread(() -> {
    try { barrier.await(1, TimeUnit.SECONDS); } catch (Exception e) { }
});
Thread t2 = new Thread(() -> {
    try { Thread.sleep(500); barrier.await(1, TimeUnit.SECONDS); }
    catch (Exception e) { }
});
Thread t3 = new Thread(() -> {
    try { Thread.sleep(2000); barrier.await(1, TimeUnit.SECONDS); }
    catch (Exception e) { }  // t3 times out, barrier breaks
});
// t1 and t2 receive BrokenBarrierException

// Cause 2: Thread interrupted while waiting at barrier
Thread t1 = new Thread(() -> {
    try { barrier.await(); }
    catch (InterruptedException e) { Thread.currentThread().interrupt(); }
    catch (BrokenBarrierException e) { /* barrier broken */ }
});

// Cause 3: Barrier action throws an exception
CyclicBarrier barrier = new CyclicBarrier(2, () -> {
    throw new RuntimeException("Barrier action failed");  // breaks barrier
});
// All waiting threads get BrokenBarrierException

// Cause 4: Using a broken barrier after reset
barrier.reset();  // resets the barrier, but any thread still gets BrokenBarrierException
```

## Solutions

### Fix 1: Handle BrokenBarrierException with recovery logic

```java
CyclicBarrier barrier = new CyclicBarrier(3);

public void awaitSafely() {
    try {
        barrier.await();
    } catch (BrokenBarrierException e) {
        System.err.println("Barrier was broken, retrying...");
        barrier.reset();  // reset before retrying
        try {
            barrier.await();  // retry
        } catch (Exception retryEx) {
            throw new RuntimeException("Barrier recovery failed", retryEx);
        }
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
    }
}
```

### Fix 2: Use await() with timeout to detect stuck threads

```java
CyclicBarrier barrier = new CyclicBarrier(3);

public void awaitWithTimeout() {
    try {
        boolean passed = barrier.await(30, TimeUnit.SECONDS);
        if (!passed) {
            handleTimeout();
        }
    } catch (TimeoutException e) {
        handleTimeout();
    } catch (BrokenBarrierException e) {
        handleBrokenBarrier();
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
    }
}

private void handleTimeout() {
    System.err.println("Barrier wait timed out");
    barrier.reset();
}
```

### Fix 3: Check barrier state before waiting

```java
CyclicBarrier barrier = new CyclicBarrier(3);

public void safeAwait() {
    int parties = barrier.getParties();
    int waiting = barrier.getNumberWaiting();

    if (waiting >= parties - 1) {
        // We are the last party, expect barrier to complete
        barrier.await();
    } else {
        // Not enough parties, handle appropriately
        throw new IllegalStateException("Not enough parties at barrier");
    }
}
```

### Fix 4: Use barrier with proper error handling in barrier action

```java
CyclicBarrier barrier = new CyclicBarrier(3, () -> {
    try {
        // Barrier action: safe execution
        processAggregatedResults();
    } catch (Exception e) {
        System.err.println("Barrier action error: " + e.getMessage());
        // Don't throw — let barrier complete successfully
    }
});
```

## Prevention Checklist

- Always catch `BrokenBarrierException` when using `CyclicBarrier`
- Use `await()` with timeout to detect stuck participants
- Implement a safe barrier action that does not throw exceptions
- Call `reset()` to restore a broken barrier before retrying
- Consider using `Phaser` (Java 7+) as a more flexible alternative to `CyclicBarrier`

## Related Errors

- [TimeoutException](/languages/java/timeoutexception/) — await() timed out (causes BrokenBarrierException)
- [InterruptedException](/languages/java/interruptedioexception/) — Thread interrupted during await
- [CancellationException](/languages/java/cancellationexception/) — Related task cancellation
