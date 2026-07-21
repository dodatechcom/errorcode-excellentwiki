---
title: "[Solution] pip Dep Missing Wheel -- Fix Dependency Without Wheel"
description: "Fix pip dependency missing wheel errors when a dependency of your package has no wheel available. Build from source or find alternatives."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means one of your package's dependencies does not have a pre-built wheel and source build failed.

## Common Causes

- The dependency is a C extension without pre-built wheels
- Build tools are missing on the system
- The dependency requires system libraries

## How to Fix

### 1. Install Build Dependencies

```bash
sudo apt install build-essential python3-dev libffi-dev
```

### 2. Install Dependencies Individually

```bash
pip install <dependency>  # Build from source
pip install <main-package>
```

### 3. Use a Different Index

```bash
pip install <package> --extra-index-url https://example.com/simple/
```

### 4. Use conda for Binary Packages

```bash
conda install <dependency>
pip install <package>
```

## Examples

```bash
$ pip install cryptography
ERROR: Could not build wheel for cffi

$ sudo apt install build-essential libffi-dev
$ pip install cryptography
Building wheel for cffi ... done
```
