---
title: "FFI - native library load error"
description: "Flutter FFI fails to load a native shared library due to missing files or platform incompatibility"
frameworks: ["flutter"]
error-types: ["build-error"]
severities: ["error"]
tags: ["flutter", "ffi", "native", "shared-library", "dynamic", "c", "c++"]
weight: 5
---

A Flutter FFI native library load error occurs when `DynamicLibrary.open()` or `Package.swift` fails to locate or load the required shared library. This is common when using dart:ffi to call native C/C++ code from Flutter.

## Common Causes

- Shared library file (.so/.dylib/.dll) not included in the build
- Library architecture mismatch (arm64 vs x86_64)
- Incorrect library name or path in the FFI binding
- Missing native library dependencies
- Library not bundled correctly for the target platform

## How to Fix

1. Include the library in the correct platform directories:

```
android/
  app/
    src/
      main/
        jniLibs/
          arm64-v8a/
            libnative.so
          armeabi-v7a/
            libnative.so
ios/
  Runner/
    Libs/
      libnative.dylib
```

2. Load the library with platform detection:

```dart
import 'dart:ffi';
import 'dart:io' show Platform;

DynamicLibrary openLibrary() {
  if (Platform.isAndroid) {
    return DynamicLibrary.open('libnative.so');
  } else if (Platform.isIOS) {
    return DynamicLibrary.process();
  } else if (Platform.isLinux) {
    return DynamicLibrary.open('libnative.so');
  } else if (Platform.isMacOS) {
    return DynamicLibrary.open('libnative.dylib');
  } else if (Platform.isWindows) {
    return DynamicLibrary.open('native.dll');
  }
  throw UnsupportedError('Platform not supported');
}
```

3. Verify library architecture:

```bash
file android/app/src/main/jniLibs/arm64-v8a/libnative.so
# Should show: ELF 64-bit LSB shared object, ARM aarch64
```

4. Check for missing native dependencies:

```bash
ldd libnative.so
# Shows shared library dependencies
```

5. Update CMakeLists for Android native builds:

```cmake
# android/app/CMakeLists.txt
add_library(native SHARED native.c)
target_link_libraries(native log android)
```

## Examples

```dart
// Error: Failed to load dynamic library 'libnative.so'
final dylib = DynamicLibrary.open('libnative.so');
// dlopen failed: library "libnative.so" not found

// Fix: verify file exists in the correct directory
ls android/app/src/main/jniLibs/arm64-v8a/
```

## Related Errors

- [Build error]({{< relref "/frameworks/flutter/flutter-build-error-v2" >}})
- [Platform error]({{< relref "/frameworks/flutter/flutter-platform-error-v2" >}})
