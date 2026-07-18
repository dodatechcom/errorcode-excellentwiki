---
title: "[Solution] Conda Package Specs Conflict Error — How to Fix"
description: "Fix conda package specs conflict errors. Resolve version constraint conflicts, dependency mismatches, and specification errors in conda environments."
tools: ["conda"]
error-types: ["specs-conflict"]
severities: ["error"]
weight: 5
comments: true
---

This error means the package specifications you provided contain conflicting constraints that the solver cannot satisfy simultaneously. Two or more packages require incompatible versions of the same dependency.

## Why It Happens

- You explicitly requested two packages that depend on different versions of a shared library
- A package has strict upper-bound constraints that block a newer version of another package
- You are mixing packages from different channels with incompatible version ranges
- The solver cannot find any combination of versions that satisfies all constraints at once
- A package requires a specific Python version that conflicts with another package's requirement
- You specified exact versions with `=` that are known to be incompatible

## Common Error Messages

```
UnsatisfiableError: The following specifications were found to be
incompatible with each other:
  - numpy=1.20 -> python[version='>=3.7,<3.10']
  - python=3.11
```

```
LibMambaUnsatisfiableError: Encountered problems while solving:
  - package-a >=1.0 requires package-b >=2.0,<3.0
  - package-c >=3.0 requires package-b >=3.0
```

```
ConflictError: package-a and package-b both pin
package-c to different incompatible versions.
```

```
SpecificationsMatchError: package-a and package-b have overlapping
but incompatible version constraints.
```

## How to Fix It

### 1. Identify the Conflicting Packages

```bash
conda install package-a package-b --dry-run
```

The dry run shows which packages conflict without making changes.

### 2. Relax Version Constraints

```bash
# Instead of pinning exact versions
conda install numpy=1.26.1 pandas=2.1.4

# Use flexible ranges
conda install "numpy>=1.24,<1.27" "pandas>=2.0,<3.0"
```

### 3. Update All Packages Together

```bash
conda update --all
```

The solver may find a newer combination where all constraints are satisfied.

### 4. Use conda-forge for Broader Compatibility

```bash
conda install -c conda-forge package-a package-b
```

conda-forge packages often have more relaxed constraints.

### 5. Split into Separate Environments

If two packages truly cannot coexist, use different environments:

```bash
# Environment for package-a
conda create -n env-a python=3.11 package-a

# Environment for package-b
conda create -n env-b python=3.11 package-b
```

### 6. Use the Verbose Solver to Pinpoint the Conflict

```bash
conda install package-a package-b -vvv
```

This shows the exact constraint that causes the failure.

### 7. Create a Minimal Reproducer

```bash
# Create a test environment
conda create -n test python=3.11
conda activate test

# Add packages one at a time
conda install package-a
conda install package-b  # This shows the conflict
```

## Common Scenarios

**NumPy version conflict between packages.** Package A requires NumPy <1.24 while Package B requires NumPy >=1.25. Upgrade both packages or find versions with overlapping NumPy constraints:

```bash
conda search -c conda-forge package-a --info
conda search -c conda-forge package-b --info
```

**Python version conflict.** One package requires Python 3.8 while another requires Python 3.11. You must use separate environments.

**Channel mixing causes version mismatches.** Packages from defaults and conda-forge may have different version ranges. Use strict channel priority:

```bash
conda config --set channel_priority strict
conda install -c conda-forge package-a package-b
```

## Prevent It

1. Always run `--dry-run` before installing multiple packages to preview potential conflicts
2. Use `conda search package-name --info` to check version constraints before installation
3. Stick to a single channel (preferably conda-forge with strict priority) to avoid cross-channel version conflicts
