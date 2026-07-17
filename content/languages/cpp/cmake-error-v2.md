---
title: "[Solution] CMake find_package Not Found Error Fix"
description: "Fix CMake find_package not found errors. Handle missing packages, wrong version requirements, and module path issues."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["cmake", "find_package", "build-system", "dependency"]
weight: 5
---

# CMake find_package Not Found Error

Fix CMake find_package not found errors. Handle missing packages, wrong version requirements, and module path issues.

## What This Error Means

CMake errors occur when `find_package` cannot locate a required dependency:

```
CMake Error at CMakeLists.txt:10 (find_package):
  Could not find a package configuration file provided by "Boost" with any of
  the following names: BoostConfig.cmake / boost-config.cmake
```

## Common Causes

```cmake
# Cause 1: Package not installed on system
find_package(Boost REQUIRED COMPONENTS system filesystem)

# Cause 2: Wrong package name
find_package(BoostSystem)  # Wrong - should be Boost with COMPONENTS

# Cause 3: CMAKE_PREFIX_PATH not set
# Cause 4: Version requirement too high
find_package(Boost 1.80.0 REQUIRED)  # Only 1.74 installed
```

## How to Fix

### Fix 1: Set CMAKE_PREFIX_PATH

```bash
cmake -S . -B build -DCMAKE_PREFIX_PATH=/usr/local
```

Or in CMakeLists.txt:

```cmake
list(APPEND CMAKE_PREFIX_PATH "/usr/local/lib/cmake")
find_package(Boost REQUIRED)
```

### Fix 2: Use optional find_package with fallback

```cmake
find_package(Boost QUIET COMPONENTS system)
if(Boost_FOUND)
    target_link_libraries(myapp PRIVATE Boost::system)
else()
    message(WARNING "Boost not found, building without it")
    target_compile_definitions(myapp PRIVATE NO_BOOST)
endif()
```

### Fix 3: Use FetchContent for bundled dependencies

```cmake
include(FetchContent)
FetchContent_Declare(
    fmt
    GIT_REPOSITORY https://github.com/fmtlib/fmt.git
    GIT_TAG 10.1.1
)
FetchContent_MakeAvailable(fmt)
target_link_libraries(myapp PRIVATE fmt::fmt)
```

## Examples

```cmake
cmake_minimum_required(VERSION 3.16)
project(MyApp LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)

find_package(Threads REQUIRED)

add_executable(myapp main.cpp)

# Conditional dependencies
find_package(OpenSSL QUIET)
if(OPENSSL_FOUND)
    target_link_libraries(myapp PRIVATE OpenSSL::SSL)
    target_compile_definitions(myapp PRIVATE HAS_OPENSSL)
endif()

find_package(CURL QUIET)
if(CURL_FOUND)
    target_link_libraries(myapp PRIVATE CURL::libcurl)
endif()

target_link_libraries(myapp PRIVATE Threads::Threads)
```

## Related Errors

- [CMake Error]({{< relref "/languages/cpp/cmake-error" >}}) — CMake configuration error
- [Ninja Error]({{< relref "/languages/cpp/ninja-error" >}}) — Ninja build error
- [Conan Error]({{< relref "/languages/cpp/conan-error" >}}) — Conan error
