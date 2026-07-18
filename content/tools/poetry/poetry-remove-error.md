---
title: "[Solution] Poetry Package Removal Failed Error — How to Fix"
description: "Fix Poetry package removal failures. Resolve dependency removal errors, lock file issues, and broken package uninstallation in Poetry projects."
tools: ["poetry"]
error-types: ["remove-error"]
severities: ["error"]
weight: 5
comments: true
---

This error means Poetry failed to remove a package from your project. The package may be required by other packages, the lock file may be inconsistent, or the virtual environment may be in a broken state.

## Why It Happens

- Other packages in your project depend on the package you are trying to remove
- The package is listed in a dependency group but you did not specify the correct group
- The lock file references a package that was manually removed from `pyproject.toml`
- The virtual environment is corrupted and Poetry cannot update it
- The package was installed via pip inside the Poetry-managed venv
- You are trying to remove a package that is a direct dependency, not a dev dependency

## Common Error Messages

```
ValueError

package-name is a dependency of other packages in your
pyproject.toml: package-a, package-b.
```

```
PackageNotFound

package-name is not a dependency.
```

```
InstallationError

Failed to uninstall package-name because it is being used by:
  - package-a
  - package-b
```

```
RuntimeError

Unable to remove package-name from the virtual environment.
The environment may be corrupted.
```

## How to Fix It

### 1. Remove with the Correct Group

```bash
# Remove from the default (main) dependencies
poetry remove package-name

# Remove from a specific group
poetry remove --group dev package-name
poetry remove --group test package-name
```

### 2. Check What Depends on the Package

```bash
poetry show --tree | grep package-name
```

This shows which packages depend on the one you want to remove.

### 3. Remove Dependent Packages First

```bash
poetry remove dependent-package-a dependent-package-b package-name
```

### 4. Force Remove from pyproject.toml

If the package was already removed from `pyproject.toml` but the lock file is stale:

```bash
poetry lock
poetry install --sync
```

The `--sync` flag removes packages not in the lock file.

### 5. Reinstall the Virtual Environment

If the venv is corrupted:

```bash
# Remove the venv
poetry env remove --all

# Recreate and reinstall
poetry install
```

### 6. Remove a Pip-Installed Package

If the package was installed via pip inside the Poetry venv:

```bash
poetry run pip uninstall package-name
poetry install --sync
```

### 7. Verify Package Was Removed

```bash
poetry show | grep package-name
```

If the package still appears, run:

```bash
poetry lock
poetry install --sync
```

## Common Scenarios

**Removing a package that other packages need.** Check if an alternative package exists that does not have the same dependency chain. If not, keep the dependency.

**Removed from pyproject.toml but still installed.** Poetry does not automatically uninstall packages when you remove them from `pyproject.toml`. Run:

```bash
poetry install --sync
```

**Package name changed.** If a package was renamed, remove the old name and add the new one:

```bash
poetry remove old-package-name
poetry add new-package-name
```

## Prevent It

1. Always run `poetry install --sync` after removing packages to ensure the venv matches `pyproject.toml`
2. Use `poetry show --tree` before removing a package to understand its dependency relationships
3. Keep a clean separation between main and dev dependencies in `pyproject.toml` to avoid removal conflicts
