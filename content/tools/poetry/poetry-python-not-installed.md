---
title: "[Solution] Poetry Python Not Installed -- Fix Missing Python Interpreter"
description: "Fix Poetry Python not installed errors when Poetry cannot locate a Python interpreter on your system. Install Python and configure Poetry to find it."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry cannot find any Python interpreter on your system or in the locations it searches. Without Python, Poetry cannot create virtual environments or install packages.

## Common Causes

- Python is not installed on the system at all
- Poetry was installed in an isolated environment without Python
- The `python` or `python3` command is not in your PATH
- pyenv or asdf Python versions are not shimmed correctly
- Poetry's own Python was removed during an upgrade

## How to Fix

### 1. Verify Python Installation

```bash
python3 --version
which python3
```

If neither command returns output, install Python:

```bash
# Debian/Ubuntu
sudo apt install python3 python3-pip python3-venv

# macOS
brew install python@3.11
```

### 2. Tell Poetry Which Python to Use

```bash
poetry env use /usr/bin/python3.11
```

### 3. Install Poetry with a Specific Python

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 4. Check pyenv Shims

```bash
pyenv versions
pyenv global 3.11.4
```

## Examples

```bash
$ poetry install
PythonNotFound: Poetry requires Python but it was not found on your system.

# Fix:
$ python3 --version
# If missing, install Python 3.9+
$ poetry env use $(which python3)
```
