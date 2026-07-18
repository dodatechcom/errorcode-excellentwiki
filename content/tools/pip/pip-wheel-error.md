---
title: "[Solution] pip Wheel Error — Fix Failed to Build Wheel"
description: "Fix pip wheel build failures when no compatible wheel exists for your platform. Resolve binary compilation issues and install pre-built alternatives."
tools: ["pip"]
error-types: ["wheel-error"]
severities: ["error"]
weight: 5
---

This error means pip attempted to build a wheel from a source distribution but the wheel build failed. Without a compatible wheel, pip cannot complete the installation.

## What This Error Means

pip searches for a pre-built wheel matching your platform and Python version. When none exists, it falls back to building from source. If the wheel build fails:

```
ERROR: Failed to build wheel for <package>
Failed to build <package>
ERROR: Could not build wheels for <package>, which is required to install pyproject.toml-based projects
```

## Why It Happens

- The package has no pre-built wheel for your OS/architecture/Python version combination
- The build requires a C extension but the compiler is missing or incompatible
- The package uses a build backend pip cannot handle (older pip with modern pyproject.toml)
- The build process runs out of memory on resource-constrained machines
- A build dependency specified in pyproject.toml is not installed

## How to Fix It

### Upgrade pip and Build Tools

```bash
pip install --upgrade pip setuptools wheel build
pip install <package>
```

### Install Build Dependencies

Check the error log for missing build dependencies:

```bash
pip install cython numpy  # common build deps
pip install <package>
```

### Build the Wheel Manually

```bash
pip download --no-binary=:all: <package>
cd <package-dir>
pip wheel --no-deps .
pip install <package>.whl
```

### Use a Pre-Built Wheel from an Alternative Source

```bash
# PyPI may have wheels for other platforms
pip download --platform manylinux2014_x86_64 --only-binary=:all: <package>

# Try conda which often has pre-built binaries
conda install <package>
```

### Skip Binary Fallback Entirely

```bash
# Force source build but skip wheel step
pip install --no-binary <package> <package>
```

### Use Docker with a Compatible Platform

```bash
docker run -it --platform linux/amd64 python:3.11-slim pip install <package>
```

## Common Mistakes

- Not checking if the package has wheels for your platform on PyPI
- Forgetting to install build dependencies listed in pyproject.toml
- Using an outdated pip that cannot parse modern pyproject.toml files
- Not checking whether a conda-forge binary exists as an alternative

## Related Pages

- [pip Build Error]({{< relref "/tools/pip/pip-build-error" >}}) -- subprocess build failures
- [pip Dependency Conflict]({{< relref "/tools/pip/pip-dependency-conflict" >}}) -- dependency resolution
- [pip Cache Error]({{< relref "/tools/pip/pip-cache-error" >}}) -- cache corruption
