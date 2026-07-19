---
title: "[Solution] Java ThreadDeath — attempting to restart completed thread or calling methods on wrong state"
description: "Fix Java ThreadDeath when attempting to restart completed thread or calling methods on wrong state with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ThreadDeath — attempting to restart completed thread or calling methods on wrong state

A `ThreadDeath` occurs when Thread t = new Thread(() -> System.out.println("hi"));
t.start();
t.join();
t.start();  // IllegalThreadStateException.

## Common Causes

```java
Thread t = new Thread(() -> System.out.println("hi"));
t.start();
t.join();
t.start();  // IllegalThreadStateException
```

## Solutions

```java
// Fix: create new thread
Thread t1 = new Thread(() -> System.out.println("hi"));
t1.start();
t1.join();
Thread t2 = new Thread(() -> System.out.println("world"));
t2.start();

// Fix: ExecutorService
ExecutorService pool = Executors.newFixedThreadPool(4);
pool.submit(() -> System.out.println("hi"));
pool.submit(() -> System.out.println("world"));
pool.shutdown();

// Fix: check state
if (t.getState() == Thread.State.RUNNABLE) { /* interact */ }
```

## Prevention Checklist

- Never restart a thread after completion.
- Use ExecutorService for thread reuse.
- Check Thread.getState() before interacting.
- Use Thread.isAlive() to check status.

## Related Errors

IllegalThreadStateException, IllegalStateException
