---
title: "[Solution] Poetry Venv Error — Fix Virtual Environment Creation Failed"
description: "Fix Poetry virtual environment errors when poetry fails to create or locate the venv. Remove broken environments and configure Poetry venv settings properly."
tools: ["poetry"]
error-types: ["environment-error"]
severities: ["error"]
weight: 5
---

This error means Poetry could not create, access, or use the virtual environment for your project. Without a working venv, Poetry cannot install any packages.

## What This Error Means

Poetry creates a virtual environment per project (or uses a shared cache directory). When creation fails, you see:

```
EnvCommandError

Failed to create virtual environment
```

Or:

```
VirtualenvError

Virtual environment already exists but its Python is missing
```

## Why It Happens

- The Python version used to create the venv was uninstalled or upgraded
- The venv directory was manually deleted but Poetry still references it
- A symlink inside the venv points to a Python binary that no longer exists
- `virtualenvs.in-project` is set but `.venv` is corrupted
- The system is missing `venv` or `virtualenv` module
- Disk space is full in the venv location

## How to Fix It

### Let Poetry Recreate the Venv

```bash
poetry env remove --all
poetry install
```

### Force Remove a Specific Environment

```bash
poetry env list
poetry env remove python3.11
poetry install
```

### Configure In-Project Venvs

```bash
poetry config virtualenvs.in-project true
```

This puts `.venv` inside your project directory and makes it easy to manage with git.

### Point to a Specific Python Interpreter

```bash
poetry env use /usr/bin/python3.11
poetry install
```

### Check Available Python Versions

```bash
poetry env info
```

This shows whether the Python interpreter exists and is accessible.

### Manually Delete the Broken Venv

```bash
# Find where Poetry stores venvs
poetry config virtualenvs.path

# Remove the broken one
rm -rf $(poetry config virtualenvs.path)/<project-name>-<python-version>

# Recreate
poetry install
```

### Fix Missing venv Module on Debian/Ubuntu

```bash
sudo apt install python3-venv
```

## Common Mistakes

- Manually editing files inside the `.venv` directory
- Switching Python versions via `pyenv` without recreating the Poetry venv
- Setting `virtualenvs.in-project true` and then deleting `.venv` without telling Poetry
- Running `poetry install` after upgrading Python without first running `poetry env use`

## Related Pages

- [Poetry Python Version Error]({{< relref "/tools/poetry/poetry-python-version" >}}) -- incompatible Python versions
- [Poetry Install Error]({{< relref "/tools/poetry/poetry-install-error" >}}) -- install failures
- [Poetry Lock Error]({{< relref "/tools/poetry/poetry-lock-error" >}}) -- lock file issues
