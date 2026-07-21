---
title: "[Solution] Deprecated Function Migration: e.printStackTrace() to logging"
description: "Migrate from deprecated e.printStackTrace() to proper logging frameworks in Java."
deprecated_function: "e.printStackTrace()"
replacement_function: "Logger.log()"
languages: ["java"]
deprecated_since: "Java best practice"
---

# [Solution] Deprecated Function Migration: e.printStackTrace() to logging

The `e.printStackTrace()` has been deprecated in favor of `Logger.log()`.

## Migration Guide

printStackTrace() writes to stderr without context. Use a logging framework for structured error logging.

## Before (Deprecated)

```java
try {
    processData();
} catch (Exception e) {
    e.printStackTrace();
}
```

## After (Modern)

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

private static final Logger logger = LoggerFactory.getLogger(MyClass.class);

try {
    processData();
} catch (Exception e) {
    logger.error("Failed to process data", e);
}
```

## Key Differences

- printStackTrace goes to stderr without context
- Logger provides timestamps, levels, and destinations
- Log files for production monitoring
- Configurable output format
