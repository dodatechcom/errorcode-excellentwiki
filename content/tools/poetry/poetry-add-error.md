---
title: "[Solution] Poetry Package Add Failed Error — How to Fix"
description: "Fix Poetry package add failures when poetry add cannot resolve or install a package. Resolve version conflicts, source issues, and dependency resolution errors."
tools: ["poetry"]
error-types: ["add-error"]
severities: ["error"]
weight: 5
comments: true
---

This error means Poetry failed to add a new package to your project. The solver could not find a compatible version, the package does not exist on the configured sources, or adding the package creates an unresolvable conflict with existing dependencies.

## Why It Happens

- The package name is misspelled or does not exist on PyPI
- The requested version conflicts with an existing dependency's constraints
- The package requires a different Python version than your project specifies
- The package is hosted on a private repository that is not configured
- The solver cannot find a combination of versions that satisfies all constraints
- The package has been yanked from PyPI or has malformed metadata

## Common Error Messages

```
PackageNotFound

Package "package-name" not found.
```

```
SolverProblemError

Because my-project depends on package-name (>=2.0)
and existing-package (>=1.0) depends on package-a (<2.0),
package-name (>=2.0) cannot be installed.
```

```
HTTPError

404 Not Found: https://pypi.org/simple/package-name/
```

```
InvalidVersion

Invalid version "1.0.0.dev1.post2"
```

## How to Fix It

### 1. Verify the Package Exists

```bash
pip index versions package-name 2>/dev/null || echo "Package not found on PyPI"
```

Or check directly:

```bash
curl -s https://pypi.org/pypi/package-name/json | python -c "import sys,json; print('Found' if sys.stdin.read(1) == '{' else 'Not found')"
```

### 2. Specify a Compatible Version

```bash
# Add the latest version
poetry add package-name@latest

# Add a specific version
poetry add package-name@1.5.0

# Add with version range
poetry add package-name@^1.5
```

### 3. Check Existing Constraints

```bash
poetry show --tree
poetry show package-name
```

If a dependency already constrains `package-name`, you may need to update both.

### 4. Configure a Private Repository

```toml
[[tool.poetry.source]]
name = "private-pypi"
url = "https://pypi.company.com/simple/"
priority = "supplemental"
```

```bash
poetry add package-name --source private-pypi
```

### 5. Use pip as a Fallback

```bash
poetry run pip install package-name
```

Then add it to `pyproject.toml` manually:

```toml
[tool.poetry.dependencies]
package-name = {version = "^1.0", optional = true}
```

### 6. Relax Existing Version Constraints

If the conflict is with an existing package, relax its constraint:

```bash
poetry add existing-package@^2.0
poetry add package-name
```

### 7. Update the Lock File

```bash
poetry add package-name
poetry lock
poetry install
```

## Common Scenarios

**Package exists on PyPI but Poetry cannot find it.** The package name may differ from the import name. Check the PyPI page for the correct distribution name.

**Adding a package conflicts with existing dependencies.** Use `poetry add package-name --dry-run` to preview the impact before making changes.

**Private package not found.** Configure the private repository in `pyproject.toml` and use `--source` to specify it.

## Prevent It

1. Always verify a package exists on PyPI before running `poetry add` to catch typos early
2. Run `poetry add --dry-run` for unfamiliar packages to preview compatibility with existing dependencies
3. Keep `pyproject.toml` version constraints flexible (use `^` or `>=`) to avoid blocking new additions
