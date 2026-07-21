---
title: "[Solution] Deprecated Function Migration: Runtime.exec() to ProcessBuilder"
description: "Migrate from deprecated Runtime.exec() to ProcessBuilder for system process execution."
deprecated_function: "Runtime.getRuntime().exec()"
replacement_function: "ProcessBuilder"
languages: ["java"]
deprecated_since: "Java 5+"
---

# [Solution] Deprecated Function Migration: Runtime.exec() to ProcessBuilder

The `Runtime.getRuntime().exec()` has been deprecated in favor of `ProcessBuilder`.

## Migration Guide

ProcessBuilder provides full control over working directory, environment variables, and I/O streams.

## Before (Deprecated)

```java
Runtime runtime = Runtime.getRuntime();
Process process = runtime.exec("ls -la");
BufferedReader reader = new BufferedReader(
    new InputStreamReader(process.getInputStream()));
```

## After (Modern)

```java
ProcessBuilder pb = new ProcessBuilder("ls", "-la");
pb.directory(new File("/home"));
pb.environment().put("MY_VAR", "value");
pb.redirectErrorStream(true);

Process process = pb.start();
BufferedReader reader = new BufferedReader(
    new InputStreamReader(process.getInputStream()));
```

## Key Differences

- ProcessBuilder allows setting working directory
- Environment variables can be configured
- Command passed as a list (safer)
