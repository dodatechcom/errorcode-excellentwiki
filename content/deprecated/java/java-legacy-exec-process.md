---
title: "[Solution] Deprecated Function Migration: Runtime.exec to ProcessBuilder"
description: "Migrate from deprecated Runtime.exec to ProcessBuilder."
deprecated_function: "Runtime.getRuntime().exec(cmd)"
replacement_function: "ProcessBuilder(cmd).start()"
languages: ["java"]
deprecated_since: "Java 5+"
---

# [Solution] Deprecated Function Migration: Runtime.exec to ProcessBuilder

The `Runtime.getRuntime().exec(cmd)` has been deprecated in favor of `ProcessBuilder(cmd).start()`.

## Migration Guide

ProcessBuilder provides more control.

## Before (Deprecated)

```java
Process p = Runtime.getRuntime().exec("ls -la");
```

## After (Modern)

```java
ProcessBuilder pb = new ProcessBuilder("ls", "-la");
pb.directory(new File("/home"));
Process p = pb.start();
```

## Key Differences

- ProcessBuilder allows working directory
