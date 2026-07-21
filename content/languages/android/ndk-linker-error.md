---
title: "NDK Linker Error"
description: "Fix native library linker errors in Android NDK builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Native build fails during linking phase with undefined reference errors

## Common Causes

- Missing library in target_link_libraries
- Symbol not defined in any source file
- Circular dependency between native libraries
- Wrong linkage type: shared vs static

## Fixes

- Add missing library to target_link_libraries
- Implement or declare missing symbols
- Break circular dependency chain
- Use SHARED for JNI libraries, STATIC for internal

## Code Example

```kotlin
# CMakeLists.txt
add_library(mylib SHARED mylib.cpp)

# Link dependencies
find_library(log-lib log)
find_library(android-lib android)

target_link_libraries(mylib
    ${log-lib}
    ${android-lib}
    myotherlib)  # Add missing dependency
```

# Check linker errors
./gradlew assembleDebug 2>&1 | grep "undefined reference"
# Add library to target_link_libraries
