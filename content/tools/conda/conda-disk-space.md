---
title: "[Solution] Conda Disk Space Error - Fix No Space Left on Device"
description: "Fix conda 'no space left on device' errors by cleaning caches, unused environments, and packages to reclaim disk space efficiently."
tools: ["conda"]
error-types: ["disk-space"]
severities: ["error"]
weight: 5
---

This error means your filesystem has run out of available space while conda is trying to download, extract, or install packages. conda requires significant temporary and permanent storage for package caches and environments.

## What This Error Means

conda downloads compressed packages, extracts them into environments, and caches copies for future installs. When disk space is exhausted, operations fail with:

```
NoSpaceLeftError: OSError: [Errno 28] No space left on device
# or
CondaError: DiskError: ... No space left on device
```

Even if conda itself has space, the system may be unable to allocate temporary files during extraction. The package cache and environments directory can consume tens of gigabytes over time.

## Why It Happens

- Multiple conda environments accumulate over time without cleanup
- The package cache (`pkgs/`) stores every downloaded package version
- Large packages like PyTorch, CUDA toolkits, or TensorFlow consume several gigabytes each
- Temporary extraction during install doubles the space requirement momentarily
- Logs and other system files are consuming disk space independently
- A shared server has multiple users with overlapping environments

## How to Fix It

### Clean the package cache

```bash
conda clean --all
```

This removes unused packages, tarballs, source caches, and index caches. It is safe to run at any time.

### Remove unused environments

```bash
conda env list
conda env remove -n old-unused-env
```

Delete environments you no longer need to free several gigabytes at once.

### Check what is consuming space

```bash
du -sh $HOME/miniconda3/*
du -sh $HOME/.conda/*
```

This identifies the largest directories so you can target cleanup.

### Move the package cache to another drive

```bash
conda config --set pkgs_dirs /mnt/large-disk/conda-pkgs
```

If you have a larger secondary drive, relocate the cache there.

### Remove specific package versions

```bash
conda clean -p
```

This removes cached packages that are not currently linked to any environment.

### Monitor space during install

```bash
df -h .
conda install large-package
```

Check available space before installing large packages like deep learning frameworks.

## Common Mistakes

- Not running `conda clean` periodically, letting the cache grow to tens of gigabytes
- Creating duplicate environments for similar projects instead of reusing one
- Installing full Anaconda when Miniconda would suffice
- Forgetting that CUDA and GPU packages are extremely large
- Ignoring disk space warnings until a critical install fails mid-operation

## Related Pages

- [Conda Environment Error]({{< relref "/tools/conda/conda-environment-error" >}}) -- environment management
- [Conda Fetch Error]({{< relref "/tools/conda/conda-fetch-error" >}}) -- download failures
- [Conda Solver Error]({{< relref "/tools/conda/conda-solver-error" >}}) -- solver and dependency issues
