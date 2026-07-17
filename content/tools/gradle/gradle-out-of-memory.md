---
title: "Gradle Java Heap Space Out of Memory"
description: "Gradle fails with OutOfMemoryError: Java heap space during build execution."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Gradle Java Heap Space Out of Memory

This error means Gradle's JVM ran out of heap memory during build execution. The build process tried to allocate more memory than the JVM was configured to allow.

## Common Causes

- Large projects with many dependencies exceed default heap limits
- Memory leaks in custom Gradle plugins or build scripts
- Too many parallel tasks running simultaneously
- Insufficient `org.gradle.jvmargs` configuration

## How to Fix

### Increase JVM Memory

```properties
# gradle.properties
org.gradle.jvmargs=-Xmx4g -XX:MaxMetaspaceSize=512m
```

### Reduce Parallel Workers

```properties
# gradle.properties
org.gradle.parallel=false
org.gradle.workers.max=2
```

### Enable Gradle Build Cache

```properties
# gradle.properties
org.gradle.caching=true
```

### Analyze Memory Usage

```bash
./gradlew build --profile
# Open the generated HTML report in build/reports/profile/
```

### Fix Memory Leaks in Build Scripts

```groovy
// Avoid accumulating collections in buildSrc
// Don't create objects inside task actions that persist
```

### Use Daemon with Proper Memory Settings

```bash
./gradlew --stop
./gradlew build -Dorg.gradle.jvmargs=-Xmx6g
```

## Examples

```bash
./gradlew build
# FAILURE: Build failed with an exception.
# * What went wrong: Java heap space
# > GC overhead limit exceeded

# After increasing memory:
# gradle.properties: org.gradle.jvmargs=-Xmx4g
# Build succeeds
```

## Related Errors

- [Build Failed]({{< relref "/tools/gradle/build-failed" >}}) — general build failure
- [Task Error]({{< relref "/tools/gradle/task-error" >}}) — task execution failure
