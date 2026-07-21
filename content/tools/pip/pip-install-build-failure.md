---
title: "[Solution] pip Install Build Failure -- Fix Package Build Error"
description: "Fix pip install build failure errors when building a package from source fails during setup. Install required build dependencies."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip failed to build a package from source during installation. The build process returned an error.

## Common Causes

- Missing C compiler or build tools
- Required system libraries are not installed
- setup.py has configuration errors
- The package requires a specific build environment

## How to Fix

### 1. Install Build Essentials

```bash
sudo apt install build-essential python3-dev
```

### 2. Check Build Logs

```bash
pip install --verbose <package> 2>&1 | tail -100
```

### 3. Install Pre-built Wheel

```bash
pip install --only-binary=:all: <package>
```

### 4. Use conda for Compiled Packages

```bash
conda install <package>
```

## Examples

```bash
$ pip install numpy
error: command 'gcc' failed: exit status 1

$ sudo apt install build-essential python3-dev
$ pip install numpy
Successfully built numpy
```
