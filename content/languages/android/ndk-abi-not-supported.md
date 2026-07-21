---
title: "ABI Not Supported Error"
description: "Fix unsupported ABI errors when building native code for Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build fails because target ABI is not supported by NDK or device

## Common Causes

- Trying to build for armeabi (removed ABI)
- ABI not listed in abiFilters
- NDK version does not support requested ABI
- Native library compiled for wrong ABI

## Fixes

- Use supported ABIs: armeabi-v7a, arm64-v8a, x86, x86_64
- Add abiFilters in build.gradle ndk block
- Check NDK release notes for supported ABIs
- Provide prebuilt libraries for each target ABI

## Code Example

```kotlin
android {
    defaultConfig {
        ndk {
            abiFilters 'arm64-v8a', 'armeabi-v7a', 'x86_64'
        }
    }
}
```

# Check what ABIs your native libs support
file libmylib.so
# Or use readelf
readelf -h libmylib.so | grep Machine
