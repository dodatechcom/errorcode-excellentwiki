---
title: "Gradle Sync Failed"
description: "Fix Android Studio Gradle sync failed errors with dependency resolution and cache solutions"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Gradle sync failed with an error during project synchronization

## Common Causes

- Corrupted Gradle cache
- Stale build files
- Network issues downloading dependencies
- Incompatible Gradle plugin version

## Fixes

- Run 'File > Invalidate Caches / Restart'
- Delete .gradle and build directories
- Update Gradle wrapper version
- Check network proxy settings

## Code Example

```kotlin
// project-level build.gradle
plugins {
    id 'com.android.application' version '8.2.0' apply false
}
```

# Clean and rebuild
rm -rf .gradle build app/build
./gradlew clean
# Then re-sync in Android Studio
