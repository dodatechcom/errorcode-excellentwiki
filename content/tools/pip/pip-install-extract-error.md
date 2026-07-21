---
title: "[Solution] pip Install Extract Error -- Fix Wheel Extraction Failure"
description: "Fix pip install extract error when pip cannot extract a downloaded wheel or sdist file. Clear cache and re-download."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip downloaded a package file but could not extract its contents. The file may be corrupted.

## Common Causes

- Corrupted download
- Incomplete download due to network issue
- Disk error during extraction
- The file is not a valid archive

## How to Fix

### 1. Clear Cache and Re-download

```bash
pip cache purge
pip install --no-cache-dir <package>
```

### 2. Verify File Integrity

```bash
pip download <package> -d /tmp
file /tmp/<package>*.whl
```

### 3. Download Manually

```bash
wget https://files.pythonhosted.org/packages/.../package.whl
pip install /tmp/package.whl
```

### 4. Check Disk Space

```bash
df -h /tmp
```

## Examples

```bash
$ pip install numpy
ERROR: Could not install packages: Unexpected EOF while reading

$ pip cache purge
$ pip install --no-cache-dir numpy
Successfully installed numpy-1.24.0
```
