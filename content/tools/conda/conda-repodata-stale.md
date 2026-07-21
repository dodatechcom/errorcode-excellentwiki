---
title: "[Solution] Conda Repodata Stale -- Fix Outdated Channel Data"
description: "Fix conda repodata stale errors when channel metadata is outdated. Update channel indices to get current package information."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means conda is using outdated channel metadata that does not reflect the current state of packages. Installs may fail or install wrong versions.

## Common Causes

- `conda update` was not run recently
- Channel metadata cache is old
- The mirror is not syncing frequently
- Internet was disconnected during previous operations

## How to Fix

### 1. Update All Channels

```bash
conda update conda
conda clean --all
```

### 2. Force Refresh

```bash
conda search --channel conda-forge numpy
```

### 3. Remove Stale Cache

```bash
conda clean --index-cache
```

### 4. Set Auto-Update Frequency

```bash
conda config --set auto_update_conda false
```

## Examples

```bash
$ conda install numpy=1.25
PackageNotFoundError: numpy 1.25 not found

$ conda clean --all
$ conda update conda
$ conda install numpy=1.25
Solving environment: done
```
