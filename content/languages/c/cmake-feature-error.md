---
title: "[Solution] CMAKE_FEATURE_ERROR — CMake feature requires specific version"
description: "Fix CMake version requirement errors by updating cmake_minimum_required, setting policies, or upgrading CMake. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["cmake-error"]
weight: 815
---

# CMAKE_FEATURE_ERROR — CMake feature requires specific version

CMake encounters a command or feature that requires a newer version than what is installed. This typically happens when a `CMakeLists.txt` uses modern CMake features with an older CMake installation.

## Common Causes

```cmake
# Cause 1: Using features from a newer CMake version
cmake_minimum_required(VERSION 3.10)
project(MyApp)

# This requires CMake 3.14+:
target_precompile_headers(app PRIVATE pch.h)

# CMake Error: target_precompile_headers command not found
```

```cmake
# Cause 2: Dependency's CMakeLists.txt requires newer CMake
add_subdirectory(deps/somelib)
# deps/somelib/CMakeLists.txt has: cmake_minimum_required(VERSION 3.20)
# But system has CMake 3.16
```

```cmake
# Cause 3: Deprecated command removed in newer CMake
cmake_minimum_required(VERSION 2.8)
# CMake 3.x removed many deprecated commands
include_directories(${Boost_INCLUDE_DIRS})  # still works but old style
```

```cmake
# Cause 4: Policy CMPolicy not set for newer behavior
cmake_minimum_required(VERSION 3.10)
# CMake Warning: Policy CMP0077 is not set
```

```cmake
# Cause 5: Using generator expressions or features from newer CMake
set(SOURCES main.c)
add_executable(app ${SOURCES})
target_compile_definitions(app PRIVATE
    $<IF:$<CONFIG:Debug>,DEBUG,NDEBUG>  # requires CMake 3.12+ for some generator expressions
)
```

## How to Fix

### Fix 1: Update cmake_minimum_required to match your CMake version

```cmake
# Check your CMake version
# cmake --version

# Set minimum version to what you actually have (or need)
cmake_minimum_required(VERSION 3.16)  # if you have CMake 3.16
project(MyApp C)
```

### Fix 2: Install a newer version of CMake

```bash
# Debian/Ubuntu - install from Kitware's APT repository
sudo apt-get update
sudo apt-get install ca-certificates gpg wget
wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc | sudo gpg --dearmor -o /usr/share/keyrings/kitware-archive-keyring.gpg
echo 'deb [signed-by=/usr/share/keyrings/kitware-archive-keyring.gpg] https://apt.kitware.com/ubuntu/ jammy main' | sudo tee /etc/apt/sources.list.d/kitware.list
sudo apt-get update && sudo apt-get install cmake

# pip
pip install cmake

# snap
sudo snap install cmake --classic
```

### Fix 3: Set CMake policies for backward compatibility

```cmake
cmake_minimum_required(VERSION 3.10)

# Set specific policies
if(POLICY CMP0077)
    cmake_policy(SET CMP0077 NEW)
endif()

# Or set all policies up to a version
if(POLICY CMP0000 through CMP0XXX)
    cmake_policy(VERSION 3.10)
endif()
```

### Fix 4: Use conditional feature detection

```cmake
cmake_minimum_required(VERSION 3.10)
project(MyApp C)

# Check CMake version before using newer features
if(CMAKE_VERSION VERSION_GREATER_EQUAL "3.14")
    target_precompile_headers(app PRIVATE pch.h)
else()
    # Fallback: manually set precompiled header flags
    set_target_properties(app PROPERTIES
        COMPILE_FLAGS "-include ${CMAKE_CURRENT_SOURCE_DIR}/pch.h"
    )
endif()
```

### Fix 5: Use fallback commands for older CMake

```cmake
cmake_minimum_required(VERSION 3.10)

# Modern way (CMake 3.13+):
# target_link_directories(app PRIVATE /usr/local/lib)

# Fallback for older CMake:
target_link_libraries(app -L/usr/local/lib mylib)

# Or use full paths:
find_library(MYLIB_LIB mylib PATHS /usr/local/lib)
target_link_libraries(app ${MYLIB_LIB})
```

## Examples

```cmake
# Real-world: CMakeLists.txt with version-aware feature usage
cmake_minimum_required(VERSION 3.12)
project(MyApp VERSION 1.0 LANGUAGES C)

# Features by version:
# 3.12: target_link_directories
# 3.14: target_precompile_headers
# 3.16: file(CREATE_LINK)
# 3.19: cmake_language(DEFER)

add_executable(app main.c)

# Always available in 3.12+
target_compile_features(app PRIVATE c_std_11)

# Conditionally use newer features
if(CMAKE_VERSION VERSION_GREATER_EQUAL "3.14")
    target_precompile_headers(app PRIVATE
        PRIVATE <stdio.h> <stdlib.h>
    )
endif()

if(CMAKE_VERSION VERSION_GREATER_EQUAL "3.13")
    target_link_directories(app PRIVATE /usr/local/lib)
endif()
```

```bash
# Check what version of CMake is installed
cmake --version

# To see which policies are relevant
cmake --help-policy CMP0077
```

## Related Errors

- [CMAKE_COMPILER_ERROR](/languages/c/cmake-compiler-error) — CMake compiler identification unknown
- [CMAKE_NOT_FOUND_PACKAGE](/languages/c/cmake-not-found-package) — CMake could not find package
- [CMAKE_CACHE_ERROR](/languages/c/cmake-cache-error) — CMake cache error
