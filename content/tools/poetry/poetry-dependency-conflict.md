---
title: "[Solution] Poetry SolverProblemError — Fix Dependency Resolution Conflicts"
description: "Fix Poetry SolverProblemError when Poetry cannot resolve conflicting package dependencies. Learn to relax constraints and update the lock file correctly."
tools: ["poetry"]
error-types: ["dependency-error"]
severities: ["error"]
weight: 5
---

This error means Poetry's dependency resolver found a set of requirements that cannot all be satisfied simultaneously. Poetry refuses to install or update until the conflict is resolved.

## What This Error Means

Poetry uses a SAT-solver-based resolver (PyInstaller) to find a consistent set of package versions. When it exhausts all combinations and still finds conflicts, it raises `SolverProblemError`. The output looks like:

```
SolverProblemError

Because myproject depends on requests (^2.28) and httpx (^0.24) depends on httpcore (>=1.0.0,<2.0.0),
  version solving failed.
```

The error traces the full chain of constraints that led to the conflict.

## Why It Happens

- Two top-level dependencies in `pyproject.toml` require incompatible ranges of a shared sub-dependency
- A newly released version of a dependency tightened its own requirements
- You specified a very narrow version range that leaves no room for other packages
- A transitive dependency was removed from PyPI
- You are mixing PyPI packages with git dependencies that pin conflicting versions

## How to Fix It

### Read the Conflict Chain Carefully

Poetry names every package in the chain. Identify the two branches that create the conflict.

### Relax Version Constraints

Edit `pyproject.toml` and widen the range:

```
[tool.poetry.dependencies]
requests = "^2.28"
httpx = "^0.23"
```

Changing `httpx` from `^0.24` to `^0.23` may resolve the conflict.

### Update All Dependencies

```bash
poetry update
```

A full update often pulls in newer versions that are mutually compatible.

### Use `--dry-run` to Preview Changes

```bash
poetry lock --dry-run
```

This shows what Poetry would change without writing `poetry.lock`.

### Override a Transitive Dependency

If one specific sub-dependency is the problem, override it in `pyproject.toml`:

```toml
[tool.poetry.dependencies]
requests = "^2.28"

[tool.poetry.source]
name = "pypi"
url = "https://pypi.org/simple/"
```

Or use `poetry add` to force a specific version:

```bash
poetry add requests@^2.28 httpx@^0.23
```

### Check for Conflicting Sources

Make sure you do not have multiple `[[tool.poetry.source]]` entries pointing to different indexes that host different versions of the same package.

## Common Mistakes

- Ignoring the full error trace and guessing which package to update
- Forcing a lock with `--no-update` which can leave `poetry.lock` inconsistent
- Adding `--no-interaction` in CI which hides the interactive conflict resolution prompt
- Not regenerating the lock file after changing `pyproject.toml`

## Related Pages

- [Poetry Lock Error]({{< relref "/tools/poetry/poetry-lock-error" >}}) -- lock file inconsistency
- [Poetry Install Error]({{< relref "/tools/poetry/poetry-install-error" >}}) -- install failures
- [Poetry Package Not Found]({{< relref "/tools/poetry/poetry-package-not-found" >}}) -- missing packages
