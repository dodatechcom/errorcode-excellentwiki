---
title: "[Solution] pip Install Platform Error -- Fix Cross-Platform Install"
description: "Fix pip install platform error when --platform flag specifies incompatible platform tags. Use correct platform identifiers."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the --platform flag value does not match any known platform tags. pip cannot find compatible distributions.

## Common Causes

- Wrong platform tag format
- Using Linux platform tag on macOS
- Platform tag is misspelled
- Python version mismatch

## How to Fix

### 1. Check Available Platform Tags

```bash
pip debug --verbose 2>&1 | grep "Compatible tags"
```

### 2. Use Correct Tags

```bash
pip install --platform manylinux2014_x86_64 --python-version 3.11 <package>
```

### 3. Common Platform Tags

```bash
# Linux x86_64
manylinux2014_x86_64

# macOS ARM64
macosx_11_0_arm64

# Windows
win_amd64
```

### 4. Let pip Auto-Detect

```bash
pip install <package>  # without --platform
```

## Examples

```bash
$ pip install --platform linux_x86_64 --python-version 3.11 requests
ERROR: 'linux_x86_64' is not a supported platform

$ pip install --platform manylinux2014_x86_64 --python-version 3.11 requests
Successfully installed requests-2.31.0
```
