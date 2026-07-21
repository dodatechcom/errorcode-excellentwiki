---
title: "NDK Build Error"
description: "Fix NDK build errors and CMake configuration failures in Android projects"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Native code compilation fails during NDK build process

## Common Causes

- CMakeLists.txt has syntax errors
- NDK version not compatible with compileSdk
- Missing native source files in jni/ directory
- C++ standard not set in CMake configuration

## Fixes

- Check CMakeLists.txt syntax
- Update NDK to version matching compileSdk
- Verify all source files listed in CMakeLists.txt
- Set CMAKE_CXX_STANDARD in CMake config

## Code Example

```kotlin
# CMakeLists.txt
cmake_minimum_required(VERSION 3.22.1)
project("native-lib")

add_library(native-lib SHARED
    native-lib.cpp
    helper.cpp)

target_link_libraries(native-lib
    android
    log)
```

# Build native code
./gradlew assembleDebug
# Check CMake output in .cxx/ directory
