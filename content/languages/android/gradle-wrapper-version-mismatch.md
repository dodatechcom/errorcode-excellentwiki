---
title: "Gradle Wrapper Version Mismatch"
description: "Fix Gradle wrapper version mismatch and distribution download errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
The Gradle wrapper cannot download or use the specified distribution version

## Common Causes

- gradle-wrapper.properties has wrong distributionUrl
- Gradle distribution not available for current platform
- Local Java version incompatible with Gradle version
- Corrupted wrapper JAR file

## Fixes

- Update gradle-wrapper.properties with correct URL
- Use compatible Java and Gradle versions
- Regenerate wrapper with gradle wrapper command
- Download wrapper JAR from official source

## Code Example

```kotlin
# gradle-wrapper.properties
distributionUrl=https\://services.gradle.org/distributions/gradle-8.2-bin.zip
# Ensure Java 17 for Gradle 8.x
```

# Regenerate wrapper
gradle wrapper --gradle-version 8.2
# Then sync again
