---
title: "[Solution] Conda Package Integrity Error -- Fix Package Hash Mismatch"
description: "Fix conda package integrity error when downloaded package hashes do not match expected values. Clear cache and re-download packages."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means conda detected a hash mismatch when verifying a downloaded package. The file may be corrupted or tampered with.

## Common Causes

- Corrupted download due to network issues
- Package cache contains partial files
- Mirror server is serving corrupted packages
- Disk corruption affected cached files

## How to Fix

### 1. Clear the Package Cache

```bash
conda clean --all
```

### 2. Reinstall the Package

```bash
conda install --force-reinstall <package>
```

### 3. Use a Different Mirror

```bash
conda config --set default_channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
```

### 4. Verify Package Integrity Manually

```bash
conda install --verify <package>
```

## Examples

```bash
$ conda install numpy
CondaError: Hash mismatch for package numpy-1.24.0

$ conda clean --all
$ conda install numpy
Solving environment: done
```
