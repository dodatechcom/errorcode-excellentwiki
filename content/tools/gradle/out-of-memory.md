---
title: "Out of Memory: Java Heap Space"
description: "Gradle daemon or build process ran out of memory, causing the build to fail with a Java heap space error."
tools: ["gradle"]
error-types: ["build-error"]
severities: ["error"]
tags: ["gradle", "out-of-memory", "heap-space", "daemon"]
weight: 5
---

This error means the Gradle daemon process exceeded its allocated Java heap memory. It typically happens on large projects with many modules or heavy compilation tasks.

## Common Causes

- Default JVM heap size is too small for the project size
- Memory leak in a custom Gradle plugin or build script
- Too many concurrent Gradle daemon processes consuming system memory
- Large generated sources or annotation processing consuming excessive memory

## How to Fix

Increase the Gradle daemon JVM memory in `gradle.properties`:

```properties
org.gradle.jvmargs=-Xmx4g -XX:MaxMetaspaceSize=512m
```

Stop existing daemons and rebuild:

```bash
./gradlew --stop
./gradlew build
```

Limit parallel workers to reduce memory pressure:

```properties
org.gradle.parallel=true
org.gradle.workers.max=4
```

## Examples

```
> Task :compileJava
FAILURE: Build failed with an exception.

* What went wrong:
Java heap space

* Try:
Run with --stacktrace to get the full stack trace.
```

## Related Errors

- [Build Failed]({{< relref "/tools/gradle/build-failed" >}})
