---
title: "[Solution] CMAKE_NOT_FOUND_PACKAGE — CMake could not find package"
description: "Fix CMake could not find package errors by setting Package_DIR, installing the package, or using FindPackage. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["cmake-error"]
weight: 811
---

# CMAKE_NOT_FOUND_PACKAGE — CMake could not find package

CMake cannot locate a required package during configuration. This happens when the package is not installed, the install path is non-standard, or `find_package` cannot locate the package's configuration files.

## Common Causes

```cmake
# Cause 1: Package not installed on the system
find_package(OpenSSL REQUIRED)
# CMake Error: Could not find a package configuration file provided by "OpenSSL"
```

```cmake
# Cause 2: Package installed in a non-standard location
find_package(MyLib REQUIRED)
# Installed to /opt/mylib/lib/cmake/MyLib/ but CMAKE_PREFIX_PATH not set
```

```cmake
# Cause 3: Wrong package name or version
find_package(Boost 1.80 REQUIRED)  # only Boost 1.74 is installed
```

```cmake
# Cause 4: Missing development files (only runtime libs installed)
# libfoo.so exists but FooConfig.cmake or FindFoo.cmake is missing
```

```cmake
# Cause 5: Using CONFIG mode when only MODULE mode works (or vice versa)
find_package(ZLIB CONFIG REQUIRED)   # only FindZLIB.cmake exists, no ZLIBConfig.cmake
```

## How to Fix

### Fix 1: Install the required package

```bash
# Debian/Ubuntu
sudo apt-get install libssl-dev       # for OpenSSL
sudo apt-get install libcurl4-openssl-dev  # for CURL

# Fedora/RHEL
sudo dnf install openssl-devel

# From source
cmake -B build -DCMAKE_INSTALL_PREFIX=/usr/local
cmake --build build
sudo cmake --install build
```

### Fix 2: Set CMAKE_PREFIX_PATH to the package location

```bash
# If package is installed in a non-standard location
cmake -B build -DCMAKE_PREFIX_PATH=/opt/mylib;/usr/local

# Or in CMakeLists.txt
set(CMAKE_PREFIX_PATH "/opt/mylib" ${CMAKE_PREFIX_PATH})
find_package(MyLib REQUIRED)
```

### Fix 3: Set the package's specific config directory

```bash
# If you know exactly where the config file is
cmake -B build -DMyLib_DIR=/opt/mylib/lib/cmake/MyLib

# Or in CMakeLists.txt
set(MyLib_DIR "/opt/mylib/lib/cmake/MyLib")
find_package(MyLib REQUIRED)
```

### Fix 4: Try MODULE mode or use find_library directly

```cmake
# If CONFIG mode fails, try MODULE
find_package(ZLIB MODULE REQUIRED)

# Or find the library directly
find_library(ZLIB_LIB z)
find_path(ZLIB_INCLUDE zlib.h)
if(ZLIB_LIB AND ZLIB_INCLUDE)
    add_library(ZLIB::ZLIB UNKNOWN IMPORTED)
    set_target_properties(ZLIB::ZLIB PROPERTIES
        IMPORTED_LOCATION "${ZLIB_LIB}"
        INTERFACE_INCLUDE_DIRECTORIES "${ZLIB_INCLUDE}"
    )
endif()
```

### Fix 5: Check package name and version requirements

```cmake
# Verify correct package name (case-sensitive)
find_package(PkgConfig)
pkg_check_modules(SSL openssl)

# Or lower version requirement
find_package(Boost 1.65 REQUIRED COMPONENTS system filesystem)

# Check what's available
find_package(Boost COMPONENTS system filesystem)
message(STATUS "Boost found: ${Boost_FOUND}")
message(STATUS "Boost version: ${Boost_VERSION}")
```

## Examples

```cmake
# Real-world: project with multiple dependencies
cmake_minimum_required(VERSION 3.16)
project(MyApp C)

# Set search paths for non-standard installations
list(APPEND CMAKE_PREFIX_PATH "/opt/custom-libs")
set(OpenSSL_DIR "/opt/openssl/lib/cmake/OpenSSL")

find_package(OpenSSL 3.0 REQUIRED)
find_package(CURL REQUIRED)
find_package(PkgConfig REQUIRED)
pkg_check_modules(JSON REQUIRED json-c)

add_executable(app main.c)
target_link_libraries(app OpenSSL::SSL CURL::libcurl ${JSON_LIBRARIES})
target_include_directories(app PRIVATE ${JSON_INCLUDE_DIRS})
```

```bash
# Debugging: verbose mode shows where CMake searches
cmake -B build --log-level=VERBOSE 2>&1 | grep -i "find"

# List all search paths
cmake -B build --graphize=deps 2>&1 | head -20

# Check if a package provides a config file
find /usr -name "*Config.cmake" -o -name "*-config.cmake" 2>/dev/null
```

## Related Errors

- [C CANNOT_FIND_LIBRARY](/languages/c/linker-cannot-find-library) — Cannot find -l
- [CMAKE_COMPILER_ERROR](/languages/c/cmake-compiler-error) — CMake compiler identification unknown
- [CMAKE_TARGET_NOT_FOUND](/languages/c/cmake-target-not-found) — CMake target not found
