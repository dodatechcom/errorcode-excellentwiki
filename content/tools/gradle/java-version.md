---
title: "[Solution] Gradle Invalid Java Version"
description: "Fix Gradle invalid Java version errors. Resolve JDK compatibility and toolchain configuration issues."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gradle", "java", "version", "jdk", "toolchain", "compatibility"]
weight: 5
---

# Gradle Invalid Java Version

Gradle requires a specific Java version to run and a compatible JDK for compilation. A version mismatch occurs when the running JDK does not meet the Gradle minimum requirement or the `sourceCompatibility`/`targetCompatibility` settings.

## Common Causes

- The JAVA_HOME points to an unsupported JDK version
- `sourceCompatibility` or `targetCompatibility` is set to an unsupported version
- The Java toolchain version is not installed
- Gradle version is too old for the JDK being used

## How to Fix

### Check Current Java Version

```bash
java -version
echo $JAVA_HOME
```

### Set Java Version in Build Script

```groovy
// build.gradle
java {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}
```

### Use Java Toolchain

```groovy
java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(17)
    }
}
```

### Configure JAVA_HOME for Gradle

```bash
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
./gradlew build
```

### Check Gradle-JDK Compatibility

```bash
# Gradle 8.x requires JDK 8+
# Gradle 7.x requires JDK 8+
# Check: https://docs.gradle.org/current/userguide/compatibility.html
```

## Examples

```bash
# JAVA_HOME points to JDK 6
./gradlew build
# FAILURE: Build failed with an exception.
# * What went wrong: Gradle 8.0 requires JDK 8+ to run.
# Fix: set JAVA_HOME to a JDK 8+ installation

# sourceCompatibility set to unsupported version
./gradlew compileJava
# ERROR: unsupported source version: 21
# Fix: update Gradle or lower sourceCompatibility
```

## Related Errors

- [Compatibility Error]({{< relref "/tools/gradle/compatibility-error" >}}) — Gradle version mismatch
- [Task Error]({{< relref "/tools/gradle/task-error" >}}) — task execution failure
