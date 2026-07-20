---
title: "[Solution] Java IllegalStateException — Concurrent Context Fix"
description: "Fix Java IllegalStateException in concurrent context like CompletableFuture and Flow by checking state before operations, using proper synchronization, and handling concurrent access."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# IllegalStateException — Concurrent Context Fix

An `IllegalStateException` in a concurrent context is thrown when an operation is attempted on an object whose state does not allow it — typically because another thread has already completed, cancelled, or modified the object. This is common with `CompletableFuture`, `SubmissionPublisher` (Flow API), and concurrent data structures.

## Description

Concurrent objects like `CompletableFuture`, `CountDownLatch`, and `Flow.Subscriber` have strict state machines. Attempting to complete an already-completed future, subscribe after flow termination, or operate on a closed resource triggers `IllegalStateException`.

Message variants:

- `java.lang.IllegalStateException: Complete already completed`
- `java.lang.IllegalStateException: Already subscribed`
- `java.lang.IllegalStateException: Timeout expired`
- `java.lang.IllegalStateException: Thread.currentThread() != owner`

## Common Causes

```java
// Cause 1: Completing an already-completed CompletableFuture
CompletableFuture<String> future = new CompletableFuture<>();
future.complete("first");
future.complete("second");  // IllegalStateException — already completed

// Cause 2: Completing a future that already has an exception
CompletableFuture<String> future = new CompletableFuture<>();
future.completeExceptionally(new RuntimeException("fail"));
future.complete("value");  // IllegalStateException

// Cause 3: Subscribing to a terminated Flow.Publisher
SubmissionPublisher<String> publisher = new SubmissionPublisher<>();
publisher.close();  // terminates the publisher
publisher.subscribe(mySubscriber);  // IllegalStateException

// Cause 4: Operating on a closed CountDownLatch or Barrier
CountDownLatch latch = new CountDownLatch(1);
latch.countDown();
latch.countDown();  // IllegalStateException — count is already 0

// Cause 5: Joining a future from the completing thread
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
    return "done";
});
future.join();  // may cause issues if called from the same thread
```

## Solutions

### Fix 1: Check state before completing a CompletableFuture

```java
CompletableFuture<String> future = new CompletableFuture<>();

// Wrong — assumes future is not yet complete
future.complete("value");

// Right — use complete() which returns false if already complete
boolean wasSet = future.complete("value");
if (!wasSet) {
    System.out.println("Future was already completed — skipping");
}

// Right — use completeExceptionally safely
boolean wasSet = future.completeExceptionally(new RuntimeException("error"));
```

### Fix 2: Use atomic state transitions with compareAndSet

```java
import java.util.concurrent.atomic.AtomicReference;

public class SafeCompletableFuture<T> {
    private final CompletableFuture<T> delegate = new CompletableFuture<>();
    private final AtomicReference<State> state = new AtomicReference<>(State.PENDING);

    enum State { PENDING, COMPLETED, FAILED }

    public boolean complete(T value) {
        if (state.compareAndSet(State.PENDING, State.COMPLETED)) {
            return delegate.complete(value);
        }
        return false;  // already transitioned
    }

    public boolean completeExceptionally(Throwable ex) {
        if (state.compareAndSet(State.PENDING, State.FAILED)) {
            return delegate.completeExceptionally(ex);
        }
        return false;
    }
}
```

### Fix 3: Handle Flow.Publisher lifecycle properly

```java
import java.util.concurrent.Flow;
import java.util.concurrent.SubmissionPublisher;

public class SafePublisher<T> {
    private final SubmissionPublisher<T> publisher = new SubmissionPublisher<>();
    private volatile boolean closed = false;

    public void subscribe(Flow.Subscriber<? super T> subscriber) {
        if (closed) {
            subscriber.onError(new IllegalStateException("Publisher is closed"));
            return;
        }
        publisher.subscribe(subscriber);
    }

    public void submit(T item) {
        if (!closed) {
            publisher.submit(item);
        }
    }

    public void close() {
        closed = true;
        publisher.close();
    }
}
```

### Fix 4: Use handle() to avoid state-check races

```java
CompletableFuture<String> future = new CompletableFuture<>();

// Instead of checking isDone() then complete() (race condition):
// Wrong
if (!future.isDone()) {
    future.complete("value");  // another thread may complete between check and act
}

// Right — use handle() or complete() directly
future.complete("value");  // atomic — returns false if already done

// Or use handle for combined completion logic
future.handle((value, ex) -> {
    if (ex != null) {
        return "fallback";
    }
    return value;
});
```

### Fix 5: Properly synchronize concurrent state machines

```java
public class StateMachine {
    private enum State { IDLE, RUNNING, COMPLETED, FAILED }
    private State state = State.IDLE;

    public synchronized void start() {
        if (state != State.IDLE) {
            throw new IllegalStateException("Cannot start from state: " + state);
        }
        state = State.RUNNING;
    }

    public synchronized void complete() {
        if (state != State.RUNNING) {
            throw new IllegalStateException("Cannot complete from state: " + state);
        }
        state = State.COMPLETED;
    }

    public synchronized boolean tryComplete() {
        if (state == State.RUNNING) {
            state = State.COMPLETED;
            return true;
        }
        return false;
    }
}
```

## Prevention Checklist

- Always check `isDone()` or handle return values from `complete()` / `completeExceptionally()`.
- Use `AtomicReference` with `compareAndSet` for thread-safe state transitions.
- Avoid `isDone()` then `complete()` patterns — they are racy.
- Validate publisher/subscriber lifecycle before calling `subscribe()`.
- Document thread-safety contracts for concurrent objects.
- Prefer `handle()`, `whenComplete()`, and `thenCombine()` over manual state checks.

## Related Errors

- [IllegalStateException](../illegalstateexception) — general state check failure
- [CompletionException](../completionexception) — exception wrapped in CompletableFuture
- [CancellationException](../cancellationexception) — future was cancelled
- [RejectedExecutionException](../rejectedexecutionexception) — task rejected by executor
