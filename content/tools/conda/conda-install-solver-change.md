---
title: "[Solution] Conda Install Solver Change -- Fix Switching Solvers Mid-Operation"
description: "Fix conda install solver change errors when switching solvers during an operation causes failures. Complete operations with one solver."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means changing the solver configuration mid-operation caused conda to fail. The operation started with one solver and finished with another.

## Common Causes

- Changed solver config while an install was running
- Multiple terminals with different solver settings
- Environment variable override conflicted with config

## How to Fix

### 1. Complete Current Operation First

```bash
# Let current operation finish
conda install package-name
# Then switch solver
conda config --set solver libmamba
```

### 2. Set Solver Before Operations

```bash
conda config --set solver libmamba
conda install package-name
```

### 3. Use Environment Variable

```bash
CONDA_SOLVER=libmamba conda install package-name
```

### 4. Reset Solver Config

```bash
conda config --remove-key solver
```

## Examples

```bash
$ conda install numpy &
$ conda config --set solver libmamba
# Conflict: solver changed during operation

# Fix: let install finish first
$ conda install numpy
$ conda config --set solver libmamba
$ conda install pandas  # Now uses libmamba
```
