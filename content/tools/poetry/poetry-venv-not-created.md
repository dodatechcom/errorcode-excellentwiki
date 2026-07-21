---
title: "[Solution] Poetry Venv Not Created -- Fix Virtual Environment Creation"
description: "Fix Poetry venv not created errors when Poetry fails to create a new virtual environment. Check system Python and disk space."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry could not create a virtual environment. The process failed during or before venv creation.

## Common Causes

- The system Python lacks the `venv` module
- Disk space is insufficient in the cache directory
- Permissions prevent writing to the venv directory
- The Python executable is not a standard CPython build

## How to Fix

### 1. Check for the venv Module

```bash
python3 -m venv --help
```

If this fails, install it:

```bash
# Debian/Ubuntu
sudo apt install python3-venv
```

### 2. Configure In-Project Venv

```bash
poetry config virtualenvs.in-project true
```

### 3. Check Disk Space

```bash
df -h $(poetry config cache-dir)
```

### 4. Use a Specific Python

```bash
poetry env use $(which python3.11)
```

## Examples

```bash
$ poetry install
ensurepip is not available

# Fix:
$ sudo apt install python3.11-venv
$ poetry env use /usr/bin/python3.11
$ poetry install
Installing dependencies from lock file...
```
