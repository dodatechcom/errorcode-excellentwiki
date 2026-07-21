---
title: "Gradle Source Set Not Found"
description: "Fix missing source set errors when adding new source directories in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build cannot find a configured source directory for a given build variant

## Common Causes

- Source directory not created on disk
- Source set not declared in build.gradle
- Flavor or build type directory naming incorrect
- Manual directory addition not synced with Gradle

## Fixes

- Create the directory manually and re-sync
- Declare sourceSet in build.gradle android block
- Follow Android naming conventions for flavor dirs
- Use sourceSets.android.main.java.srcDirs += syntax

## Code Example

```kotlin
android {
    sourceSets {
        main {
            java.srcDirs = ['src/main/java', 'src/shared/java']
        }
        debug {
            java.srcDirs = ['src/debug/java']
        }
    }
}
```

# Create missing directories
mkdir -p app/src/debug/java/com/example/app
# Then re-sync Android Studio
