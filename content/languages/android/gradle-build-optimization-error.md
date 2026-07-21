---
title: "Build Optimization Error"
description: "Fix Gradle build performance optimization and configuration cache errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Gradle builds are slow because of configuration and optimization issues

## Common Causes

- Configuration cache not enabled
- Parallel builds not configured
- Build cache not utilized
- Dependencies downloading every build

## Fixes

- Enable configuration cache in gradle.properties
- Enable parallel and configure-on-demand
- Enable Gradle build cache
- Use dependency lock files

## Code Example

```kotlin
# gradle.properties
org.gradle.parallel=true
org.gradle.caching=true
org.gradle.configureondemand=true
org.gradle.configuration-cache=true
org.gradle.jvmargs=-Xmx4g -XX:MaxMetaspaceSize=512m

# Cache dependencies:
# Use gradle/libs.versions.toml for version catalog
# Lock dependencies: ./gradlew dependencies --write-locks
```

# Build scan for performance analysis:
# ./gradlew assembleDebug --scan
# Use build cache for incremental builds
