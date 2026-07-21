---
title: "[Solution] pip Hash Mismatch Wheel -- Fix Wheel Integrity Check"
description: "Fix pip hash mismatch wheel errors when downloaded wheel file hash does not match expected value. Clear cache and re-download."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the downloaded wheel file's hash does not match the hash recorded in the package index. pip refuses to install potentially tampered files.

## Common Causes

- Corrupted download due to network issues
- Mirror server is serving modified packages
- Cache contains partial downloads
- Package was re-released with same version

## How to Fix

### 1. Clear pip Cache

```bash
pip cache purge
```

### 2. Re-download Without Cache

```bash
pip install --no-cache-dir <package>
```

### 3. Use Official PyPI

```bash
pip install <package> -i https://pypi.org/simple/
```

### 4. Verify Download Manually

```bash
pip download <package> -d ./downloads
sha256sum ./downloads/*.whl
```

## Examples

```bash
$ pip install numpy
HashMismatchError: hash mismatch for numpy-1.24.0-cp311-cp311-linux_x86_64.whl

$ pip cache purge
$ pip install --no-cache-dir numpy
Successfully installed numpy-1.24.0
```
