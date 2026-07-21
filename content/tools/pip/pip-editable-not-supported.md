---
title: "[Solution] pip Editable Not Supported -- Fix Editable Install Failure"
description: "Fix pip editable not supported errors when pip install -e fails because the project does not support editable mode. Configure build backend."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `pip install -e .` failed because the project's build backend does not support editable installs.

## Common Causes

- The project uses a build backend that does not support PEP 660
- setup.py is missing `ext_modules` configuration
- The project is a pure-Python package without proper setup

## How to Fix

### 1. Update pip and setuptools

```bash
pip install --upgrade pip setuptools wheel
```

### 2. Use --no-build-isolation

```bash
pip install --no-build-isolation -e .
```

### 3. Add PEP 660 Support

Ensure `pyproject.toml` or `setup.py` supports editable installs.

### 4. Install Without Editable Mode

```bash
pip install .
```

## Examples

```bash
$ pip install -e .
ERROR: Editable installs are not supported by this backend

$ pip install --upgrade pip setuptools wheel
$ pip install -e .
Building editable for myproject (pyproject.toml) ... done
```
