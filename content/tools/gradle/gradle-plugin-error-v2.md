---
title: "Gradle Plugin Was Not Found"
description: "Gradle cannot find a required plugin in any configured repository."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gradle", "plugin", "not-found", "repository", "configuration"]
weight: 5
---

# Gradle Plugin Was Not Found

This error occurs when Gradle cannot find a plugin specified in the build script. The plugin may not exist in the configured repositories, or the plugin ID may be incorrect.

## Common Causes

- Plugin ID is misspelled or uses the wrong group
- Plugin repository not configured (e.g., missing `gradlePluginPortal()`)
- Plugin version does not exist
- Network issues preventing plugin download
- Plugin is published under a different ID

## How to Fix

### Add the Gradle Plugin Portal

```groovy
// settings.gradle
pluginManagement {
    repositories {
        gradlePluginPortal()
        mavenCentral()
    }
}
```

### Verify Plugin ID and Version

```groovy
plugins {
    id 'com.example.plugin' version '1.0.0' apply false
}
```

### Use Legacy Plugin Application

```groovy
buildscript {
    repositories {
        maven { url 'https://plugins.gradle.org/m2/' }
    }
    dependencies {
        classpath 'com.example:plugin:1.0.0'
    }
}
apply plugin: 'com.example.plugin'
```

### Check Plugin Portal

Visit [plugins.gradle.org](https://plugins.gradle.org) to search for the correct plugin ID.

### Use Snapshot Version if Needed

```groovy
plugins {
    id 'com.example.plugin' version '1.1.0-SNAPSHOT'
}
```

## Examples

```text
* What went wrong:
  Plugin [id: 'com.example.unknown', version: '1.0.0'] was not found
  in any of the following sources:
  - Gradle Plugin Portal (plugins.gradle.org)
  - Maven Central (repo.maven.apache.org)
```

## Related Errors

- [Gradle Version Error]({{< relref "/tools/gradle/gradle-version-error" >}}) — version incompatibility
- [Gradle Wrapper Error]({{< relref "/tools/gradle/gradle-wrapper-error" >}}) — wrapper download failure
- [Gradle Configuration Error]({{< relref "/tools/gradle/gradle-configuration-error" >}}) — script evaluation failure
