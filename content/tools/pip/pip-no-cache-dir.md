---
title: "[Solution] pip No Cache Dir -- Fix Cache Directory Issues"
description: "Fix pip no cache dir errors when pip cannot write to its cache directory. Fix permissions or use temporary directory."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip cannot write to its cache directory due to permission issues or disk space problems.

## Common Causes

- Cache directory permissions are restrictive
- Disk is full
- Cache directory was manually deleted
- Another user owns the cache directory

## How to Fix

### 1. Check Cache Location

```bash
pip cache dir
```

### 2. Fix Permissions

```bash
sudo chown -R $(whoami) $(pip cache dir)
```

### 3. Use --no-cache-dir

```bash
pip install --no-cache-dir <package>
```

### 4. Set Custom Cache Directory

```bash
pip install --cache-dir /tmp/pip-cache <package>
```

## Examples

```bash
$ pip install numpy
ERROR: Could not install packages: Permission denied: '/home/user/.cache/pip'

$ pip install --no-cache-dir numpy
Successfully installed numpy-1.24.0
```
