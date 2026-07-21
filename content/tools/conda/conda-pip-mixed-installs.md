---
title: "[Solution] Conda Pip Mixed Installs -- Fix Mixed Package Manager State"
description: "Fix conda pip mixed installs errors when mixing conda and pip creates inconsistent environments. Use one primary package manager."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the environment has inconsistent package metadata because conda and pip were used to install overlapping packages.

## Common Causes

- pip installed over a conda-managed package
- Both managers track different file lists
- Upgrading with pip broke conda's solver state
- conda cannot uninstall pip-installed packages cleanly

## How to Fix

### 1. Identify pip-Installed Packages

```bash
pip list --not-required
```

### 2. Remove pip Packages

```bash
pip uninstall conflicting-package
conda install conflicting-package
```

### 3. Use conda-forge for Everything

```bash
conda install -c conda-forge package-name
```

### 4. Create Separate Environments

```bash
conda create -n conda-only python=3.11 numpy pandas
conda create -n pip-only python=3.11
pip install custom-package
```

## Examples

```bash
$ conda list numpy
numpy     1.24.0    pypi_0    pypi  # Installed by pip over conda

# Fix:
$ pip uninstall numpy
$ conda install numpy
$ conda list numpy
numpy     1.24.0    py311h1234_0    conda-forge
```
