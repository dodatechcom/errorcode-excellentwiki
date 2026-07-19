---
title: "[Solution] Java ThreadDeath — calling Thread.stop() which throws ThreadDeath"
description: "Fix Java ThreadDeath when calling thread.stop() which throws threaddeath with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ThreadDeath — calling Thread.stop() which throws ThreadDeath

A `ThreadDeath` occurs when Thread worker = new Thread(() -> { while(running) { process(); } });
worker.start();
worker.stop();  // ThreadDeath — data corruption.

## Common Causes

```java
Thread worker = new Thread(() -> { while(running) { process(); } });
worker.start();
worker.stop();  // ThreadDeath — data corruption
```

## Solutions

```java
// Fix: cooperative cancellation
Thread worker = new Thread(() -> {
    while (!Thread.currentThread().isInterrupted() && running) { process(); }
});
worker.start();
worker.interrupt();

// Fix: volatile flag
private volatile boolean running = true;
public void stop() { running = false; }

// Fix: ExecutorService shutdown
ExecutorService pool = Executors.newFixedThreadPool(4);
pool.shutdown();
pool.awaitTermination(5, SECONDS);
if (!pool.isTerminated()) pool.shutdownNow();
```

## Prevention Checklist

- Never use Thread.stop() — deprecated since Java 1.2.
- Use Thread.interrupt() for cooperative cancellation.
- Use volatile flags for clean shutdown.
- Use ExecutorService lifecycle methods.

## Related Errors

IllegalStateException, InterruptedException
