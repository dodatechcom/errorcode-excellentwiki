---
title: "[Solution] Java IllegalArgumentException — non-positive pool size or invalid capacity for executors"
description: "Fix Java IllegalArgumentException when non-positive pool size or invalid capacity for executors with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# IllegalArgumentException — non-positive pool size or invalid capacity for executors

A `IllegalArgumentException` occurs when Executors.newFixedThreadPool(0);  // IAE
new ThreadPoolExecutor(5, 2, 60, SECONDS, q);  // IAE.

## Common Causes

```java
Executors.newFixedThreadPool(0);  // IAE
new ThreadPoolExecutor(5, 2, 60, SECONDS, q);  // IAE
```

## Solutions

```java
// Fix: validate parameters
public static ExecutorService createPool(int core, int max) {
    if (core <= 0) throw new IAE("coreSize must be > 0");
    if (max < core) throw new IAE("maxSize must be >= coreSize");
    return new ThreadPoolExecutor(core, max, 60L, SECONDS, new LinkedBlockingQueue<>());
}

// Fix: clamp to valid range
int poolSize = Math.max(1, calculatePoolSize());
ExecutorService pool = Executors.newFixedThreadPool(poolSize);
```

## Prevention Checklist

- Validate all concurrency parameters.
- Use Math.max(1, value) for positive sizes.
- Test edge cases (0, negative, MAX_VALUE).

## Related Errors

RejectedExecutionException, IllegalStateException
