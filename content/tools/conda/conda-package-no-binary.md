---
title: "[Solution] Conda Package No Binary -- Fix Missing Binary Distribution"
description: "Fix conda package no binary available errors when no pre-built binary exists for your platform. Build from source or use alternative channels."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means conda cannot find a pre-built binary package for your platform and Python version. A source build may be required.

## Common Causes

- The package was not built for your platform (e.g., ARM)
- The package requires a different Python version
- No conda package exists, only on PyPI
- The package is very new and not yet built

## How to Fix

### 1. Use pip Instead

```bash
pip install package-name
```

### 2. Try a Different Python Version

```bash
conda install python=3.10
conda install package-name
```

### 3. Build from Source

```bash
conda install -c conda-forge conda-build
conda build recipe/
```

### 4. Use a Different Channel

```bash
conda install -c bioconda package-name
```

## Examples

```bash
$ conda install package-name
UnsatisfiableError: no viable package for package-name on linux-64

$ pip install package-name
Successfully installed package-name-1.0
```
