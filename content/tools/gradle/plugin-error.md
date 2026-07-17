---
title: "[Solution] Gradle Plugin Not Found"
description: "Fix Gradle plugin not found errors. Resolve plugin resolution and repository issues."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Gradle Plugin Not Found

This error means Gradle could not resolve a plugin specified in `build.gradle`. The plugin may not exist in the configured repositories or the plugin ID may be wrong.

## Common Causes

- The plugin ID is misspelled or incorrect
- The plugin repository (e.g., Gradle Plugin Portal) is not in `pluginManagement`
- The plugin version is not specified and cannot be resolved
- The plugin is a custom plugin not published to any repository

## How to Fix

### Verify Plugin ID and Repository

```groovy
// settings.gradle
pluginManagement {
    repositories {
        gradlePluginPortal()
        mavenCentral()
    }
}
```

### Specify Plugin Version Explicitly

```groovy
plugins {
    id 'com.example.myplugin' version '1.2.3'
}
```

### Publish Custom Plugin to Local Maven

```bash
./gradlew publishToMavenLocal
```

### Check Available Plugins

```bash
# Search Gradle Plugin Portal
# https://plugins.gradle.org/
```

### Use Buildscript Block for Legacy Plugins

```groovy
buildscript {
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath 'com.example:myplugin:1.2.3'
    }
}

apply plugin: 'com.example.myplugin'
```

## Examples

```groovy
// Wrong plugin ID
plugins {
    id 'spring-boot' version '3.1.0'  // Plugin not found
}
// Fix: id 'org.springframework.boot' version '3.1.0'

// Missing repository
plugins {
    id 'com.example.custom' version '1.0.0'  // Plugin not found
}
// Fix: add the repository in settings.gradle pluginManagement
```

## Related Errors

- [Configuration Error]({{< relref "/tools/gradle/config-error4" >}}) — build script evaluation failure
- [Compatibility Error]({{< relref "/tools/gradle/compatibility-error" >}}) — Gradle version incompatibility
