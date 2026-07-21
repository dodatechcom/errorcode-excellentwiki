---
title: "[Solution] pip Install Source Only -- Fix Source Distribution Build"
description: "Fix pip install source only errors when only source distributions are available and build fails. Install build tools or find wheels."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip tried to install a package but only source distributions were available, and the build failed.

## Common Causes

- No pre-built wheel for your platform/Python
- C compiler or headers are missing
- Build dependencies are not installed

## How to Fix

### 1. Install Build Tools

```bash
sudo apt install build-essential python3-dev
```

### 2. Use a Pre-built Wheel if Available

```bash
pip install --only-binary=:all: <package>
```

### 3. Use a Binary Distribution Channel

```bash
pip install <package> --extra-index-url https://example.com/simple/
```

### 4. Install from Conda Instead

```bash
conda install <package>
```

## Examples

```bash
$ pip install lxml
Building wheel for lxml (setup.py) ... error
error: command 'gcc' failed

$ sudo apt install build-essential python3-dev
$ pip install lxml
Building wheel for lxml (setup.py) ... done
```
