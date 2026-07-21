---
title: "[Solution] Conda Env Duplicate Name -- Fix Multiple Environments Same Name"
description: "Fix conda env duplicate name errors when multiple environments share the same name in different locations. Manage environment names and prefixes."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means conda found multiple environments with the same name, causing ambiguity in activation and management.

## Common Causes

- An environment was created with both `--name` and `--prefix`
- A manual copy of the environment directory was created
- The envs directory contains duplicates from different sources

## How to Fix

### 1. List All Environments

```bash
conda env list
```

### 2. Remove the Duplicate

```bash
conda env remove -n duplicate-env --all
```

### 3. Rename Using a Different Name

```bash
conda create --name new-env-name --clone old-env
conda env remove -n old-env
```

### 4. Use Prefixes Instead

```bash
conda create --prefix /path/to/env python=3.11
```

## Examples

```bash
$ conda env list
# conda environments:
base                  /home/user/miniconda3
myenv                 /home/user/miniconda3/envs/myenv
myenv                 /home/user/shared/envs/myenv  # duplicate!

$ conda env remove -n myenv --all
```
