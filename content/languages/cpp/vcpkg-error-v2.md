---
title: "[Solution] vcpkg Dependency Conflict Error Fix"
description: "Fix vcpkg dependency conflict errors. Handle version conflicts, feature resolution, and overlay port issues."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["vcpkg", "package-manager", "dependency", "conflict"]
weight: 5
---

# vcpkg Dependency Conflict Error

Fix vcpkg dependency conflict errors. Handle version conflicts, feature resolution, and overlay port issues.

## What This Error Means

vcpkg dependency conflicts occur when two packages require incompatible versions:

```
error: vcpkg was unable to find a dependency conflict
error: curl[core] requires openssl[core] >=1.1.0 but openssl/1.0.2 is installed
```

## Common Causes

```json
// Cause 1: Version constraints from different packages
// Cause 2: Feature selection pulls in incompatible dependencies
// Cause 3: Custom overlay port conflicts with baseline
// Cause 4: Missing triplet configuration
```

## How to Fix

### Fix 1: Use versioning in vcpkg.json

```json
{
    "name": "myapp",
    "version-string": "1.0",
    "dependencies": [
        {
            "name": "curl",
            "version>=": "7.88.0"
        },
        {
            "name": "openssl",
            "version>=": "3.0.0"
        }
    ]
}
```

### Fix 2: Set a consistent baseline

```json
{
    "name": "myapp",
    "version-string": "1.0",
    "builtin-baseline": "abc123def456...",
    "dependencies": ["boost", "fmt"]
}
```

### Fix 3: Use overlay ports for custom versions

```bash
vcpkg install --overlay-ports=./my-ports --overlay-triplets=./my-triplets
```

## Examples

```json
{
    "name": "myapp",
    "version-string": "1.0.0",
    "dependencies": [
        {
            "name": "fmt",
            "version>=": "10.1.0"
        },
        {
            "name": "spdlog",
            "features": ["external-fmt"],
            "version>=": "1.12.0"
        }
    ],
    "overrides": [
        {
            "name": "zlib",
            "version": "1.2.13"
        }
    ]
}
```

```bash
# Install dependencies with vcpkg
cmake -B build -DCMAKE_TOOLCHAIN_FILE=[vcpkg root]/scripts/buildsystems/vcpkg.cmake
cmake --build build
```

## Related Errors

- [Vcpkg Error]({{< relref "/languages/cpp/vcpkg-error" >}}) — vcpkg error
- [Conan Error]({{< relref "/languages/cpp/conan-error-v2" >}}) — Conan error
- [CMake Error]({{< relref "/languages/cpp/cmake-error-v2" >}}) — CMake error
