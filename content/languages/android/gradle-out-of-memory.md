---
title: "Gradle Out Of Memory Error"
description: "Solve Gradle out of memory error during Android project builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build fails with java.lang.OutOfMemoryError during Gradle execution

## Common Causes

- JVM heap size too small for large project
- Too many parallel Gradle daemon processes
- Memory leak in custom build script
- Insufficient system RAM for requested build tasks

## Fixes

- Increase JVM max heap in gradle.properties
- Reduce parallel worker count
- Enable Gradle build cache
- Use --no-daemon for CI builds

## Code Example

```kotlin
# gradle.properties
org.gradle.jvmargs=-Xmx4096m -XX:MaxMetaspaceSize=512m
org.gradle.parallel=true
org.gradle.caching=true
```

# Run with more memory
./gradlew assembleDebug --no-daemon -Dorg.gradle.jvmargs=-Xmx8g
