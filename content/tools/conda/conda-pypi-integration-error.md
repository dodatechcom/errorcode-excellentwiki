---
title: "[Solution] Conda PyPI Integration Error -- Fix pip-in-conda Issues"
description: "Fix conda PyPI integration errors when mixing pip and conda packages. Manage the interaction between package managers correctly."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means conda detected an inconsistency caused by mixing pip and conda package installations. The two managers tracked different states.

## Common Causes

- Installing with pip after conda in the same environment
- Using `pip install --upgrade` on a conda-managed package
- conda cannot see pip-installed packages in its solver
- pip overwrote conda-managed files

## How to Fix

### 1. Prefer conda Over pip

```bash
conda install package-name
# Only use pip for packages not on conda
```

### 2. Install pip Packages Last

```bash
conda install numpy pandas
pip install custom-package
```

### 3. Use conda-forge for More Packages

```bash
conda install -c conda-forge package-name
```

### 4. Create Separate Environments

```bash
conda create -n conda-env python=3.11 numpy
conda create -n pip-env python=3.11
conda activate pip-env
pip install custom-package
```

## Examples

```bash
$ conda install numpy
$ pip install numpy  # Warning: conda pip interaction
$ conda list numpy
# numpy may show conflicting versions
```
