---
title: "[Solution] Conda Env Creation Failed -- Fix Environment Setup Failure"
description: "Fix conda env creation failed errors when creating a new conda environment fails. Debug the creation process and resolve dependencies."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `conda create` failed to build the new environment. The creation process was interrupted or hit an error.

## Common Causes

- Dependency conflicts prevent environment creation
- Disk space is insufficient
- The solver crashed or timed out
- Network issues prevented downloading packages

## How to Fix

### 1. Create with Fewer Packages

```bash
conda create -n myenv python=3.11
conda activate myenv
conda install numpy pandas
```

### 2. Use Verbose Output

```bash
conda create -n myenv python=3.11 -v
```

### 3. Use Mamba

```bash
mamba create -n myenv python=3.11 numpy pandas
```

### 4. Check Disk Space

```bash
df -h $(conda info --base)/envs/
```

## Examples

```bash
$ conda create -n myenv python=3.11 numpy pandas scipy
Collecting package metadata: done
Solving environment: failed
UnsatisfiableError: numpy and scipy have incompatible versions

$ conda create -n myenv python=3.11
$ conda activate myenv
$ conda install numpy pandas scipy
```
