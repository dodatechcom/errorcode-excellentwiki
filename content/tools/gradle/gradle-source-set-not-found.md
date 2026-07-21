---
title: "[Solution] Gradle Source Set Not Found"
description: "Fix source set not found errors in Gradle."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Source Set Not Found

Fix source set not found errors in Gradle. This error occurs when Gradle encounters build, plugin, or dependency problems.

## Common Causes

- Incorrect build.gradle configuration
- Plugin compatibility issues
- Dependency resolution failures
- Gradle version incompatibility

## How to Fix

### Solution 1: Check Build Configuration

Review your `build.gradle` or `build.gradle.kts` for errors:

```groovy
plugins {
    id 'java'
}

repositories {
    mavenCentral()
}

dependencies {
    implementation 'com.google.guava:guava:31.1-jre'
}
```

### Solution 2: Clean and Rebuild

```bash
./gradlew clean build
```

### Solution 3: Debug Build

```bash
./gradlew build --stacktrace --info
```

The `--stacktrace` flag provides detailed error traces and `--info` gives verbose logging.

## Example

```kotlin
// build.gradle.kts example
plugins {
    java
}

repositories {
    mavenCentral()
}

dependencies {
    testImplementation("org.junit.jupiter:junit-jupiter:5.9.0")
}

tasks.test {
    useJUnitPlatform()
}
```

## Related Links

- [Gradle Documentation](https://docs.gradle.org/)
- [Gradle Troubleshooting](https://docs.gradle.org/current/userguide/troubleshooting.html)
