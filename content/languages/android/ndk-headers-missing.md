---
title: "NDK Header File Missing"
description: "Fix missing NDK header file errors in Android native builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compilation fails because required NDK header files cannot be found

## Common Causes

- NDK include path not configured in CMake
- Using deprecated header from old NDK version
- Header file location changed in newer NDK
- Missing system header for target API level

## Fixes

- Add NDK include directories to CMakeLists.txt
- Update include paths for current NDK version
- Use #include <cstdio> instead of deprecated headers
- Check NDK sysroot for available headers

## Code Example

```kotlin
# CMakeLists.txt
include_directories(${ANDROID_NDK}/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include)

# Or use imported targets
find_library(log-lib log)
include_directories(${log-lib_INCLUDE_DIR})
```

# Find headers in NDK
ls $ANDROID_HOME/ndk/VERSION/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include
