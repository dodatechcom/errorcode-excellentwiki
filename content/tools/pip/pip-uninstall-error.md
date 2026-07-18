---
title: "[Solution] Pip Uninstall Files Not Found Error Fix"
description: "Fix 'pip uninstall files not found' errors. Resolve package removal issues and leftover file cleanup in Python."
tools: ["pip"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Pip Uninstall Files Not Found Error Fix

The pip uninstall files not found error occurs when pip cannot locate the files to remove a package, usually because the package was installed differently or files were manually deleted.

## What This Error Means

pip records installed files in a metadata directory. When files are missing from disk but the package entry exists, uninstall fails because pip cannot find what to remove.

A typical error:

```
ERROR: Cannot uninstall package 'mypackage'. 
It is a distutils installed project and thus we cannot accurately 
determine which files belong to it which would lead to only a partial uninstall.
```

## Why It Happens

Common causes include:

- **Distutils installation** — Package installed without metadata tracking.
- **Files manually deleted** — Installed files were removed.
- **Different pip version** — Different pip installed different files.
- **Editable install** — Package installed in development mode.
- **System package manager installed** — Package came from apt/yum.
- **Multiple Python versions** — Installed under different Python.

## How to Fix It

### Fix 1: Force uninstall

```bash
# RIGHT: Force removal
pip uninstall package-name --yes

# Or ignore errors
pip uninstall package-name -y
```

### Fix 2: Manually remove package

```bash
# RIGHT: Find and remove manually
pip show package-name

# Find installation location
pip show -f package-name

# Remove directory
rm -rf /path/to/site-packages/package-name
rm -f /path/to/site-packages/package-name*.dist-info
```

### Fix 3: Use --target for custom installs

```bash
# RIGHT: Uninstall from custom location
pip uninstall --target /custom/path package-name
```

### Fix 4: Reinstall then uninstall

```bash
# RIGHT: Reinstall to fix metadata, then uninstall
pip install package-name
pip uninstall package-name
```

### Fix 5: Use pip to repair

```bash
# RIGHT: Force reinstall
pip install --force-reinstall package-name
pip uninstall package-name
```

## Common Mistakes

- **Assuming pip knows all installed files** — Distutils installs are not tracked.
- **Not checking if package is from system package manager** — Use apt/yum instead.
- **Using sudo with pip uninstall** — Avoid sudo with pip.

## Related Pages

- [Pip Check Error](pip-check-error) — Dependency conflict checks
- [Pip Show Error](pip-show-error) — Package info issues
- [Pip Install Error](/tools/pip/pip-install-error) — Installation problems
