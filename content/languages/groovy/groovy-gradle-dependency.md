---
title: "[Solution] Gradle Dependency Error"
description: "Gradle dependency resolution errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Gradle Dependency Error

Gradle dependency resolution errors.

### Common Causes
Wrong repository; version conflict; missing

### How to Fix
```groovy
repositories {
    mavenCentral()
}
dependencies {
    implementation 'com.google.guava:guava:32.1.3-jre'
}
```

### Examples
```groovy
configurations.all {
    resolutionStrategy {
        force 'com.google.guava:guava:32.1.3-jre'
    }
}
```
