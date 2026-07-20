---
title: "[Solution] Python ImportError: No module named 'mypy' — Fix"
description: "Fix Python ImportError: No module named 'mypy'. Install mypy with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 304
---

# Python ImportError: No module named 'mypy'

The `ModuleNotFoundError: No module named 'mypy'` error occurs when Python cannot locate the mypy package, which provides static type checking for Python code.

## Common Causes

```python
# Cause 1: mypy not installed
# Running: mypy src/
# ModuleNotFoundError: No module named 'mypy'

# Cause 2: Installed for wrong Python version or virtual environment
import mypy  # ModuleNotFoundError

# Cause 3: mypy plugin cannot be loaded
# mypy.ini references plugins that require mypy itself
```

```python
# Cause 4: Pre-commit hook references mypy but not installed

# Cause 5: IDE integration cannot find mypy executable
# VSCode/Pylance configured to use mypy but package missing
```

## How to Fix

### Fix 1: Install mypy with pip

```bash
pip install mypy

# With additional type stubs
pip install mypy boto3-stubs

# Verify installation
mypy --version
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install mypy
mypy --install-types --non-interactive
```

### Fix 3: Add to project dev dependencies

```bash
# pyproject.toml
[project.optional-dependencies]
dev = ["mypy"]

# Install
pip install -e ".[dev]"
```

## Examples

```bash
# Type-check a module
mypy src/

# Type-check with strict mode
mypy --strict src/

# Type-check a single file
mypy mymodule.py

# Install missing type stubs
mypy --install-types --non-interactive
```

```python
# Using mypy programmatically
from mypy import api

result = api.run(["src/", "--strict"])
print(result[0])  # stdout
print(result[1])  # stderr
```

## Related Errors

- {{< relref "importerror-black" >}} — ImportError: black
- {{< relref "importerror-pydantic" >}} — ImportError: pydantic
- {{< relref "importerror-pycparser" >}} — ImportError: pycparser
