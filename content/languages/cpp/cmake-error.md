---
title: "[Solution] C++ CMake - configuration error"
description: "Fix C++ CMake configuration errors. Resolve CMakeLists.txt issues."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# CMake - configuration error

CMake configuration errors occur when `CMakeLists.txt` has syntax errors, missing targets, or incompatible settings.

## Common Causes

```cmake
# Cause 1: Missing target
add_executable(myapp)  # missing source files

# Cause 2: Wrong syntax
set(SOURCES main.cpp utils.cpp)  # missing quotes for paths with spaces
add_executable(myapp ${SOURCES})

# Cause 3: Missing find_package
target_link_libraries(myapp Boost::system)  # Boost not found
```

## How to Fix

### Fix 1: Check CMake syntax

```bash
cmake -S . -B build 2>&1 | head -50
```

### Fix 2: Fix CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.16)
project(MyApp)

add_executable(myapp main.cpp utils.cpp)
target_link_libraries(myapp PRIVATE Boost::system)
```

### Fix 3: Set CMake variables

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
```

## Related Errors

- [Meson - build error]({{< relref "/languages/cpp/meson-error" >}}) — Meson build errors.
- [Ninja - build error]({{< relref "/languages/cpp/ninja-error" >}}) — Ninja build errors.
- [Conan - package error]({{< relref "/languages/cpp/conan-error" >}}) — Conan errors.
