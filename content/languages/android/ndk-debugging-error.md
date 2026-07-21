---
title: "NDK Debug Configuration Error"
description: "Fix native code debugging configuration errors in Android NDK projects"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Cannot debug native code in Android Studio due to misconfiguration

## Common Causes

- ndk-build or cmake not configured for debug symbols
- Debug build type missing debuggable flag
- LLDB configuration file missing
- Source path mapping incorrect in debug config

## Fixes

- Ensure debuggable true in debug build type
- Add -g flag to CMake compile options
- Create .lldbinit or lldbconfig.txt
- Set sourceRoots in native debug config

## Code Example

```kotlin
android {
    buildTypes {
        debug {
            debuggable true
            jniDebuggable true
        }
    }
}

# In CMakeLists.txt for debug symbols:
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_options(mylib PRIVATE -g -O0)
endif()
```

# Debug native code
# Run app, then attach LLDB:
# Run > Edit Configurations > Android App > debug type = Native
