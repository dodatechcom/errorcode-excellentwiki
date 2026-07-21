---
title: "[Solution] Conda Package Downgrade Failed -- Fix Downgrade Errors"
description: "Fix conda package downgrade failed errors when downgrading a package version conflicts with dependencies. Handle version changes carefully."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means conda cannot downgrade a package because other installed packages depend on a higher version.

## Common Causes

- A dependency requires a minimum version higher than the downgrade target
- Other packages in the environment conflict with the downgrade
- The downgrade would break ABI compatibility

## How to Fix

### 1. Check Dependencies

```bash
conda list --show-channel-urls package-name
```

### 2. Downgrade All Related Packages

```bash
conda install package=old-version dependency=compatible-version
```

### 3. Create a New Environment

```bash
conda create -n old-env python=3.9 package=old-version
```

### 4. Remove Conflicting Packages First

```bash
conda remove conflicting-package
conda install package=old-version
```

## Examples

```bash
$ conda install numpy=1.22
UnsatisfiableError: numpy 1.22 is incompatible with scipy>=1.8

$ conda install numpy=1.22 scipy=1.7
Solving environment: done
```
