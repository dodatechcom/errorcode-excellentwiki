---
title: "NDK API Level Compatibility"
description: "Fix NDK compatibility errors across different Android API levels and ABIs"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Native code fails because it uses NDK APIs not available at target API level

## Common Causes

- Using NDK API removed in target API level
- Linking against libc functions not in NDK
- ABI-specific code fails on certain architectures
- NDK version incompatible with compileSdk

## Fixes

- Check NDK API availability per API level
- Use stable NDK APIs only
- Target correct ABIs in build.gradle
- Update NDK version to match compileSdk

## Code Example

```kotlin
android {
    ndkVersion "25.2.9519653"
    defaultConfig {
        ndk {
            abiFilters 'arm64-v8a', 'armeabi-v7a', 'x86_64'
        }
    }
}
```

# Check available NDK APIs
$ANDROID_HOME/ndk/VERSION/toolchains/llvm/prebuilt/linux-x86_64/bin/clang     --print-supported-cpus
# Use stable APIs documented in NDK guide
