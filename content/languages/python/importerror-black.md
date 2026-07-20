---
title: "[Solution] Python ImportError: No module named 'black' — Fix"
description: "Fix Python ImportError: No module named 'black'. Install black with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 302
---

# Python ImportError: No module named 'black'

The `ModuleNotFoundError: No module named 'black'` error occurs when Python cannot locate the Black code formatter package, used for automatic Python code formatting.

## Common Causes

```python
# Cause 1: Black not installed
# Running: black .
# ModuleNotFoundError: No module named 'black'

# Cause 2: Installed for wrong Python version or virtual environment
import black  # ModuleNotFoundError

# Cause 3: Package name vs command name mismatch
# pip install black → command: black, import: black
```

```python
# Cause 4: Pre-commit hook cannot find black
# .pre-commit-config.yaml references black but it is not installed

# Cause 5: IDE formatter integration missing black
# VSCode/PyCharm cannot locate black for formatting
```

## How to Fix

### Fix 1: Install black with pip

```bash
pip install black

# With Jupyter support
pip install black[jupyter]

# Verify installation
black --version
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install black
black --check .
```

### Fix 3: Add to project dev dependencies

```bash
# pyproject.toml
[project.optional-dependencies]
dev = ["black"]

# Install
pip install -e ".[dev]"
```

## Examples

```bash
# Format all Python files in current directory
black .

# Check without modifying files
black --check .

# Format with specific line length
black --line-length 88 src/

# Format a single file
black myscript.py
```

```python
# Using black programmatically
from black import format_str, FileMode

code = "x  =  1"
formatted = format_str(code, mode=FileMode())
print(formatted)  # x = 1
```

## Related Errors

- {{< relref "importerror-isort" >}} — ImportError: isort
- {{< relref "importerror-pycparser" >}} — ImportError: pycparser
- {{< relref "importerror-mypy" >}} — ImportError: mypy
