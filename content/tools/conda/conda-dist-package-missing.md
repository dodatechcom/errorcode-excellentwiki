---
title: "[Solution] Conda Dist Package Missing -- Fix Missing Distribution Package"
description: "Fix conda dist package missing errors when a package distribution file is missing from the cache. Redownload and reinstall."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means conda found a reference to a package in the cache index but the actual distribution file is missing.

## Common Causes

- Partial cache cleanup removed distribution files
- Interrupted download left incomplete files
- Cache index is stale compared to file system
- Disk corruption affected the cache

## How to Fix

### 1. Clean and Refresh Cache

```bash
conda clean --all
```

### 2. Reinstall the Package

```bash
conda install --force-reinstall <package>
```

### 3. Remove Index Cache Only

```bash
conda clean --index-cache
```

### 4. Rebuild Package Cache

```bash
conda install -n base conda-build
```

## Examples

```bash
$ conda install numpy
CondaError: Package not found in cache: numpy-1.24.0-py311h1234_0.tar.bz2

$ conda clean --all
$ conda install numpy
Solving environment: done
```
