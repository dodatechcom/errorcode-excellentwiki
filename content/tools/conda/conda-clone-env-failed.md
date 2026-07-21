---
title: "[Solution] Conda Clone Env Failed -- Fix Environment Cloning Failure"
description: "Fix conda clone env failed errors when creating a copy of an existing environment fails. Export and recreate instead."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `conda create --clone` failed to create an exact copy of an existing environment.

## Common Causes

- Source environment is corrupted
- Disk space is insufficient
- Permission issues prevent copying
- Source environment has broken symlinks

## How to Fix

### 1. Export and Recreate

```bash
conda env export -n source-env > environment.yml
conda env create -n target-env -f environment.yml
```

### 2. Check Disk Space

```bash
df -h $(conda info --base)/envs/
```

### 3. Fix Permissions

```bash
chmod -R u+w $(conda info --base)/envs/source-env
```

### 4. Remove Broken Symlinks

```bash
find $(conda info --base)/envs/source-env -xtype l -delete
```

## Examples

```bash
$ conda create --clone source-env -n target-env
CondaError: Cannot clone into target directory

$ conda env export -n source-env > environment.yml
$ conda env create -n target-env -f environment.yml
```
