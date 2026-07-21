---
title: "[Solution] Conda Remove Not Installed -- Fix Removing Non-Existent Package"
description: "Fix conda remove not installed errors when trying to remove a package that is not in the environment. Verify the package is installed."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `conda remove` was called with a package name that does not exist in the current environment.

## Common Causes

- The package was already removed
- The package name is misspelled
- You are in the wrong environment
- The package was installed with pip, not conda

## How to Fix

### 1. Check Installed Packages

```bash
conda list | grep package-name
```

### 2. Verify Environment

```bash
conda info --envs
conda activate correct-env
```

### 3. Remove pip-installed Packages with pip

```bash
pip uninstall package-name
```

### 4. Use the Correct Package Name

```bash
conda search package-name
```

## Examples

```bash
$ conda remove numpy
PackageNotFoundError: Package not found: 'numpy'

$ conda list | grep numpy
# (empty -- numpy was installed with pip)

$ pip uninstall numpy
```
