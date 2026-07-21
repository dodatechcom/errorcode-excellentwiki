---
title: "[Solution] pip Cache Space Exceeded -- Fix Disk Space in Cache"
description: "Fix pip cache space exceeded when pip cannot write to cache due to full disk. Clean cache or redirect to different location."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip ran out of disk space while trying to cache downloaded packages.

## Common Causes

- /tmp or cache directory is full
- Large packages consume cache quickly
- Cache was never cleaned

## How to Fix

### 1. Clean Cache

```bash
pip cache purge
```

### 2. Check Disk Space

```bash
df -h $(pip cache dir)
```

### 3. Redirect Cache

```bash
pip install --cache-dir /larger/partition/pip-cache <package>
```

### 4. Don't Cache

```bash
pip install --no-cache-dir <package>
```

## Examples

```bash
$ pip install tensorflow
ERROR: No space left on device

$ pip cache purge
Files removed: 847

$ pip install tensorflow
Downloading tensorflow-2.15.0...
```
