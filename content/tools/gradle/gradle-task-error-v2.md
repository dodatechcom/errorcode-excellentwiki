---
title: "Gradle Task Execution Failed for Task"
description: "Gradle task execution fails with 'Execution failed for task' error during build."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gradle", "task", "execution", "runtime", "build"]
weight: 5
---

# Gradle Task Execution Failed for Task

This error occurs when a specific Gradle task fails during its execution phase. Gradle reports `Execution failed for task ':taskName'` and the build stops. The task was configured correctly but failed when it ran.

## Common Causes

- Compilation errors in Java, Kotlin, or Groovy source files
- Test failures with strict test configurations
- Missing files or directories expected by the task
- Code quality checks (linting, formatting) detecting violations
- Resource processing failures

## How to Fix

### Identify the Failing Task

```bash
./gradlew build --stacktrace
```

### Run the Specific Task with Info

```bash
./gradlew :app:compileJava --info
```

### Skip the Failing Task Temporarily

```bash
./gradlew build -x test
./gradlew assemble -x lint
```

### Fix Compilation Errors

```bash
./gradlew compileJava 2>&1 | tail -20
```

### Increase Memory for Heavy Tasks

```properties
# gradle.properties
org.gradle.jvmargs=-Xmx4g -XX:MaxMetaspaceSize=512m
```

### Fix Task Configuration

```groovy
tasks.named('compileJava') {
    options.encoding = 'UTF-8'
    options.compilerArgs << '-Xlint:unchecked'
}
```

## Examples

```text
> Task :app:compileJava FAILED
/home/user/project/src/main/App.java:15: error: cannot find symbol
    String result = obejct.getName();
                         ^
FAILURE: Build failed with an exception.
* What went wrong:
  Execution failed for task ':app:compileJava'.
```

## Related Errors

- [Gradle Configuration Error]({{< relref "/tools/gradle/gradle-configuration-error" >}}) — build script evaluation failure
- [Gradle Build Failed]({{< relref "/tools/gradle/gradle-build-failed" >}}) — general build failure
- [Gradle Out of Memory]({{< relref "/tools/gradle/gradle-out-of-memory" >}}) — JVM heap space issues
