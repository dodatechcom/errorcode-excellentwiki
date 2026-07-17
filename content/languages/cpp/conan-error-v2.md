---
title: "[Solution] Conan Package Conflict Error Fix"
description: "Fix Conan package conflict errors. Handle version conflicts, diamond dependencies, and package resolution failures."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["conan", "package-manager", "dependency", "conflict"]
weight: 5
---

# Conan Package Conflict Error

Fix Conan package conflict errors. Handle version conflicts, diamond dependencies, and package resolution failures.

## What This Error Means

Conan package conflicts occur when dependency versions are incompatible:

```
ERROR: Conflict in zlib/1.2.13@conan/stable:
    Requires zlib/1.2.13
    Requires zlib/1.2.11 (overlapping requirement)
```

## Common Causes

```python
# Cause 1: Two dependencies require different versions of the same package
# Cause 2: Lockfile out of date
# Cause 3: Package not in configured remote
# Cause 4: Recipe revision mismatch
```

## How to Fix

### Fix 1: Use version ranges for flexibility

```ini
# conanfile.txt
[requires]
zlib/[>=1.2.13 <1.3.0]
boost/1.82.0
```

### Fix 2: Set version resolution policy

```bash
# conan.conf or environment variable
conan config set general.resolver_version=full
```

### Fix 3: Use --update to refresh packages

```bash
conan install . --update --build=missing
```

### Fix 4: Pin exact versions in lockfile

```bash
conan lock create . --lockfile-out=conan.lock
conan install . --lockfile=conan.lock
```

## Examples

```python
# conanfile.py
from conan import ConanFile

class MyAppConan(ConanFile):
    name = "myapp"
    version = "1.0"
    requires = "boost/1.82.0", "fmt/10.1.1"
    default_options = {
        "boost:shared": False,
    }

    def requirements(self):
        self.requires("zlib/[>=1.2.13 <2.0.0]")

    def configure(self):
        if self.settings.os == "Linux":
            self.options["boost"].system = True
```

## Related Errors

- [Conan Error]({{< relref "/languages/cpp/conan-error" >}}) — Conan error
- [Vcpkg Error]({{< relref "/languages/cpp/vcpkg-error" >}}) — vcpkg error
- [CMake Error]({{< relref "/languages/cpp/cmake-error-v2" >}}) — CMake error
