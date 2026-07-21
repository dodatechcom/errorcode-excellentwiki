---
title: "[Solution] Conda Install Timeout -- Fix Package Installation Timeout"
description: "Fix conda install timeout errors when package installation takes too long. Configure timeouts and use faster solvers."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means conda's install process timed out while downloading or extracting packages. The operation did not complete within the allowed time.

## Common Causes

- Large packages with many dependencies take a long time
- Slow network connection or high latency
- The solver is taking too long with complex dependency trees
- Download speeds are throttled by the mirror

## How to Fix

### 1. Use Libmamba Solver

```bash
conda install -n base -c conda-forge conda-libmamba-solver
conda config --set solver libmamba
```

### 2. Install Specific Packages Only

```bash
conda install package=1.0
```

### 3. Use Mamba Instead

```bash
conda install -n base -c conda-forge mamba
mamba install package
```

### 4. Increase Network Timeout

```bash
conda config --set remote_read_timeout_secs 600
```

## Examples

```bash
$ conda install numpy
Collecting package metadata: timeout after 300s

$ conda config --set solver libmamba
$ conda install numpy
Solving environment: done
```
