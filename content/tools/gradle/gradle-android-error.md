---
title: "Android Gradle Minimum SDK Error"
description: "Android Gradle build fails due to minimum SDK version configuration error."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Android Gradle — Minimum SDK Error

This error occurs when the Android Gradle plugin detects a mismatch between the configured `minSdkVersion` and the requirements of dependencies or the compile SDK version.

## Common Causes

- `minSdkVersion` higher than target device API level
- Library dependency requires higher `minSdkVersion`
- Compile SDK version incompatible with Gradle plugin
- AGP version incompatible with Gradle version
- Build tools version mismatch

## How to Fix

### Set Compatible SDK Versions

```groovy
android {
    compileSdk 34
    defaultConfig {
        minSdk 24
        targetSdk 34
    }
}
```

### Check Library minSdk Requirements

```groovy
dependencies {
    // Check library docs for minSdk requirement
    implementation 'com.google.android.material:material:1.11.0' // requires minSdk 21
}
```

### Update Android Gradle Plugin

```groovy
// buildscript or settings.gradle
plugins {
    id 'com.android.application' version '8.2.0'
}
```

### Match AGP and Gradle Versions

```properties
# gradle-wrapper.properties
distributionUrl=https\://services.gradle.org/distributions/gradle-8.5-bin.zip

# build.gradle
plugins {
    id 'com.android.application' version '8.2.0' // requires Gradle 8.2+
}
```

### Use compileSdkPreview for Latest SDK

```groovy
android {
    compileSdkPreview "VanillaIceCream"
}
```

## Examples

```text
Manifest merger failed :
  uses-sdk:minSdkVersion 14 cannot be smaller than
  version 21 declared in library [com.google.android.material:material:1.11.0]

Minimum supported Gradle version is 8.2. Current version is 7.6.
```

## Related Errors

- [Gradle Version Error]({{< relref "/tools/gradle/gradle-version-error" >}}) — Gradle version incompatibility
- [Gradle Dependency Error]({{< relref "/tools/gradle/gradle-dependency-error" >}}) — dependency resolution failure
- [Gradle Build Failed]({{< relref "/tools/gradle/gradle-build-failed" >}}) — general build failure
