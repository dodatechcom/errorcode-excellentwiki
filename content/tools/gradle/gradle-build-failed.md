---
title: "Build Failed with Exception — Gradle"
description: "Gradle build fails with a build exception indicating configuration or execution problems."
tools: ["gradle"]
error-types: ["build-error"]
severities: ["error"]
tags: ["gradle", "build", "exception", "failure", "error"]
weight: 5
---

# Build Failed with Exception — Gradle

A Gradle build failure with an exception indicates the build process encountered a fatal error. The exception message identifies whether the failure occurred during configuration, task execution, or dependency resolution.

## Common Causes

- Build script syntax errors in `build.gradle`
- Incompatible plugin versions
- Missing required build configuration
- Environment-specific issues (wrong Java version, missing SDK)

## How to Fix

### Read the Full Error Message

```bash
./gradlew build --stacktrace
```

### Check Java Version

```bash
java -version
./gradlew --version
```

Ensure the Java version matches what Gradle requires.

### Fix Build Script Errors

```groovy
// Check for syntax errors, missing semicolons, wrong imports
plugins {
    id 'com.android.application' version '8.1.0' apply false
}
```

### Use Build Scan for Detailed Report

```bash
./gradlew build --scan
```

### Clean and Rebuild

```bash
./gradlew clean build
```

### Update Gradle Wrapper

```bash
./gradlew wrapper --gradle-version 8.4
```

## Examples

```bash
./gradlew build
# FAILURE: Build failed with an exception.
# * What went wrong:
# Execution failed for task ':compileJava'.
# > error: cannot find symbol

./gradlew build
# FAILURE: Build failed with an exception.
# * What went wrong:
# A problem occurred configuring project ':app'.
# > Failed to apply plugin 'com.android.application'.
```

## Related Errors

- [Task Error]({{< relref "/tools/gradle/task-error" >}}) — specific task failure
- [Configuration Error]({{< relref "/tools/gradle/config-error4" >}}) — configuration phase failure
- [Out of Memory]({{< relref "/tools/gradle/out-of-memory" >}}) — heap space exhausted
