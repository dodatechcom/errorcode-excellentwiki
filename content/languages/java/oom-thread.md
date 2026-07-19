---
title: "[Solution] Java OutOfMemoryError — creating too many threads consuming stack memory"
description: "Fix Java OutOfMemoryError when creating too many threads consuming stack memory with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# OutOfMemoryError — creating too many threads consuming stack memory

A `OutOfMemoryError` occurs when while (hasWork()) { new Thread(() -> process()).start(); }.

## Common Causes

```java
while (hasWork()) { new Thread(() -> process()).start(); }
```

## Solutions

```java
// Fix: bounded pool
ExecutorService pool = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors()*2);

// Fix: reduce stack
// -Xss256k

// Fix: virtual threads (Java 21+)
try (var ex = Executors.newVirtualThreadPerTaskExecutor()) {
    for (int i=0; i<100000; i++) ex.submit(() -> process());
}

// Fix: monitor
System.out.println("Threads: "+ManagementFactory.getThreadMXBean().getThreadCount());
```

## Prevention Checklist

- Use bounded thread pools.
- Set -Xss for stack size.
- Monitor thread count.
- Consider virtual threads (Java 21+).

## Related Errors

OutOfMemoryError, StackOverflowError
