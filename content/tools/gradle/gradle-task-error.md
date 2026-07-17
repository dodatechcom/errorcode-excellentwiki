---
title: "Gradle Task Execution Error"
description: "Gradle task fails during execution, returning a non-zero exit code or throwing an exception."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gradle", "task", "execution", "runtime", "build"]
weight: 5
---

# Gradle Task Execution Error

A Gradle task execution error means the build started a task but the task failed during its execution phase. This is different from configuration errors — the build script evaluated correctly but a specific task returned a failure status.

## Common Causes

- Compilation errors in source code
- Test failures with strict test configurations
- Missing files or directories expected by the task
- Insufficient memory or system resources for the task

## How to Fix

### Run with Stack Trace

```bash
./gradlew <task-name> --stacktrace
```

### Run with Info Logging

```bash
./gradlew <task-name> --info
```

### Skip Failing Tests Temporarily

```bash
./gradlew build -x test
```

### Increase JVM Memory

```properties
# gradle.properties
org.gradle.jvmargs=-Xmx4g -XX:MaxMetaspaceSize=512m
```

### Fix the Specific Task

```groovy
tasks.register('myTask') {
    doLast {
        file('build/output').mkdirs()
    }
}
```

## Examples

```bash
# Compilation failure
./gradlew compileJava
# FAILURE: Build failed with an exception.
# * What went wrong: Execution failed for task ':compileJava'.
# Fix: correct the source code errors

# Test failure
./gradlew test
# FAILURE: Build failed with an exception.
# * What went wrong: 3 tests failed.
# Fix: fix failing tests or use ./gradlew build -x test
```

## Related Errors

- [Configuration Error]({{< relref "/tools/gradle/config-error4" >}}) — build script evaluation failure
- [Cache Error]({{< relref "/tools/gradle/cache-error3" >}}) — corrupted build cache
