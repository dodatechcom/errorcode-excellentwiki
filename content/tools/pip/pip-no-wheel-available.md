---
title: "[Solution] pip No Wheel Available -- Fix No Compatible Wheel"
description: "Fix pip no wheel available errors when no compatible wheel exists for your platform. Build from source or use platform-specific index."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip cannot find a compatible wheel for your operating system, architecture, and Python version.

## Common Causes

- The package does not provide wheels for all platforms
- Your Python version is not supported
- Your architecture (e.g., ARM) is not covered
- The package is Windows-only

## How to Fix

### 1. Allow Source Distribution

```bash
pip install <package>  # without --only-binary
```

### 2. Use platform498 Index

```bash
pip install <package> --platform manylinux2014_x86_64 --python-version 3.11
```

### 3. Install Build Tools

```bash
sudo apt install build-essential python3-dev
```

### 4. Use Docker for Consistent Builds

```bash
docker run -it python:3.11 pip install <package>
```

## Examples

```bash
$ pip install --only-binary=:all: lxml
ERROR: No matching distribution found for lxml

$ pip install lxml  # allows source build
Building wheel for lxml (setup.py) ... done
```
