---
title: "[Solution] pip Install Dry Run Error -- Fix --dry-run Not Supported"
description: "Fix pip install dry run error when using --dry-run with incompatible pip versions. Use alternative methods to preview installations."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `pip install --dry-run` is not supported in your pip version or is conflicting with other flags.

## Common Causes

- pip version is older than 22.2 (no --dry-run support)
- Using --dry-run with incompatible flags
- Python version is too old

## How to Fix

### 1. Upgrade pip

```bash
pip install --upgrade pip
```

### 2. Use --report Instead

```bash
pip install --dry-run --report - <package>
```

### 3. Use pipdeptree to Preview

```bash
pip install pipdeptree
pipdeptree --package <package>
```

### 4. Use --target for Preview

```bash
pip install --target /tmp/preview <package>
```

## Examples

```bash
$ pip install --dry-run numpy
ERROR: unknown option --dry-run

$ pip install --upgrade pip
$ pip install --dry-run numpy
Would install: numpy-1.24.0
```
