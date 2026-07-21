---
title: "[Solution] pip No Binary For Platform -- Fix Missing Platform Wheel"
description: "Fix pip no binary for platform errors when no binary wheel exists for your specific platform. Build from source."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip specifically searched for binary wheels and found none for your platform tag.

## Common Causes

- The package maintainer did not build wheels for your platform
- Your platform (e.g., musllinux, aarch64) is less common
- The package only supports specific platforms

## How to Fix

### 1. Allow Source Distributions

```bash
pip install <package>
```

### 2. Build from Source

```bash
pip install --no-binary=<package> <package>
```

### 3. Use Manylinux Wheels

```bash
pip install --platform manylinux2014_x86_64 --python-version 3.11 --only-binary=:all: <package>
```

### 4. Use conda

```bash
conda install <package>
```

## Examples

```bash
$ pip install --only-binary=:all: lxml
ERROR: No matching distribution found for lxml for platform linux-aarch64

$ pip install lxml
Building wheel for lxml (setup.py) ... done
```
