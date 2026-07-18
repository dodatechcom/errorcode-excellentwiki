---
title: "[Solution] Conda Downgrade Error - Fix UnsatisfiableError Downgrade Conflict"
description: "Fix conda UnsatisfiableError when downgrading a package causes dependency conflicts. Resolve version constraints and environment mismatches."
tools: ["conda"]
error-types: ["downgrade-error"]
severities: ["error"]
weight: 5
---

This error means conda refuses to install a package because downgrading it would break other packages that depend on a newer version. The solver cannot find a solution where both the requested version and existing packages coexist.

## What This Error Means

When you ask conda to install a specific older version of a package, the solver checks whether that version is compatible with everything else in the environment. If not, you see:

```
UnsatisfiableError: The following specifications were found to be incompatible with the downgrade:
  - <package>=<old_version>
Conflicts:
  - other-package requires <package>>=<new_version>
```

The solver shows the chain of constraints preventing the downgrade. Unlike a fresh install conflict, this involves an existing environment where packages already depend on a specific version range.

## Why It Happens

- You requested an older version of a package that other installed packages require at a newer version
- A package was updated as a dependency of another package and cannot go back
- Two packages depend on the same library but at different minimum versions
- You are trying to match a version from production but your environment has moved ahead
- Channel metadata is stale and the solver has incorrect version information
- The downgrade would require a different Python version than what is currently active

## How to Fix It

### Create a separate environment

The safest approach is to start fresh:

```bash
conda create -n legacy python=3.10 <package>=<old_version>
```

This avoids conflicting with your existing environment.

### Remove conflicting packages first

```bash
conda remove other-package
conda install <package>=<old_version>
```

Check what depends on the newer version before removing:

```bash
conda list --show-channel-urls | grep <package>
```

### Use the conda-libmamba-solver

The libmamba solver gives clearer error messages and sometimes finds solutions the classic solver misses:

```bash
conda install -n base -c conda-forge conda-libmamba-solver
conda config --set solver libmamba
```

### Allow conda to downgrade all dependent packages

```bash
conda install <package>=<old_version> --update-deps
```

This lets conda downgrade everything required, but may break other functionality.

### Pin versions in environment YAML

```yaml
name: myenv
dependencies:
  - python=3.10
  - <package>=<old_version>
  - <package2>==2.1.0
```

Specifying the full set avoids solver surprises.

## Common Mistakes

- Running `conda update --all` before checking version compatibility
- Assuming conda will automatically downgrade dependencies to satisfy a request
- Not creating separate environments for different project version requirements
- Using `--force` or `--no-deps` which installs broken states
- Forgetting that pinned versions in environment files override solver suggestions

## Related Pages

- [Conda Solver Error]({{< relref "/tools/conda/conda-solver-error" >}}) -- general solver conflicts
- [Conda Conflict Error]({{< relref "/tools/conda/conda-conflict-error" >}}) -- dependency conflict details
- [Conda Environment Error]({{< relref "/tools/conda/conda-environment-error" >}}) -- environment creation issues
