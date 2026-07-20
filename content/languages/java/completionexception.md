---
title: "[Solution] Java CompletionException — CompletableFuture Error Fix"
description: "Fix Java CompletionException by handling the cause, using exceptionally() for recovery, and checking isCompletedExceptionally()."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# CompletionException — CompletableFuture Error Fix

A `CompletionException` is thrown when an exception occurs during the execution of a `CompletableFuture` stage. The original exception is wrapped as the cause. This is the standard way `CompletableFuture` propagates errors through the completion chain.

## Description

`java.util.concurrent.CompletionException` is an unchecked exception extending `java.lang.RuntimeException`. It wraps the actual exception that occurred during an asynchronous stage's execution.

Common message variants:

- `java.util.concurrent.CompletionException`
- `java.util.concurrent.CompletionException: <original exception message>`

Key behaviors:

- Thrown by `join()`, `get()`, `getNow()` when a stage completes exceptionally
- Wraps the original exception as `getCause()`
- A stage's exception propagates to dependent stages unless handled

## Common Causes

```java
// Cause 1: Exception in supplyAsync lambda
CompletableFuture<String> cf = CompletableFuture.supplyAsync(() -> {
    throw new RuntimeException("Something went wrong");
});
cf.join();  // CompletionException wrapping RuntimeException

// Cause 2: Exception in thenApply chain
CompletableFuture<Integer> cf = CompletableFuture
    .supplyAsync(() -> "hello")
    .thenApply(s -> {
        throw new IllegalArgumentException("Bad input");
    });
cf.join();  // CompletionException wrapping IllegalArgumentException

// Cause 3: Exception in thenCompose (flatmap)
CompletableFuture<String> cf = CompletableFuture
    .supplyAsync(() -> 42)
    .thenCompose(n -> {
        throw new IllegalStateException("Failed to compose");
    });
cf.join();  // CompletionException wrapping IllegalStateException

// Cause 4: Unhandled exception in thenAccept
CompletableFuture<Void> cf = CompletableFuture
    .supplyAsync(() -> "data")
    .thenAccept(data -> {
        if (data == null) throw new NullPointerException("Null data");
    });
cf.join();  // CompletionException wrapping NullPointerException
```

## Solutions

### Fix 1: Use exceptionally() to handle exceptions in the chain

```java
CompletableFuture<String> cf = CompletableFuture
    .supplyAsync(() -> fetchData())
    .exceptionally(ex -> {
        System.err.println("Failed: " + ex.getMessage());
        return "default value";  // Recovery value
    });

String result = cf.join();  // Returns "default value" on failure
```

### Fix 2: Handle cause in catch blocks when using join()

```java
CompletableFuture<String> cf = CompletableFuture.supplyAsync(() -> {
    throw new RuntimeException("Error");
});

try {
    String result = cf.join();
} catch (CompletionException e) {
    Throwable cause = e.getCause();
    if (cause instanceof RuntimeException) {
        System.err.println("Runtime error: " + cause.getMessage());
    } else {
        throw e;  // Re-throw if not handled
    }
}
```

### Fix 3: Check isCompletedExceptionally() before joining

```java
CompletableFuture<String> cf = CompletableFuture.supplyAsync(() -> {
    throw new RuntimeException("Error");
});

// Wait for completion (without blocking for long)
while (!cf.isDone()) {
    Thread.sleep(100);
}

if (cf.isCompletedExceptionally()) {
    System.err.println("Task failed exceptionally");
    cf.exceptionally(ex -> {
        System.err.println("Cause: " + ex.getCause().getMessage());
        return "fallback";
    });
}

String result = cf.join();
```

### Fix 4: Use handle() for dual success/failure processing

```java
CompletableFuture<String> cf = CompletableFuture
    .supplyAsync(() -> fetchData())
    .handle((result, ex) -> {
        if (ex != null) {
            System.err.println("Error: " + ex.getMessage());
            return "fallback value";
        }
        return result.toUpperCase();
    });

String result = cf.join();  // Always succeeds (either real or fallback)
```

## Prevention Checklist

- Always handle exceptions in `CompletableFuture` chains using `exceptionally()` or `handle()`.
- Prefer `handle()` over `exceptionally()` when you need to process both success and failure.
- Use `try-catch` around `join()` if exceptions might propagate from the chain.
- Wrap exceptions explicitly with `CompletionException` in custom `CompletableFuture` stages.
- Avoid calling `get()` with long timeouts — use `orTimeout()` or `completeOnTimeout()` instead.

## Related Errors

- [CancellationException](../cancellationexception) — task was cancelled.
- [ExecutionException](../interruptedexception) — wraps exceptions from `Future.get()`.
- [RejectedExecutionException](../rejectedexecutionexception) — task submission rejected by executor.
