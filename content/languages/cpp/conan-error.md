---
title: "[Solution] C++ Conan - package manager error"
description: "Fix C++ Conan package manager errors. Resolve dependency and package issues."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# Conan - package manager error

Conan errors occur during package installation, dependency resolution, or when packages fail to build.

## Common Causes

```python
# Cause 1: Package not found
[requires]
nonexistent/1.0  # recipe not in remote

# Cause 2: Version conflict
[requires]
boost/1.80.0
other-boost/1.70.0  # conflicting boost versions

# Cause 3: Binary compatibility
# Package built for different compiler/settings
```

## How to Fix

### Fix 1: Check available packages

```bash
conan search "boost/*" -r conancenter
```

### Fix 2: Fix conanfile.txt

```ini
[requires]
boost/1.83.0

[generators]
cmake_find_package
```

### Fix 3: Install and build

```bash
mkdir build && cd build
conan install .. --build=missing
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build .
```

## Related Errors

- [vcpkg - package error]({{< relref "/languages/cpp/vcpkg-error" >}}) — vcpkg errors.
- [CMake - configuration error]({{< relref "/languages/cpp/cmake-error" >}}) — CMake errors.
- [Meson - build error]({{< relref "/languages/cpp/meson-error" >}}) — Meson errors.
