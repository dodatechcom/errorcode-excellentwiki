---
title: "Gradle Java Heap Space Out of Memory"
description: "Gradle build fails with Java heap space or out of memory error."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Gradle Java Heap Space — Out of Memory

This error occurs when Gradle runs out of JVM heap memory during a build. Large projects with many dependencies or heavy annotation processing can exhaust the default memory allocation.

## Common Causes

- Default heap size too small for project size
- Large number of dependencies being resolved
- Memory leaks in custom Gradle plugins
- Annotation processors consuming excessive memory
- Multiple daemons running simultaneously

## How to Fix

### Increase JVM Heap Size

```properties
# gradle.properties
org.gradle.jvmargs=-Xmx4g -XX:MaxMetaspaceSize=512m
```

### Increase for Specific Builds

```bash
./gradlew build -Dorg.gradle.jvmargs="-Xmx8g"
```

### Limit Daemon Memory

```properties
# gradle.properties
org.gradle.daemon=true
org.gradle.jvmargs=-Xmx2g
```

### Stop All Running Daemons

```bash
./gradlew --stop
```

### Configure Memory in init Script

```groovy
// ~/.gradle/init.d/memory.gradle
gradle.settingsEvaluated {
    jvmArgs '-Xmx4g', '-XX:MaxMetaspaceSize=512m'
}
```

### Reduce Memory Pressure from Plugins

```groovy
// Disable parallel execution if causing memory issues
// org.gradle.parallel=false in gradle.properties
```

## Examples

```text
java.lang.OutOfMemoryError: Java heap space

Gradle could not start your process.
  > JVM heap space exhausted

java.lang.OutOfMemoryError: Metaspace
```

## Related Errors

- [Gradle Task Error]({{< relref "/tools/gradle/gradle-task-error" >}}) — task execution failure
- [Gradle Daemon Error]({{< relref "/tools/gradle/gradle-daemon-error" >}}) — daemon connection issues
- [Gradle Build Failed]({{< relref "/tools/gradle/gradle-build-failed" >}}) — general build failure
