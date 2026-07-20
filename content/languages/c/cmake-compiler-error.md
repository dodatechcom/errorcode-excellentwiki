---
title: "[Solution] CMAKE_COMPILER_ERROR — CMake compiler identification unknown"
description: "Fix CMake compiler identification errors by setting CMAKE_C_COMPILER, checking the toolchain, and installing the compiler. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["cmake-error"]
weight: 812
---

# CMAKE_COMPILER_ERROR — CMake compiler identification unknown

CMake cannot identify or find the C compiler. This prevents the build system from generating project files since CMake needs to know the compiler's capabilities, flags, and features.

## Common Causes

```cmake
# Cause 1: No C compiler installed
# CMake Error at CMakeLists.txt:3 (project):
# No CMAKE_C_COMPILER could be found
```

```bash
# Cause 2: Compiler not in PATH
# gcc exists at /opt/gcc/bin/gcc but /opt/gcc/bin is not in PATH
```

```cmake
# Cause 3: Wrong compiler specified
set(CMAKE_C_COMPILER "gcc-13")  # only gcc-12 is installed
```

```cmake
# Cause 4: Cross-compilation without proper toolchain file
# Using a toolchain file that references a non-existent compiler
set(CMAKE_C_COMPILER "arm-linux-gnueabihf-gcc")
# But the cross-compiler is not installed
```

```cmake
# Cause 5: CMake cache from a previous failed configuration
# CMakeCache.txt contains stale compiler paths from a different environment
```

## How to Fix

### Fix 1: Install a C compiler

```bash
# Debian/Ubuntu
sudo apt-get install build-essential  # installs gcc and essential tools

# Fedora/RHEL
sudo dnf groupinstall "Development Tools"

# Arch
sudo pacman -S base-devel

# macOS
xcode-select --install
```

### Fix 2: Set CMAKE_C_COMPILER explicitly

```bash
# Specify the compiler on the command line
cmake -B build -DCMAKE_C_COMPILER=gcc

# Full path to compiler
cmake -B build -DCMAKE_C_COMPILER=/usr/bin/gcc-12

# Clang
cmake -B build -DCMAKE_C_COMPILER=clang
```

### Fix 3: Verify compiler is in PATH and works

```bash
# Check if gcc is available
which gcc
gcc --version

# If not in PATH, add it
export PATH="/usr/local/gcc/bin:$PATH"
cmake -B build

# Or use full path
cmake -B build -DCMAKE_C_COMPILER=/usr/local/gcc/bin/gcc
```

### Fix 4: Create or fix a toolchain file for cross-compilation

```cmake
# toolchain-arm.cmake
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR arm)
set(CMAKE_C_COMPILER "arm-linux-gnueabihf-gcc")
set(CMAKE_CXX_COMPILER "arm-linux-gnueabihf-g++")
set(CMAKE_FIND_ROOT_PATH /usr/arm-linux-gnueabihf)
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)

# Usage:
# cmake -B build -DCMAKE_TOOLCHAIN_FILE=toolchain-arm.cmake
```

### Fix 5: Clean CMake cache and reconfigure

```bash
# Remove cached configuration
rm -rf build/CMakeCache.txt
rm -rf build/CMakeFiles

# Reconfigure from scratch
cmake -B build -DCMAKE_C_COMPILER=gcc
```

## Examples

```bash
# Real-world: setting up a project with specific compiler versions
# Check available compilers
ls /usr/bin/gcc* /usr/bin/clang* 2>/dev/null

# Configure with specific version
CC=gcc-12 cmake -B build

# Or use update-alternatives (Debian/Ubuntu)
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 100
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 90
sudo update-alternatives --config gcc  # select version interactively

cmake -B build
```

```cmake
# Real-world: CMakeLists.txt with compiler validation
cmake_minimum_required(VERSION 3.16)
project(MyApp C)

# Verify compiler works
include(CheckCCompilerFlag)
check_c_compiler_flag("-Wall" HAS_WALL)
if(NOT HAS_WALL)
    message(FATAL_ERROR "Compiler does not support -Wall flag")
endif()

add_executable(app main.c)
```

## Related Errors

- [CMAKE_NOT_FOUND_PACKAGE](/languages/c/cmake-not-found-package) — CMake could not find package
- [CMAKE_CACHE_ERROR](/languages/c/cmake-cache-error) — CMake cache error
- [CMAKE_FEATURE_ERROR](/languages/c/cmake-feature-error) — CMake feature requires specific version
