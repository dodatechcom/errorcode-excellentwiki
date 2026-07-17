---
title: "[Solution] C++ Meson - build error"
description: "Fix C++ Meson build errors. Resolve meson.build configuration issues."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# Meson - build error

Meson build errors occur when `meson.build` has configuration issues, dependency problems, or compilation failures.

## Common Causes

```python
# Cause 1: Missing dependency
project('myapp', 'cpp')
dep = dependency('nonexistent')  # not found

# Cause 2: Wrong source files
executable('myapp', 'missing_file.cpp')  # file not found

# Cause 3: Compiler not found
project('myapp', 'cpp')  # no C++ compiler installed
```

## How to Fix

### Fix 1: Check Meson setup

```bash
meson setup builddir
# Check error output
```

### Fix 2: Fix meson.build

```python
project('myapp', 'cpp', version: '1.0')

sources = files('main.cpp', 'utils.cpp')
executable('myapp', sources)
```

### Fix 3: Install dependencies

```bash
# On Ubuntu/Debian
sudo apt install build-essential meson ninja-build
```

## Related Errors

- [CMake - configuration error]({{< relref "/languages/cpp/cmake-error" >}}) — CMake errors.
- [Ninja - build error]({{< relref "/languages/cpp/ninja-error" >}}) — Ninja errors.
- [Conan - package error]({{< relref "/languages/cpp/conan-error" >}}) — Conan errors.
