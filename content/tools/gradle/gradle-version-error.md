---
title: "Gradle Version Incompatibility Error"
description: "Gradle build fails due to version incompatibility between Gradle wrapper, plugins, or Java."
tools: ["gradle"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Gradle Version Incompatibility Error

This error occurs when the Gradle version is incompatible with the project's plugins, build scripts, or the installed Java version. Gradle has strict compatibility requirements.

## Common Causes

- Gradle wrapper version is too old or too new for the project
- Plugin requires a newer Gradle version than installed
- Java version does not match Gradle's compatibility requirements
- Kotlin DSL syntax incompatible with Gradle version

## How to Fix

### Check Current Gradle Version

```bash
./gradlew --version
```

### Update Gradle Wrapper

```bash
./gradlew wrapper --gradle-version 8.4
```

### Check Java Compatibility

| Gradle Version | Java Compatibility |
|---|---|
| 8.x | Java 8-21 |
| 7.x | Java 8-18 |
| 6.x | Java 8-16 |

### Fix Plugin Version

```groovy
// In build.gradle
plugins {
    id 'com.android.application' version '8.1.0' apply false  // check compatibility
}
```

### Use Compatibility Matrix

Check [Gradle Compatibility Matrix](https://docs.gradle.org/current/userguide/compatibility.html) for supported combinations.

### Force Java Version

```properties
# gradle.properties
org.gradle.java.home=/usr/lib/jvm/java-17
```

## Examples

```bash
./gradlew build
# FAILURE: Required minimum Gradle version is 8.0.
# Current version is 7.6.2

# Fix:
./gradlew wrapper --gradle-version 8.4
```

## Related Errors

- [Build Failed]({{< relref "/tools/gradle/build-failed" >}}) — general build failure
- [Plugin Error]({{< relref "/tools/gradle/plugin-error" >}}) — plugin application failure
