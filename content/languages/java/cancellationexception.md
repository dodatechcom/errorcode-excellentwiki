---
title: "[Solution] Java CancellationException — Concurrent Task Cancel Fix"
description: "Fix Java CancellationException by checking isCancelled() before calling get(), handling it in catch blocks, and using proper cancellation patterns."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# CancellationException — Concurrent Task Cancel Fix

A `CancellationException` is thrown when attempting to retrieve the result of a `Future` that has been cancelled. Calling `Future.get()` on a cancelled task always throws this exception, regardless of whether the task completed before cancellation.

## Description

`java.util.concurrent.CancellationException` is an unchecked exception extending `java.lang.IllegalStateException`. It is thrown by:

- `Future.get()` when the task was cancelled via `Future.cancel()`
- `Future.get(timeout, unit)` when the task was cancelled
- `CompletableFuture.get()` on a cancelled future

Common message variants:

- `java.util.concurrent.CancellationException`
- `Task was cancelled`

Note: A cancelled task's `get()` method throws `CancellationException`, not `ExecutionException`. The task may have been cancelled before, during, or after execution.

## Common Causes

```java
// Cause 1: Getting result of a cancelled Future
ExecutorService executor = Executors.newSingleThreadExecutor();
Future<String> future = executor.submit(() -> {
    Thread.sleep(5000);
    return "result";
});
future.cancel(true);  // Cancel the task
future.get();          // CancellationException

// Cause 2: CompletableFuture cancelled
CompletableFuture<String> cf = CompletableFuture.supplyAsync(() -> {
    Thread.sleep(5000);
    return "result";
});
cf.cancel(true);
cf.get();  // CancellationException

// Cause 3: Task cancelled before it starts
ExecutorService executor = Executors.newFixedThreadPool(1);
executor.shutdown();  // No new tasks accepted
Future<String> future = executor.submit(() -> "result");
// If executor rejects: task never runs, may be effectively cancelled

// Cause 4: get() called after cancel() in multiple places
Future<Integer> future = executor.submit(() -> computeValue());
future.cancel(false);
// Later in another method...
Integer value = future.get();  // CancellationException
```

## Solutions

### Fix 1: Check isCancelled() before calling get()

```java
Future<String> future = executor.submit(() -> computeResult());

if (future.isCancelled()) {
    System.out.println("Task was cancelled");
    return;
}

try {
    String result = future.get();
} catch (CancellationException e) {
    System.out.println("Task was cancelled between check and get");
}
```

### Fix 2: Handle CancellationException in catch blocks

```java
Future<String> future = executor.submit(() -> computeResult());

try {
    String result = future.get(5, TimeUnit.SECONDS);
    processResult(result);
} catch (CancellationException e) {
    // Task was cancelled — handle gracefully
    System.err.println("Task cancelled: " + e.getMessage());
} catch (ExecutionException e) {
    // Task threw an exception
    System.err.println("Task failed: " + e.getCause());
} catch (TimeoutException e) {
    // Task timed out
    future.cancel(true);
}
```

### Fix 3: Use CompletableFuture with exception handling

```java
CompletableFuture<String> cf = CompletableFuture
    .supplyAsync(() -> computeResult())
    .exceptionally(ex -> {
        if (ex instanceof CancellationException) {
            return "default value for cancellation";
        }
        throw new CompletionException(ex);
    });

// Cancel safely
cf.cancel(true);

// get() returns default for cancellation, throws for other errors
String result = cf.join();
```

### Fix 4: Implement proper cancellation pattern with cleanup

```java
public class CancellableTask implements Callable<String> {
    private volatile boolean cancelled = false;

    @Override
    public String call() throws Exception {
        try {
            for (int i = 0; i < 100; i++) {
                if (cancelled || Thread.currentThread().isInterrupted()) {
                    throw new InterruptedException("Task cancelled");
                }
                // Do work
                Thread.sleep(100);
            }
            return "completed";
        } finally {
            cleanup();
        }
    }

    public void cancel() {
        cancelled = true;
    }

    private void cleanup() {
        // Release resources
    }
}

// Usage
CancellableTask task = new CancellableTask();
Future<String> future = executor.submit(task);
task.cancel();  // Signal cancellation
future.cancel(true);  // Interrupt if running

try {
    String result = future.get();
} catch (CancellationException e) {
    // Expected — task was cancelled
}
```

## Prevention Checklist

- Always handle `CancellationException` when calling `Future.get()` on potentially cancelled tasks.
- Check `isCancelled()` before `get()` for early detection.
- Implement proper cancellation checks within the task body.
- Use `try-finally` for cleanup in cancellable tasks.
- Prefer `CompletableFuture` with `exceptionally()` for cleaner cancellation handling.

## Related Errors

- [CompletionException](../completionexception) — exception thrown during task execution.
- [ExecutionException](../interruptedexception) — wraps exceptions thrown by a task.
- [InterruptedException](../interruptedexception) — thread interrupt during blocking.
