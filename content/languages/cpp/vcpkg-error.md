---
title: "[Solution] C++ vcpkg - package error"
description: "Fix C++ vcpkg package manager errors. Resolve vcpkg installation and build issues."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["vcpkg", "package-manager", "dependencies", "manifest", "triplet"]
weight: 5
---

# vcpkg - package error

vcpkg errors occur when packages fail to install, dependencies conflict, or triplet configuration is wrong.

## Common Causes

```json
// Cause 1: Package not found in vcpkg
{
  "dependencies": ["nonexistent-package"]
}

// Cause 2: Triplet mismatch
// Building for x64 but package only has ARM

// Cause 3: Port version conflict
{
  "dependencies": [
    { "name": "boost", "version>=": "1.83.0" }
  ]
}
```

## How to Fix

### Fix 1: Search for package

```bash
vcpkg search boost
```

### Fix 2: Fix vcpkg.json

```json
{
  "dependencies": [
    "boost-algorithm",
    "boost-system"
  ]
}
```

### Fix 3: Install with triplet

```bash
vcpkg install boost --triplet x64-linux
```

## Related Errors

- [Conan - package error]({{< relref "/languages/cpp/conan-error" >}}) — Conan errors.
- [CMake - configuration error]({{< relref "/languages/cpp/cmake-error" >}}) — CMake errors.
- [Ninja - build error]({{< relref "/languages/cpp/ninja-error" >}}) — Ninja errors.
