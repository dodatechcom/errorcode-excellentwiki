---
title: "Build Scan Error"
description: "Fix Gradle build scan and performance profiling configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Gradle build scan cannot be initiated or performance data is missing

## Common Causes

- Build scan plugin not added
- Gradle Enterprise plugin not configured
- Build cache not enabled in settings.gradle
- Performance baseline not established

## Fixes

- Add Gradle Enterprise plugin to settings.gradle
- Configure build scan publication
- Enable build cache for faster builds
- Use build profiler to identify bottlenecks

## Code Example

```kotlin
// settings.gradle
plugins {
    id 'com.gradle.enterprise' version '3.16' apply false
}

gradleEnterprise {
    buildScan {
        termsOfServiceUrl = "https://gradle.com/terms-of-service"
        termsOfServiceAgree = "yes"
    }
}

// Enable build cache:
org.gradle.caching=true  # in gradle.properties
```

# Build scans provide build analysis
# Enable in gradle.properties:
# org.gradle.parallel=true
# org.gradle.caching=true
# org.gradle.configureondemand=true
