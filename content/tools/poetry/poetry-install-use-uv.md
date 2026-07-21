---
title: "[Solution] Poetry Install Use UV -- Fix UV Installer Compatibility"
description: "Fix Poetry install use uv errors when the UV-backed installer fails. Disable UV or configure the fallback installer."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry tried to use the UV installer backend but encountered an incompatibility or failure. UV is an alternative installer.

## Common Causes

- UV is not installed on the system
- UV version is incompatible with Poetry
- The package requires features UV does not support
- UV installation is corrupted

## How to Fix

### 1. Disable UV Installer

```bash
poetry config installer.parallel true
```

Or in `poetry.toml`:

```toml
[installer]
parallel = true
```

### 2. Install UV

```bash
pip install uv
```

### 3. Use the Default Installer

```bash
POETRY_USE_MODERN_INSTALLER=0 poetry install
```

### 4. Check UV Version

```bash
uv --version
pip install --upgrade uv
```

## Examples

```bash
$ poetry install
InstallerError: uv failed to resolve dependencies

$ POETRY_USE_MODERN_INSTALLER=0 poetry install
Installing dependencies from lock file...
```
