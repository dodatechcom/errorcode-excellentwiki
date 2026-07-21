---
title: "[Solution] Conda Solver Timeout -- Fix Dependency Resolution Timeout"
description: "Fix conda solver timeout errors when dependency resolution takes too long. Use faster solvers and simplify constraints."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the conda solver took too long to resolve dependencies and was terminated. Complex dependency trees can cause this.

## Common Causes

- Too many packages with complex constraints
- Using the classic solver instead of libmamba
- Channel mixing creates many conflict possibilities
- The solver is exploring an exponential search space

## How to Fix

### 1. Use Libmamba Solver

```bash
conda config --set solver libmamba
```

### 2. Install Fewer Packages at Once

```bash
conda install numpy pandas
```

### 3. Create a New Environment

```bash
conda create -n myenv python=3.11 numpy pandas
```

### 4. Pin Known-Compatible Versions

```bash
conda create -n myenv python=3.11 numpy=1.24 pandas=2.0
```

## Examples

```bash
$ conda install numpy pandas scipy scikit-learn matplotlib
Solving environment: killed after 300s

$ conda config --set solver libmamba
$ conda install numpy pandas scipy scikit-learn matplotlib
Solving environment: done (12.3s)
```
