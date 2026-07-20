---
title: "[Solution] Python ImportError: No module named 'isort' — Fix"
description: "Fix Python ImportError: No module named 'isort'. Install isort with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 303
---

# Python ImportError: No module named 'isort'

The `ModuleNotFoundError: No module named 'isort'` error occurs when Python cannot locate the isort package, which automatically sorts and organizes Python imports.

## Common Causes

```python
# Cause 1: isort not installed
# Running: isort .
# ModuleNotFoundError: No module named 'isort'

# Cause 2: Installed for wrong Python version or virtual environment
import isort  # ModuleNotFoundError

# Cause 3: IDE integration cannot find isort
# VSCode/PyCharm configured to use isort but package missing
```

```python
# Cause 4: Pre-commit hook references isort but not installed
# .pre-commit-config.yaml requires isort

# Cause 5: isort conflicts with black profile
# isort configured with incompatible settings
```

## How to Fix

### Fix 1: Install isort with pip

```bash
pip install isort

# Verify installation
isort --version-number
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install isort
isort --check-only --diff .
```

### Fix 3: Add to project dev dependencies

```bash
# requirements-dev.txt
isort

# Install
pip install -r requirements-dev.txt
```

## Examples

```bash
# Sort imports in all files
isort .

# Check without modifying
isort --check-only --diff .

# Sort with black-compatible profile
isort --profile black .

# Sort a single file
isort mymodule.py
```

```python
# Using isort programmatically
from isort import place_module, Config

config = Config(profile="black")
result = place_module("os", config=config)
print(result)  # ['STDLIB']
```

## Related Errors

- {{< relref "importerror-black" >}} — ImportError: black
- {{< relref "importerror-pycparser" >}} — ImportError: pycparser
- {{< relref "importerror-mypy" >}} — ImportError: mypy
