---
title: "Could Not Resolve Dependency"
description: "Fix Could not resolve dependency errors in Android Gradle builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Gradle cannot resolve one or more dependencies from configured repositories

## Common Causes

- Repository URL misconfigured or unreachable
- Artifact does not exist in the repository
- Version conflict between transitive dependencies
- MavenLocal has a corrupted cached artifact

## Fixes

- Verify repository URLs in settings.gradle
- Use dependencyInsight to find conflict
- Force a specific version with resolution strategy
- Clear MavenLocal cache and re-sync

## Code Example

```kotlin
dependencies {
    implementation 'com.squareup.retrofit2:retrofit:2.9.0'
    // If this fails:
    // 1. Check repo URL
    // 2. Force version if transitive conflict
    implementation('com.squareup.okhttp3:okhttp:4.12.0') {
        force = true
    }
}
```

# Inspect dependency tree
./gradlew app:dependencies --configuration releaseRuntimeClasspath
# Find conflicting versions and apply forces
