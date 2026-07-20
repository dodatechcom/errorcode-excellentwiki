---
title: "[Solution] C++ Multiple Definition — Linker Error Fix"
description: "Fix C++ multiple definition errors using inline functions, header-only patterns, constexpr, and respecting the One Definition Rule."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-error"]
weight: 902
---

# C++ Multiple Definition — Linker Error Fix

A multiple definition error occurs when the linker finds the same symbol defined in more than one translation unit. This violates the One Definition Rule (ODR) and typically happens when a non-inline function or variable is defined in a header file included by multiple source files.

## Common Causes

```cpp
// Cause 1: Non-inline function defined in a header
// config.h
#pragma once
int get_version() { return 1; }  // each .cpp including this gets a copy

// a.cpp and b.cpp both include config.h
// Linker sees two definitions of get_version → error
```

```cpp
// Cause 2: Global variable defined in header
// globals.h
#pragma once
int global_counter = 0;  // definition in header — multiple definition

// a.cpp
#include "globals.h"
// b.cpp
#include "globals.h"
// Linker sees two definitions of global_counter
```

```cpp
// Cause 3: Non-inline constexpr in header (C++17 before inline was required)
// math_const.h
#pragma once
constexpr double PI = 3.14159265358979;  // in C++17 this is ok, but pre-C++17 it's a problem

// In C++17, constexpr on variables implies inline, so this is fine.
// But in older standards or with non-constexpr:
// int CONSTANT = 42;  // would cause multiple definition
```

```cpp
// Cause 4: Template specialization in header without inline
// traits.h
#pragma once
template <typename T>
struct Serializer {
    static void serialize(T val) { /* generic */ }
};

// WRONG: explicit specialization without inline
template <>
struct Serializer<int> {
    static void serialize(int val) { /* int-specific */ }
};
```

```cpp
// Cause 5: Static member variable defined in header
// myclass.h
#pragma once
class MyClass {
    static int instance_count;  // declaration only — this is fine
};
int MyClass::instance_count = 0;  // DEFINITION in header — multiple definition
```

## How to Fix

### Fix 1: Use inline Functions

```cpp
// config.h
#pragma once

// inline allows definition in multiple translation units
inline int get_version() { return 1; }
inline int compute(int x) { return x * 2; }

// Safe to include from multiple .cpp files
```

### Fix 2: Header-Only with inline Variables

```cpp
// globals.h
#pragma once

// C++17: inline variables allow definition in headers
inline int global_counter = 0;
inline constexpr double PI = 3.14159265358979;
inline const std::string app_name = "MyApp";

// a.cpp and b.cpp can both include this safely
```

### Fix 3: Use constexpr Correctly

```cpp
// math_const.h
#pragma once

// C++17: constexpr variables are implicitly inline
constexpr double PI = 3.14159265358979;
constexpr int MAX_SIZE = 1024;

// Older C++: use static constexpr in class or anonymous namespace
namespace {
    constexpr double PI_OLD = 3.14159265358979;  // anonymous namespace = internal linkage
}
```

### Fix 4: Separate Declaration and Definition

```cpp
// myclass.h
#pragma once
class MyClass {
    static int instance_count;
public:
    static int get_count();
};

// myclass.cpp — single definition
#include "myclass.h"
int MyClass::instance_count = 0;
int MyClass::get_count() { return instance_count; }
```

### Fix 5: Fix Template Specializations

```cpp
// traits.h
#pragma once
template <typename T>
struct Serializer {
    static void serialize(T val) {}
};

// C++17: inline template specialization
template <>
inline void Serializer<int>::serialize(int val) {
    // int-specific implementation
}

// Or use a function template specialization instead
template <typename T>
inline void serialize_value(T val) {
    // generic
}

template <>
inline void serialize_value<int>(int val) {
    // int-specific
}
```

## Examples

```cpp
// Real-world: ODR-safe header-only library
// mylib.h
#pragma once
#include <string>
#include <vector>

// All functions are inline — safe to include everywhere
inline std::string process(const std::string& input) {
    return "processed: " + input;
}

inline int fibonacci(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1;
    for (int i = 2; i <= n; ++i) {
        int tmp = a + b;
        a = b;
        b = tmp;
    }
    return b;
}

// inline constexpr values
inline constexpr int MAX_FIB = 46;  // largest fib that fits in int

// a.cpp
#include "mylib.h"
// b.cpp
#include "mylib.h"
// No multiple definition errors
```

## Related Errors

- [Undefined reference]({{< relref "/languages/cpp/linker-undefined-reference-cpp" >}}) — symbol not found at link time.
- [Template symbol undefined]({{< relref "/languages/cpp/linker-template-symbol" >}}) — template function not instantiated.
- [ABI incompatible]({{< relref "/languages/cpp/linker-abi-incompatible" >}}) — ABI mismatch between translation units.
