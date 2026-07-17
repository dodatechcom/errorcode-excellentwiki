---
title: "Gradle Plugin Application Error"
description: "Gradle fails to apply a plugin due to version conflicts, missing dependencies, or configuration errors."
tools: ["gradle"]
error-types: ["build-error"]
severities: ["error"]
tags: ["gradle", "plugin", "application", "version", "buildscript"]
weight: 5
---

# Gradle Plugin Application Error

A plugin application error occurs when Gradle cannot apply a plugin to the build. This happens during the build script evaluation phase when the `plugins` or `apply plugin` directive fails.

## Common Causes

- Plugin version not found in configured repositories
- Plugin version incompatible with Gradle version
- Conflicting plugin versions between build scripts
- Plugin dependency conflicts

## How to Fix

### Use Correct Plugin Syntax

```groovy
// Modern syntax
plugins {
    id 'com.android.application' version '8.1.0' apply true
}

// Legacy syntax
buildscript {
    dependencies {
        classpath 'com.android.tools.build:gradle:8.1.0'
    }
}
apply plugin: 'com.android.application'
```

### Check Plugin Repository

```groovy
pluginManagement {
    repositories {
        gradlePluginPortal()
        mavenCentral()
        google()
    }
}
```

### Verify Version Compatibility

Check the plugin's documentation for required Gradle version.

### Resolve Plugin Conflicts

```groovy
// In settings.gradle
pluginManagement {
    resolutionStrategy {
        eachPlugin {
            if (requested.id.id == 'com.android.application') {
                useModule("com.android.tools.build:gradle:${requested.version}")
            }
        }
    }
}
```

### Update Plugin Version

```groovy
plugins {
    id 'com.android.application' version '8.2.0' apply true  // update
}
```

## Examples

```bash
./gradlew build
# FAILURE: Plugin [id: 'com.android.application', version: '8.1.0']
# was not found in any of the following sources:
# - Plugin Repositories (plugin management)
# - Gradle Central Plugin Repository
```

## Related Errors

- [Version Error]({{< relref "/tools/gradle/gradle-version-error" >}}) — Gradle version mismatch
- [Build Failed]({{< relref "/tools/gradle/gradle-build-failed" >}}) — general build failure
- [Configuration Error]({{< relref "/tools/gradle/gradle-configuration-error" >}}) — build configuration error
