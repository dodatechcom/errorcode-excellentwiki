---
title: "[Solution] pip Download No Mirror -- Fix Missing Mirror Configuration"
description: "Fix pip download no mirror error when the configured mirror does not have the requested package. Check mirror sync status."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the package was not found on the configured mirror. The mirror may be out of sync with PyPI.

## Common Causes

- Mirror has not synced recently
- The package was just released and mirror lag
- Mirror only syncs specific packages
- The mirror URL is wrong

## How to Fix

### 1. Use Official PyPI

```bash
pip download <package> -i https://pypi.org/simple/
```

### 2. Check Mirror Status

```bash
curl https://mirror.example.com/simple/<package>/
```

### 3. Add Official PyPI as Fallback

```bash
pip download <package> --extra-index-url https://pypi.org/simple/
```

### 4. Use a Different Mirror

```bash
pip download <package> -i https://mirrors.aliyun.com/pypi/simple/
```

## Examples

```bash
$ pip download numpy -i https://mirror.example.com/simple/
ERROR: No matching distribution found for numpy

$ pip download numpy -i https://pypi.org/simple/
Downloading numpy-1.24.0-cp311-cp311-manylinux.whl
```
