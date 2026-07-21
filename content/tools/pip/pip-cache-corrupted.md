---
title: "[Solution] pip Cache Corrupted -- Fix Broken Download Cache"
description: "Fix pip cache corrupted errors when cached wheel or http files are damaged. Clear the cache and reinstall."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip's local cache contains corrupted files that prevent installation or extraction.

## Common Causes

- Interrupted download left partial files in cache
- Disk errors during cache write
- Cache directory permissions changed
- Another process modified cache files

## How to Fix

### 1. Clear All Cache

```bash
pip cache purge
```

### 2. Clear Cache for Specific Package

```bash
pip cache remove <package>
```

### 3. Ignore Cache During Install

```bash
pip install --no-cache-dir <package>
```

### 4. Clear and Reinstall

```bash
pip cache purge
pip install <package>
```

## Examples

```bash
$ pip install numpy
ERROR: Could not install packages due to an EnvironmentError: CRC check failed

$ pip cache purge
Files removed: 23

$ pip install numpy
Successfully installed numpy-1.24.0
```
