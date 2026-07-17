---
title: "Gradle Version Incompatibility Error"
description: "Gradle version is incompatible with the project or its plugins."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gradle", "version", "compatibility", "upgrade", "wrapper"]
weight: 5
---

# Gradle Version Incompatibility Error

This error occurs when the Gradle version used to build the project is incompatible with a plugin, the build script syntax, or the Gradle wrapper configuration. The build fails before any tasks execute.

## Common Causes

- Gradle wrapper version too old for required plugins
- Build script uses features from a newer Gradle version
- Plugin requires a minimum Gradle version
- Gradle distribution corrupted during download

## How to Fix

### Check Current Gradle Version

```bash
./gradlew --version
```

### Update the Gradle Wrapper

```bash
./gradlew wrapper --gradle-version 8.5
```

### Verify Plugin Compatibility

```groovy
// Check minimum Gradle version in plugin docs
plugins {
    id 'com.android.application' version '8.2.0' // requires Gradle 8.2+
}
```

### Use a Specific Gradle Distribution

```properties
# gradle-wrapper.properties
distributionUrl=https\://services.gradle.org/distributions/gradle-8.5-bin.zip
```

### Enable Gradle Compatibility Checks

```groovy
// build.gradle
task checkGradleVersion {
    doLast {
        assert GradleVersion.current() >= GradleVersion.version('8.0')
    }
}
```

### Upgrade Build Script Syntax

```groovy
// Old syntax (deprecated)
apply plugin: 'java'

// New syntax
plugins {
    id 'java'
}
```

## Examples

```text
Minimum supported Gradle version is 8.0. Current version is 7.6.2.

The build script uses Gradle 8.x syntax but you are running Gradle 7.x.
```

## Related Errors

- [Gradle Plugin Error]({{< relref "/tools/gradle/gradle-plugin-error" >}}) — plugin not found
- [Gradle Wrapper Error]({{< relref "/tools/gradle/gradle-wrapper-error" >}}) — wrapper download failure
- [Gradle Configuration Error]({{< relref "/tools/gradle/gradle-configuration-error" >}}) — script evaluation failure
