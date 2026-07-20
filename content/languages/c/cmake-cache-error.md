---
title: "[Solution] CMAKE_CACHE_ERROR — CMake cache error"
description: "Fix CMake cache errors by deleting CMakeCache.txt, reconfiguring, and cleaning the build directory. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["cmake-error"]
weight: 814
---

# CMAKE_CACHE_ERROR — CMake cache error

CMake encounters an error reading or writing its cache file (`CMakeCache.txt`). The cache stores configuration variables from previous runs, and corruption or stale values can cause build failures.

## Common Causes

```bash
# Cause 1: Stale cache from changed environment
# Previously configured with GCC, now trying to use Clang
# CMakeCache.txt still has: CMAKE_C_COMPILER:FILEPATH=/usr/bin/gcc
cmake -B build -DCMAKE_C_COMPILER=clang
# CMake Error: The compiler "/usr/bin/gcc" is not able to compile a simple test program
```

```cmake
# Cause 2: Manually edited CMakeCache.txt with invalid values
# CMAKE_INSTALL_PREFIX:PATH=/nonexistent/path
```

```bash
# Cause 3: Cache corruption from interrupted cmake process
# Ctrl+C during cmake configuration left partial cache
# Next cmake run reads corrupted cache
```

```cmake
# Cause 4: Different CMake versions with incompatible cache format
# Cache written by CMake 3.10, now running CMake 3.25
```

```bash
# Cause 5: Build directory shared between different projects
# Running cmake in the same build directory for two different projects
# Cache from project A conflicts with project B
```

## How to Fix

### Fix 1: Delete the cache and reconfigure from scratch

```bash
# Remove the entire build directory
rm -rf build

# Or just remove the cache and CMake files
rm build/CMakeCache.txt
rm -rf build/CMakeFiles

# Reconfigure
cmake -B build
```

### Fix 2: Clean build directory and use a fresh one

```bash
# Full clean rebuild
rm -rf build
mkdir build
cd build
cmake ..
cmake --build .
```

### Fix 3: Override specific cache variables without deleting

```bash
# Change compiler without deleting cache
cmake -B build -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++

# Or set other variables
cmake -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local
```

### Fix 4: Use a separate build directory for each configuration

```bash
# Debug build
cmake -B build-debug -DCMAKE_BUILD_TYPE=Debug

# Release build
cmake -B build-release -DCMAKE_BUILD_TYPE=Release

# Cross-compilation
cmake -B build-arm -DCMAKE_TOOLCHAIN_FILE=toolchain-arm.cmake
```

### Fix 5: Verify cache consistency after environment changes

```bash
# If you changed compilers or installed new libraries, clear cache first
rm -rf build/CMakeCache.txt build/CMakeFiles
cmake -B build

# Check what CMake picked up
cmake -B build 2>&1 | grep -E "compiler|CMAKE_"
cat build/CMakeCache.txt | grep CMAKE_C_COMPILER
```

## Examples

```bash
# Real-world: switching from Debug to Release build
# WRONG: cmake will use cached Debug settings
cmake -B build -DCMAKE_BUILD_TYPE=Release
# CMake Warning: CMAKE_BUILD_TYPE already set in cache

# CORRECT: clear cache first
rm build/CMakeCache.txt
cmake -B build -DCMAKE_BUILD_TYPE=Release
```

```bash
# Real-world: CI/CD pipeline clean build
# Always start fresh in CI
rm -rf build
cmake -B build \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=${INSTALL_DIR}
cmake --build build
ctest --test-dir build
cmake --install build
```

```cmake
# In CMakeLists.txt: detect stale cache and warn
if(DEFINED CMAKE_C_COMPILER AND NOT CMAKE_C_COMPILER STREQUAL "$ENV{CC}")
    message(WARNING
        "Cached compiler (${CMAKE_C_COMPILER}) differs from "
        "environment CC ($ENV{CC}). Delete CMakeCache.txt and reconfigure."
    )
endif()
```

## Related Errors

- [CMAKE_COMPILER_ERROR](/languages/c/cmake-compiler-error) — CMake compiler identification unknown
- [CMAKE_NOT_FOUND_PACKAGE](/languages/c/cmake-not-found-package) — CMake could not find package
- [CMAKE_FEATURE_ERROR](/languages/c/cmake-feature-error) — CMake feature requires specific version
