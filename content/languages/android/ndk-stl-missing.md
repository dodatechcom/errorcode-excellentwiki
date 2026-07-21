---
title: "NDK STL Configuration Error"
description: "Fix Android NDK STL (Standard Template Library) configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Native build fails because STL is not properly configured

## Common Causes

- STL not specified in CMake or ndk-build
- Using wrong STL type for shared library
- STL runtime not included in APK
- Mixed STL usage across modules

## Fixes

- Set -DANDROID_STL to c++_shared or c++_static
- Use c++_shared for shared libraries
- Ensure STL ABI matches across all native modules
- Add STL to packaging options in build.gradle

## Code Example

```kotlin
# In CMakeLists.txt
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Or in build.gradle:
android {
    defaultConfig {
        externalNativeBuild {
            cmake {
                arguments "-DANDROID_STL=c++_shared"
            }
        }
    }
}
```

# Package c++_shared.so with APK
android {
    packagingOptions {
        pickFirst 'lib/*/libc++_shared.so'
    }
}
