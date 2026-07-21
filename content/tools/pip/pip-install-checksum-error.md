---
title: "[Solution] pip Install Checksum Error -- Fix Package Checksum Verification"
description: "Fix pip install checksum error when downloaded package fails hash verification. Clear cache and use official PyPI."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the checksum of the downloaded package does not match the expected value from the package index.

## Common Causes

- Corrupted download
- Mirror serving modified packages
- Network issues during download
- Package was re-released

## How to Fix

### 1. Clear Cache

```bash
pip cache purge
```

### 2. Download Without Cache

```bash
pip install --no-cache-dir <package>
```

### 3. Use Official PyPI

```bash
pip install <package> -i https://pypi.org/simple/
```

### 4. Verify Manually

```bash
pip download <package> -d /tmp
sha256sum /tmp/<package>*.whl
```

## Examples

```bash
$ pip install numpy
HashMismatchError: hash mismatch for numpy-1.24.0.whl

$ pip cache purge
$ pip install --no-cache-dir numpy
Successfully installed numpy-1.24.0
```
