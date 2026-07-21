---
title: "[Solution] Conda Solve Unsolvable -- Fix Impossible Dependency Resolution"
description: "Fix conda solve unsolvable errors when no combination of packages satisfies all constraints. Simplify requirements."
tools: ["conda"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means conda determined that no combination of available package versions can satisfy all your constraints simultaneously.

## Common Causes

- You requested mutually exclusive packages
- Version constraints are too tight
- A required package does not exist on any configured channel
- Channel mixing creates incompatible combinations

## How to Fix

### 1. Relax Version Constraints

```bash
conda install numpy>=1.20
```

### 2. Create Separate Environments

```bash
conda create -n env-a package-a
conda create -n env-b package-b
```

### 3. Search for Alternatives

```bash
conda search package-name
```

### 4. Use conda-forge

```bash
conda install -c conda-forge package-name
```

## Examples

```bash
$ conda install package-a package-b
UnsatisfiableError: package-a and package-b are incompatible

$ conda create -n env-a package-a
$ conda create -n env-b package-b
```
