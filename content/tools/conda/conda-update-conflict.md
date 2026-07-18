---
title: "[Solution] Conda Package Update Causes Conflict Error — How to Fix"
description: "Fix conda package update conflicts when upgrading breaks existing dependencies. Resolve version constraints and use solver flags to update safely."
tools: ["conda"]
error-types: ["update-conflict"]
severities: ["error"]
weight: 5
comments: true
---

This error means conda cannot update a package because the new version conflicts with constraints from other installed packages. The solver cannot find a combination of versions that satisfies every requirement simultaneously.

## Why It Happens

- The package you are updating requires a different version of a dependency that is already pinned by another package
- Your environment has packages from multiple channels with incompatible version constraints
- You are trying to update a core package (like Python or NumPy) that many other packages depend on
- Packages installed via pip are not tracked by conda's solver and create hidden conflicts
- The channel you are using has a newer version that was not tested against your current environment

## Common Error Messages

```
UnsatisfiableError: The following specifications were found to be incompatible:
  - numpy[version='>=1.20,<1.22'] -> python[version='>=3.7,<3.10']
  - scikit-learn[version='>=1.0'] -> numpy[version='>=1.19.2'] -> python[version='>=3.7']
  conflict: python=3.11 is installed
```

```
ResolvePackageNotFound:
  - package-name=2.0.0
```

```
LibMambaUnsatisfiableError: Encountered problems while solving:
  - package-a >=1.0 requires package-b <2.0, but package-b 3.0 is installed
```

```
ConflictError: package-a and package-b both provide 'lib/something.so'
```

## How to Fix It

### 1. Update Multiple Packages Together

Instead of updating one package at a time, let conda resolve the entire tree:

```bash
conda update --all
```

This allows the solver to adjust multiple packages simultaneously to find a compatible set.

### 2. Use the Conda-Forge Channel

conda-forge often has newer, better-tested package combinations:

```bash
conda install -c conda-forge package-name
conda update -c conda-forge --all
```

### 3. Create a Fresh Environment

When conflicts are deeply tangled, a clean environment is the fastest fix:

```bash
conda create -n fresh-env python=3.11 numpy pandas scikit-learn
conda activate fresh-env
```

### 4. Downgrade the Conflicting Package

Find which package is causing the conflict and pin a compatible version:

```bash
conda search package-name --info
conda install package-name=1.5.0
```

### 5. Remove Pip-Installed Packages That Conflict

Packages installed via pip bypass conda's solver and cause hidden conflicts:

```bash
# List pip packages in the environment
conda run -n myenv pip list

# Remove problematic pip packages
conda run -n myenv pip uninstall conflicting-package

# Then reinstall via conda
conda install conflicting-package
```

### 6. Use the libmamba Solver

The libmamba solver is faster and sometimes resolves conflicts the classic solver cannot:

```bash
conda install -n base conda-libmamba-solver
conda config --set solver libmamba
conda update --all
```

## Common Scenarios

**Upgrading NumPy breaks scikit-learn.** scikit-learn has strict NumPy version requirements. Always update them together:

```bash
conda update numpy scikit-learn
```

**Mixing conda and pip causes silent conflicts.** A package installed via pip may depend on a different NumPy version than conda expects. Remove pip-installed packages and reinstall via conda.

**Channel mixing creates version mismatches.** Packages from `defaults` and `conda-forge` may have different version ranges. Stick to one channel or use conda-forge for everything:

```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
```

## Prevent It

1. Always use `conda update --all` instead of updating individual packages to let the solver find compatible versions
2. Set `channel_priority: strict` in your `.condarc` to prevent cross-channel version conflicts
3. Prefer `conda install` over `pip install` inside conda environments to keep the solver aware of all dependencies
