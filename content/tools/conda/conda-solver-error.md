---
title: "[Solution] Conda SolverError — Fix UnsatisfiableError Package Conflicts"
description: "Fix conda UnsatisfiableError when the solver cannot find compatible package versions. Use mamba and configure channels to resolve dependency failures."
tools: ["conda"]
error-types: ["solver-error"]
severities: ["error"]
weight: 5
---

This error means conda's dependency solver could not find a combination of package versions that satisfies all constraints simultaneously. conda refuses to proceed with the install or update.

## What This Error Means

conda uses a SAT-based solver to resolve package dependencies across channels. When every candidate solution violates at least one constraint, the solver reports:

```
UnsatisfiableError

The following specifications were found to be incompatible with the existing installation:
  - <package>
```

The error traces the conflicting packages and the version ranges that clash.

## Why It Happens

- Two packages you requested require different versions of a shared dependency
- A package exists on one channel but not another, and the versions conflict across channels
- You are mixing packages from `defaults` and `conda-forge` that were built against different ABI versions
- The package requires a different Python version than what is installed in the environment
- A package was recently removed from a channel and the solver has a stale cache

## How to Fix It

### Use Mamba for Faster Resolution

mamba is a drop-in replacement with a faster solver:

```bash
conda install -n base -c conda-forge mamba
mamba install <package>
```

### Switch to conda-libmamba-solver

If you want to keep conda without installing mamba:

```bash
conda install -n base -c conda-forge conda-libmamba-solver
conda config --set solver libmamba
conda install <package>
```

### Isolate Packages into Separate Environments

```bash
conda create -n env-a python=3.11 package-a
conda create -n env-b python=3.11 package-b
```

Installing conflicting packages into separate environments avoids the solver entirely.

### Pin Compatible Versions

```bash
conda install package-a=2.1 package-b=3.0
```

Providing explicit versions helps the solver narrow down the solution space.

### Clear the Solver Cache

```bash
conda clean --all
conda install <package>
```

### Use Only One Channel

Mixing channels is the most common cause:

```bash
conda config --show channels
conda config --set channel_priority strict
conda install -c conda-forge <package>
```

## Common Mistakes

- Mixing `defaults` and `conda-forge` channels without setting `channel_priority strict`
- Not using `libmamba` solver, which handles complex dependency trees much better
- Installing dozens of packages in one command when some are known to conflict
- Forgetting that `conda update --all` can break existing environments

## Related Pages

- [Conda Conflict Error]({{< relref "/tools/conda/conda-conflict-error" >}}) -- dependency conflicts
- [Conda Channel Error]({{< relref "/tools/conda/conda-channel-error" >}}) -- channel and package lookup errors
- [Conda Environment Error]({{< relref "/tools/conda/conda-environment-error" >}}) -- environment issues
