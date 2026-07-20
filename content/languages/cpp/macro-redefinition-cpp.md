---
title: "Macro Redefinition Warning - Fix"
description: "Fix macro redefinition errors and warnings using #ifndef guards, #undef before redefinition, or suppressing warnings with -Wno-macro-redefined."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 961
---

# Macro Redefinition Warning - Fix

Macro redefinition occurs when a macro is defined with the same name in multiple places. The compiler issues a warning or error depending on whether the definitions match. This often happens when include guards conflict or feature test macros collide.

## Common Causes

```cpp
// Cause 1: Redefinition in different headers
// header1.h
#define MAX_SIZE 100

// header2.h
#define MAX_SIZE 200  // redefinition warning

// main.cpp
#include "header1.h"
#include "header2.h"  // warning: 'MAX_SIZE' redefined
```

```cpp
// Cause 2: Common define across translation units
// a.cpp
#define VERSION "1.0"

// b.cpp
#define VERSION "2.0"  // each translation unit is independent; this is fine

// But if both are in the same TU via includes:
// "version.h"
#define VERSION "1.0"
// "other.h"
#define VERSION "2.0"  // redefinition
```

```cpp
// Cause 3: NOMINMAX or Windows macros conflicting
#include <windows.h>  // defines min and max macros
#include <algorithm>  // defines std::min and std::max

// Using std::min(x, y) gets preprocessed to:
// std::(x) < (y) ? (x) : (y) -- macro expansion error
```

```cpp
// Cause 4: Debug vs Release macro mismatch
// DEBUG=0 in one header vs DEBUG=1 in another
```

```cpp
// Cause 5: Feature test macros
#define __cpp_lib_filesystem 201703L
#define __cpp_lib_filesystem 201703L  // identical redefinition is OK (same value)
#define __cpp_lib_filesystem 202000L  // warning: different value
```

## How to Fix

### Fix 1: Use #ifndef guards for definitions

```cpp
// header1.h
#ifndef MAX_SIZE
#define MAX_SIZE 100
#endif

// header2.h
#ifndef MAX_SIZE
#define MAX_SIZE 200  // skipped if already defined
#endif
```

### Fix 2: Use #undef before redefining

```cpp
// When you intentionally need to change a macro:
#include "header1.h"

#undef MAX_SIZE
#define MAX_SIZE 200  // explicit undefine before redefine
```

### Fix 3: Use constexpr instead of macros

```cpp
// Instead of:
// #define MAX_SIZE 100
// #define APP_NAME "MyApp"

// Use:
constexpr int MAX_SIZE = 100;
constexpr const char* APP_NAME = "MyApp";

// These follow normal scope/namespace rules and don't have redefinition issues.
```

### Fix 4: Suppress the warning (last resort)

```bash
# GCC/Clang:
g++ -Wno-macro-redefined main.cpp -o main

# MSVC:
cl /wd4005 main.cpp  # C4005: macro redefinition
```

### Fix 5: Define macros in a single config header

```cpp
// config.h - single source of truth for all macros
#pragma once

#ifndef CONFIG_VERSION
#define CONFIG_VERSION 1

#define MAX_BUFFER 4096
#define DEFAULT_TIMEOUT 30
#define ENABLE_LOGGING 1

#endif // CONFIG_VERSION
// Include config.h everywhere instead of redefining macros
```

## Examples

```cpp
// Real-world: portable macro handling
#ifdef _WIN32
    // Windows already defines these, avoid redefining
    #ifndef NOMINMAX
        #define NOMINMAX 1  // prevent windows.h from defining min/max
    #endif
    #include <windows.h>
#else
    // On Unix, define what's needed
    #ifndef MAX_PATH
        #define MAX_PATH 4096
    #endif
#endif

// Safe debug macro
#ifndef LOG_LEVEL
    #define LOG_LEVEL 2
#endif

#if LOG_LEVEL >= 1
    #define LOG_ERROR(msg) std::cerr << "ERROR: " << msg << std::endl
#else
    #define LOG_ERROR(msg) ((void)0)
#endif
```

## Related Errors

- [Compiler version error]({{< relref "/languages/cpp/compiler-version-error" >}})
- [Multiple definition]({{< relref "/languages/cpp/linker-multiple-definition-cpp" >}})
