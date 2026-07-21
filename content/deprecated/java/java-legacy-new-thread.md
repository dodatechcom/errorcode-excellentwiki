---
title: "[Solution] Deprecated Function Migration: new Thread() to ExecutorService"
description: "Migrate from deprecated new Thread() to ExecutorService."
deprecated_function: "new Thread(runnable).start()"
replacement_function: "executor.execute(runnable)"
languages: ["java"]
deprecated_since: "Java 5+"
---

# [Solution] Deprecated Function Migration: new Thread() to ExecutorService

The `new Thread(runnable).start()` has been deprecated in favor of `executor.execute(runnable)`.

## Migration Guide

ExecutorService manages thread pool.

## Before (Deprecated)

```java
new Thread(() -> {
    doWork();
}).start();
```

## After (Modern)

```java
ExecutorService executor = Executors.newFixedThreadPool(10);
executor.execute(() -> {
    doWork();
});
```

## Key Differences

- ExecutorService manages thread pool
