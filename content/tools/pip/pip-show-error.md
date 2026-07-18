---
title: "[Solution] Pip Show Package Not Found Error Fix"
description: "Fix 'pip show package not found' errors. Display package information and troubleshoot missing package metadata in Python."
tools: ["pip"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Pip Show Package Not Found Error Fix

The pip show package not found error occurs when pip cannot find metadata for the specified package, either because it is not installed or the metadata is missing.

## What This Error Means

pip show displays detailed information about installed packages. When the package name is wrong, not installed, or metadata was corrupted, pip returns this error.

A typical error:

```
Package(s) not found: mypackage
```

## Why It Happens

Common causes include:

- **Package not installed** — Never installed or was uninstalled.
- **Wrong package name** — Typo or wrong name.
- **Different Python version** — Installed in different Python environment.
- **Editable install** — Package installed with pip install -e.
- **Missing metadata** — .dist-info directory missing or corrupted.
- **Virtual environment** — Package in different virtualenv.

## How to Fix It

### Fix 1: Check if package is installed

```bash
# RIGHT: List all packages
pip list

# Search for package
pip list | grep -i mypackage

# Check specific package
pip show mypackage
```

### Fix 2: Verify correct package name

```bash
# RIGHT: Search PyPI for correct name
pip index versions mypackage

# Check installed names
pip list --format=columns
```

### Fix 3: Check Python environment

```bash
# RIGHT: Verify which Python/pip
which pip
which python
python -m pip show mypackage

# Check virtual environment
pip list --local
```

### Fix 4: Install if missing

```bash
# RIGHT: Install package
pip install mypackage

# Install specific version
pip install mypackage==1.0.0
```

### Fix 5: Fix corrupted metadata

```bash
# RIGHT: Force reinstall to fix metadata
pip install --force-reinstall mypackage

# Or reinstall from source
pip install --no-cache-dir --force-reinstall mypackage
```

## Common Mistakes

- **Confusing package name with import name** — `pip show Pillow` not `pip show pillow`.
- **Checking wrong Python** — Use `python -m pip` to be explicit.
- **Not activating virtual environment** — Always activate venv first.

## Related Pages

- [Pip Check Error](pip-check-error) — Dependency conflict checks
- [Pip Freeze Error](pip-freeze-error) — Dependency listing issues
- [Pip Uninstall Error](pip-uninstall-error) — Package removal issues
