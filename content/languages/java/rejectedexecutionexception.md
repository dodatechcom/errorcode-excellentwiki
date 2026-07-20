---
title: "[Solution] Java RejectedExecutionException — Thread Pool Full Fix"
description: "Fix Java RejectedExecutionException by increasing pool size, using CallerRunsPolicy, checking executor shutdown, and using bounded queues."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# RejectedExecutionException — Thread Pool Full Fix

A `RejectedExecutionException` is thrown when a task cannot be submitted for execution to a thread pool. This occurs when the pool is shut down, the maximum pool size and work queue are full, or the `RejectedExecutionHandler` rejects the task.

## Description

`java.util.concurrent.RejectedExecutionException` is an unchecked exception extending `java.lang.RuntimeException`. It is thrown by `ExecutorService.submit()` and `Executor.execute()` when the task cannot be accepted.

Common message variants:

- `java.util.concurrent.RejectedExecutionException: Task java.lang.Runnable rejected from java.util.concurrent.ThreadPoolExecutor`
- `Task rejected from ThreadPoolExecutor`
- `Executor is shut down`

This is commonly seen with:

- Fixed thread pools with bounded queues that are at capacity
- Executors that have been `shutdown()` or `shutdownNow()`'d
- Custom rejection policies that throw this exception

## Common Causes

```java
// Cause 1: Submitting to a shut-down executor
ExecutorService executor = Executors.newFixedThreadPool(2);
executor.shutdown();
executor.submit(() -> doWork());  // RejectedExecutionException

// Cause 2: Fixed pool with bounded queue is full
ExecutorService executor = new ThreadPoolExecutor(
    2, 2, 0L, TimeUnit.MILLISECONDS,
    new LinkedBlockingQueue<>(10)  // Queue capacity: 10
);
// Submit 12 tasks — queue full + max threads reached
for (int i = 0; i < 12; i++) {
    executor.submit(() -> doWork());  // Last task: RejectedExecutionException
}

// Cause 3: CallerRunsPolicy equivalent not configured
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    1, 1, 0L, TimeUnit.MILLISECONDS,
    new ArrayBlockingQueue<>(5)  // Bounded queue
);
// When full and max threads reached, default handler throws
for (int i = 0; i < 10; i++) {
    executor.submit(() -> doWork());
}

// Cause 4: ShutdownNow() in progress
executor.shutdownNow();
executor.submit(() -> doWork());  // RejectedExecutionException
```

## Solutions

### Fix 1: Increase pool size or use an unbounded queue

```java
// Option A: Larger pool
ExecutorService executor = new ThreadPoolExecutor(
    10, 20, 60L, TimeUnit.SECONDS,
    new LinkedBlockingQueue<>(100)
);

// Option B: Unbounded queue (no RejectedExecutionException, but may cause OOM)
ExecutorService executor = new ThreadPoolExecutor(
    5, 5, 0L, TimeUnit.MILLISECONDS,
    new LinkedBlockingQueue<>()  // Unbounded
);
```

### Fix 2: Use CallerRunsPolicy to handle overflow gracefully

```java
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    4, 4, 0L, TimeUnit.MILLISECONDS,
    new LinkedBlockingQueue<>(10),
    new ThreadPoolExecutor.CallerRunsPolicy()  // Runs task in caller thread
);

// When full, the calling thread executes the task instead of rejecting
executor.submit(() -> doWork());
```

### Fix 3: Check if executor is shutdown before submitting

```java
public static void safeSubmit(ExecutorService executor, Runnable task) {
    if (executor.isShutdown()) {
        System.err.println("Executor is shut down — task rejected");
        return;
    }
    try {
        executor.submit(task);
    } catch (RejectedExecutionException e) {
        System.err.println("Task rejected: " + e.getMessage());
    }
}
```

### Fix 4: Implement custom rejection handler with retry

```java
public class RetryRejectionHandler implements RejectedExecutionHandler {
    private final int maxRetries;

    public RetryRejectionHandler(int maxRetries) {
        this.maxRetries = maxRetries;
    }

    @Override
    public void rejectedExecution(Runnable r, ThreadPoolExecutor executor) {
        for (int i = 0; i < maxRetries; i++) {
            try {
                Thread.sleep(100 * (i + 1));
                executor.getQueue().put(r);  // Blocking put
                return;
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            } catch (RejectedExecutionException e) {
                // Retry
            }
        }
        throw new RejectedExecutionException("Task rejected after " + maxRetries + " retries");
    }
}

ThreadPoolExecutor executor = new ThreadPoolExecutor(
    4, 8, 60L, TimeUnit.SECONDS,
    new LinkedBlockingQueue<>(50),
    new RetryRejectionHandler(3)
);
```

## Prevention Checklist

- Always check `executor.isShutdown()` before submitting tasks.
- Use `CallerRunsPolicy` for graceful degradation when the pool is full.
- Configure appropriate pool sizes and queue capacities for expected workloads.
- Wrap `submit()` calls in try-catch to handle `RejectedExecutionException`.
- Use `awaitTermination()` after `shutdown()` to wait for in-flight tasks.

## Related Errors

- [CompletionException](../completionexception) — exception during CompletableFuture execution.
- [CancellationException](../cancellationexception) — task was cancelled.
- [RejectedExecutionException](../rejectedexecutionexception) — task submission rejected.
