---
title: "[Solution] C++ Modules Error — How to Fix"
description: "Fix C++20 module errors including import declaration failures, module interface mismatches, and partition module build issues."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time"]
weight: 5
comments: true
---

# [Solution] C++ Modules Error — How to Fix

C++20 modules replace header files with a module system that enforces proper encapsulation, but module build workflows, import declarations, and partition modules introduce new categories of compilation errors.

## Why It Happens

Module errors occur when module interface files aren't compiled before their consumers, when `export` declarations are missing from types that need public visibility, when module partitions aren't properly linked, or when build systems don't track module dependencies correctly.

## Common Error Messages

1. `error: module 'mymodule' was not found`
2. `error: 'symbol' was not declared in this module interface unit`
3. `error: module partition 'mymodule:part' not found`
4. `error: 'import' can only be used in module purview`

## How to Fix It

### Fix 1: Correct Module Interface File Structure

```cpp
// mymath.cppm — module interface file
export module mymath;

export int add(int a, int b) {
    return a + b;
}

export int multiply(int a, int b) {
    return a * b;
}
```

### Fix 2: Proper Import Declarations

```cpp
// main.cpp — module consumer
import mymath;

#include <iostream>

int main() {
    std::cout << add(2, 3) << "\n";
    std::cout << multiply(4, 5) << "\n";
    return 0;
}
```

### Fix 3: Use Module Partitions Correctly

```cpp
// mymath.geometry.cppm
export module mymath:geometry;

export double circle_area(double radius) {
    return 3.14159 * radius * radius;
}

// main.cpp
import mymath;
import mymath:geometry;
```

## Common Scenarios

- **Build order**: Module interface units (`.cppm`) must be compiled before their consumers.
- **Global module fragment**: Include `module;` before `#include` directives for compatibility with traditional headers.
- **BMI format**: Different compilers use incompatible binary module interface formats.

## Prevent It

1. Compile module interface files before any files that import them in your build system.
2. Use the global module fragment (`module;`) when mixing modules with traditional headers.
3. Keep module interfaces small and create partitions for large modules to improve build times.

## Related Errors

- [Linker error]({{< relref "/languages/cpp/linker-error" >}}) — undefined references from missing modules.
- [Concept constraint error]({{< relref "/languages/cpp/cpp-concept-constraint-error" >}}) — export missing for concepts.
- [CMake error]({{< relref "/languages/cpp/cpp-cmake-error-cpp" >}}) — build system module support.
