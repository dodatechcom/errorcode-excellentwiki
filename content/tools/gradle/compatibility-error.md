---
title: "[Solution] Gradle Version Incompatibility"
description: "Fix Gradle version incompatibility errors. Resolve wrapper and API compatibility issues."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gradle", "version", "incompatible", "wrapper", "upgrade"]
weight: 5
---

# Gradle Version Incompatibility

A version incompatibility error means the Gradle wrapper version does not support the features, APIs, or plugins used in the build script. Older Gradle versions may lack required APIs or have changed behavior.

## Common Causes

- The `gradle-wrapper.properties` specifies an outdated Gradle version
- A plugin requires a newer Gradle version than what is configured
- Deprecated API usage that was removed in the current version
- Build script uses features only available in newer Gradle releases

## How to Fix

### Check Current Gradle Version

```bash
./gradlew --version
```

### Update the Gradle Wrapper

```bash
./gradlew wrapper --gradle-version 8.5
```

### Check Plugin Gradle Requirements

```bash
# Review the plugin's documentation for minimum Gradle version
# Example: Spring Boot 3.x requires Gradle 7.5+
```

### Fix Deprecated API Usage

```groovy
// OLD: deprecated in Gradle 7+
testCompile 'junit:junit:4.13'

// NEW: use testImplementation
testImplementation 'junit:junit:4.13'
```

### Pin a Stable Version

```properties
# gradle/wrapper/gradle-wrapper.properties
distributionUrl=https\://services.gradle.org/distributions/gradle-8.5-bin.zip
```

## Examples

```bash
# Plugin requires Gradle 8.0+
./gradlew build
# FAILURE: Plugin 'com.example.plugin' requires Gradle 8.0 or later.
# Fix: ./gradlew wrapper --gradle-version 8.5

# Deprecated API removed
./gradlew build
# FAILURE: Could not find method testCompile() for arguments
# Fix: replace testCompile with testImplementation
```

## Related Errors

- [Java Version]({{< relref "/tools/gradle/java-version" >}}) — JDK version mismatch
- [Plugin Error]({{< relref "/tools/gradle/plugin-error" >}}) — plugin not found
