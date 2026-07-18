---
title: "[Solution] Poetry Development Dependency Install Failed Error — How to Fix"
description: "Fix Poetry dev dependency install failures. Resolve group installation errors, extras conflicts, and optional dependency issues in Poetry projects."
tools: ["poetry"]
error-types: ["install-dev-error"]
severities: ["error"]
weight: 5
comments: true
---

This error means Poetry failed to install development dependencies. The solver could not resolve the dependency tree for dev packages, or the installation of dev-only packages encountered an error.

## Why It Happens

- Development dependencies conflict with main dependencies in version requirements
- A dev dependency requires a Python version not available in the current environment
- The `--with` flag references a dependency group that does not exist in `pyproject.toml`
- Dev dependencies were removed from `pyproject.toml` but `poetry.lock` still references them
- Network issues prevent downloading dev dependency packages
- A dev dependency requires system libraries that are not installed

## Common Error Messages

```
InstallationError

Could not install packages due to an EnvironmentError:
401 Unauthorized for url: https://pypi.org/simple/package-name/
```

```
SolverProblemError

Because package-a (1.0.0) requires package-b (>=2.0,<3.0)
and package-c (3.0.0) requires package-b (>=3.0),
package-a (1.0.0) cannot be installed.
```

```
ValueError

Group "dev" does not exist in pyproject.toml.
```

```
PackageNotFound

Package "test-package" not found in lock file.
```

## How to Fix It

### 1. Install Dev Dependencies Explicitly

```bash
poetry install --with dev
```

If you use a custom group name:

```bash
poetry install --with dev,test,lint
```

### 2. Check Available Dependency Groups

```bash
# View all dependency groups in pyproject.toml
cat pyproject.toml | grep -A 20 "\[tool.poetry.group"
```

### 3. Regenerate the Lock File

```bash
poetry lock
poetry install --with dev
```

If dev dependencies were recently added or changed, the lock file may be stale.

### 4. Remove and Re-add the Dev Dependency

```bash
poetry remove --group dev package-name
poetry add --group dev package-name
```

### 5. Install Without Dev Dependencies First

```bash
poetry install --without dev
poetry install --with dev
```

Installing the base packages first can help the solver find a valid solution.

### 6. Check Python Version Compatibility

```bash
poetry env info
```

Ensure the Python version matches the dev dependency requirements.

### 7. Use `--sync` to Clean Up

```bash
poetry install --sync --with dev
```

The `--sync` flag removes packages not listed in `poetry.lock`, ensuring a clean install.

## Common Scenarios

**Dev dependencies conflict with production dependencies.** Check for version overlap:

```bash
poetry show --tree
```

If a dev dependency requires a different version of a shared package, update both to compatible versions or find alternative packages.

**Custom dependency groups not found.** Ensure the group is defined in `pyproject.toml`:

```toml
[tool.poetry.group.testing]
optional = true

[tool.poetry.group.testing.dependencies]
pytest = ">=7.0"
```

**Private PyPI packages fail during dev install.** Configure the repository in `pyproject.toml`:

```toml
[[tool.poetry.source]]
name = "private-pypi"
url = "https://pypi.company.com/simple/"
priority = "supplemental"
```

## Prevent It

1. Run `poetry lock` after adding or removing dev dependencies to keep the lock file in sync
2. Use `poetry show --with dev` to verify dev dependencies are recognized before installing
3. Define all dependency groups explicitly in `pyproject.toml` with clear version constraints
