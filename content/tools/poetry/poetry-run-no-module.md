---
title: "[Solution] Poetry Run No Module -- Fix Module Not Found in poetry run"
description: "Fix poetry run no module errors when the specified module cannot be found in the virtual environment. Install the module or check the name."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `poetry run python -m <module>` failed because the module is not installed in the virtual environment.

## Common Causes

- The module is not listed as a dependency in `pyproject.toml`
- The module name differs from the PyPI package name
- The virtual environment is stale
- The module is in an optional group not yet installed

## How to Fix

### 1. Install the Module

```bash
poetry add <module-name>
```

### 2. Install All Optional Groups

```bash
poetry install --with dev,test
```

### 3. Check Installed Packages

```bash
poetry show | grep <module>
```

### 4. Run from the Project Directory

```bash
cd /path/to/project
poetry run python -m <module>
```

## Examples

```bash
$ poetry run python -m pytest
No module named pytest

$ poetry add --group dev pytest
$ poetry install --with dev
$ poetry run python -m pytest
======================== no tests ran =========================
```
