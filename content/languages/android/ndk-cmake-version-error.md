---
title: "CMake Version Error"
description: "Fix CMake version mismatch errors for Android NDK builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
NDK build fails because required CMake version is not installed

## Common Causes

- CMake version not specified in build.gradle
- Installed CMake version differs from required
- CMake binary path incorrect in local.properties
- Multiple CMake versions causing conflict

## Fixes

- Specify CMake version in build.gradle android block
- Install required CMake version via SDK Manager
- Set cmake path in build.gradle externalNativeBuild
- Use SDK Manager to install correct version

## Code Example

```kotlin
android {
    externalNativeBuild {
        cmake {
            version "3.22.1"
            path "src/main/cpp/CMakeLists.txt"
        }
    }
}
```

# Install CMake via SDK Manager
$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager "cmake;3.22.1"
# Verify installation
ls $ANDROID_HOME/cmake/3.22.1/bin/cmake
