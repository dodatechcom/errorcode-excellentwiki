---
title: "[Solution] CMAKE_TARGET_NOT_FOUND — CMake target not found"
description: "Fix CMake target not found errors by adding subdirectories, using find_package, and checking target name spelling. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["cmake-error"]
weight: 813
---

# CMAKE_TARGET_NOT_FOUND — CMake target not found

CMake cannot find a target that is referenced in `target_link_libraries` or similar commands. This happens when the target has not been defined, the subdirectory containing it was not added, or the package providing it was not found.

## Common Causes

```cmake
# Cause 1: Missing add_subdirectory or find_package
add_executable(app main.c)
target_link_libraries(app mylib)  # ERROR: target "mylib" not found
# Forgot to add: add_subdirectory(mylib) or find_package(mylib)
```

```cmake
# Cause 2: Target name typo
add_library(MyLibrary STATIC src.c)
target_link_libraries(app Mylib)  # typo: lowercase 'l' vs uppercase 'L'
```

```cmake
# Cause 3: Target defined inside an if() block that was not taken
option(ENABLE_FEATURE "Enable feature" OFF)
if(ENABLE_FEATURE)
    add_library(feature_lib STATIC feature.c)
endif()
target_link_libraries(app feature_lib)  # ERROR when ENABLE_FEATURE=OFF
```

```cmake
# Cause 4: Using imported target from find_package before calling find_package
target_link_libraries(app OpenSSL::SSL)  # ERROR: OpenSSL not found yet
find_package(OpenSSL REQUIRED)
```

```cmake
# Cause 5: Target defined in a parent scope but not exported
# Subdirectory defines target but doesn't propagate it
add_subdirectory(deps/foo)
target_link_libraries(app foo::foo)  # foo::foo defined inside deps/foo/ but not visible
```

## How to Fix

### Fix 1: Add the required subdirectory or find_package before using the target

```cmake
cmake_minimum_required(VERSION 3.16)
project(MyApp C)

# Add subdirectory that defines the target
add_subdirectory(deps/mylib)

add_executable(app main.c)
target_link_libraries(app mylib)  # now mylib is defined
```

### Fix 2: Verify exact target name spelling

```bash
# List all targets in the build
cmake --build build --target help 2>/dev/null | head -20

# Or in CMakeLists.txt, print available targets
get_property(all_targets DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY BUILDSYSTEM_TARGETS)
message(STATUS "Available targets: ${all_targets}")
```

### Fix 3: Ensure targets defined in conditionals have fallbacks

```cmake
option(ENABLE_FEATURE "Enable feature" OFF)

if(ENABLE_FEATURE)
    add_library(feature_lib STATIC feature.c)
else()
    # Provide a stub target so linking doesn't fail
    add_library(feature_lib STATIC stub.c)
endif()

add_executable(app main.c)
target_link_libraries(app feature_lib)  # always works
```

### Fix 4: Call find_package before using imported targets

```cmake
# WRONG:
target_link_libraries(app OpenSSL::SSL)
find_package(OpenSSL REQUIRED)

# CORRECT:
find_package(OpenSSL REQUIRED)
target_link_libraries(app OpenSSL::SSL)
```

### Fix 5: Propagate targets properly from subdirectories

```cmake
# In deps/foo/CMakeLists.txt
add_library(foo STATIC foo.c)
# Target is automatically visible to parent after add_subdirectory

# In parent CMakeLists.txt
add_subdirectory(deps/foo)
target_link_libraries(app foo)  # foo is visible

# For imported targets, create an alias
add_library(foo::foo ALIAS foo)
target_link_libraries(app foo::foo)  # works with namespaced name
```

## Examples

```cmake
# Real-world: project with multiple library dependencies
cmake_minimum_required(VERSION 3.16)
project(NetworkApp C)

# External dependencies via find_package
find_package(OpenSSL REQUIRED)
find_package(CURL REQUIRED)

# Internal libraries via add_subdirectory
add_subdirectory(deps/protocol)
add_subdirectory(deps/utils)

add_executable(app main.c)
target_link_libraries(app
    protocol          # internal target
    utils             # internal target
    OpenSSL::SSL      # external imported target
    CURL::libcurl     # external imported target
)
```

```bash
# Debugging: check if a target exists before using it
cmake -B build 2>&1 | grep -i "target.*not found"

# In CMakeLists.txt, add a check
if(NOT TARGET mylib)
    message(FATAL_ERROR "Target 'mylib' not found. Did you forget add_subdirectory()?")
endif()
```

## Related Errors

- [CMAKE_NOT_FOUND_PACKAGE](/languages/c/cmake-not-found-package) — CMake could not find package
- [CMAKE_CACHE_ERROR](/languages/c/cmake-cache-error) — CMake cache error
- [C UNDEFINED_REFERENCE](/languages/c/linker-undefined-reference) — Undefined reference to symbol
