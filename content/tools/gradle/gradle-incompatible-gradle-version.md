---
title: "Incompatible Gradle Version Error"
description: "Gradle build fails because the required Gradle version is not installed or the wrapper specifies an incompatible version."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Incompatible Gradle Version Error

Each Gradle build may require a specific Gradle version. This error occurs when the installed Gradle or the wrapper version is incompatible with the build script features.

## Common Causes

- The `gradle-wrapper.properties` specifies a version that is not installed
- The build script uses features from a newer Gradle version
- A plugin requires a minimum Gradle version that is not met
- The wrapper distribution URL is unreachable

## How to Fix

1. Check the required Gradle version in the wrapper:

```properties
# gradle/wrapper/gradle-wrapper.properties
distributionUrl=https\://services.gradle.org/distributions/gradle-8.5-bin.zip
```

2. Use the wrapper to auto-download the correct version:

```bash
./gradlew --version
```

3. Update the wrapper to a newer version:

```bash
./gradlew wrapper --gradle-version 8.5
```

4. Check plugin compatibility with the current Gradle version:

```bash
./gradlew build --info 2>&1 | grep -i "version\|compatib"
```

## Examples

```bash
# Error output
This version of Gradle requires Gradle 8.0 or later.
  You are currently using Gradle 7.6.3.
```

```properties
# gradle-wrapper.properties with explicit version
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-8.5-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
```

## Related Errors

- [Gradle Wrapper Error]({{< relref "/tools/gradle/gradle-wrapper-error" >}}) -- wrapper download issues
- [Gradle Version Error]({{< relref "/tools/gradle/gradle-version-error" >}}) -- version compatibility issues
