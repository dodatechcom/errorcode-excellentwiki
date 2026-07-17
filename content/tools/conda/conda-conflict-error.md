---
title: "[Solution] Conda Conflict Error — Fix Dependency Conflicts Between Packages"
description: "Fix conda dependency conflicts when packages require incompatible versions of shared libraries. Use strict channel priority and separate environments to fix."
tools: ["conda"]
error-types: ["conflict-error"]
severities: ["error"]
weight: 5
---

This error means two installed or requested packages depend on different versions of the same shared library. conda detects the conflict and blocks the operation to prevent a broken environment.

## What This Error Means

Unlike an `UnsatisfiableError` (which means no solution exists at all), a conflict error means conda found a partially valid solution but two packages cannot coexist:

```
LibMambaUnsatisfiableError

Encountered problems while solving:
  - package-a requires package-c >=2.0, but package-b requires package-c <2.0
```

The error specifically names the two packages and the version ranges that clash.

## Why It Happens

- You installed packages from different channels that were built against different library versions
- A package update introduced a new, incompatible dependency constraint
- You are mixing conda-installed packages with pip-installed packages that share a dependency
- The solver picked a version of one package that conflicts with a pinned version of another

## How to Fix It

### Pin Compatible Versions Explicitly

```bash
conda install package-a=2.1 package-b=3.0
```

Finding two versions that both use the same library version often resolves the conflict.

### Create Separate Environments

```bash
conda create -n project-a package-a python=3.11
conda create -n project-b package-b python=3.11
```

Isolating conflicting packages into different environments is the cleanest solution.

### Use conda-forge Exclusively

Mixing channels is the most common source of conflicts:

```bash
conda config --remove channels defaults
conda config --add channels conda-forge
conda config --set channel_priority strict
conda install package-a package-b
```

### Allow Downgrades

```bash
conda install package-a package-b --update-deps --force-reinstall
```

This lets conda downgrade a package if needed to find a compatible set.

### Check What Is Already Installed

```bash
conda list | grep <library-name>
```

If the library is at a version that conflicts with the new package, you may need to update or remove existing packages first.

### Use pip Only as a Last Resort

```bash
# Install most packages via conda
conda install package-a

# Then install the remaining package via pip in the same environment
pip install package-b
```

Mixing conda and pip can work but makes the environment harder to manage.

## Common Mistakes

- Not setting `channel_priority strict`, which lets the solver mix channels freely
- Installing 20 packages at once when you only need to add one more
- Not using separate environments for unrelated projects
- Running `conda update --all` on a production environment without testing first

## Related Pages

- [Conda Solver Error]({{< relref "/tools/conda/conda-solver-error" >}}) -- unsatisfiable error
- [Conda Channel Error]({{< relref "/tools/conda/conda-channel-error" >}}) -- channel issues
- [Conda Update Error]({{< relref "/tools/conda/conda-update-error" >}}) -- update failures
