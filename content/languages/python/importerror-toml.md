---
title: "[Solution] Python ImportError: No module named 'toml' — Fix"
description: "Fix Python ImportError: No module named 'toml'. Install toml with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 328
---

# Python ImportError: No module named 'toml'

The `toml` package is a Python library for reading and writing TOML configuration files. This error occurs when the package is not installed in the current Python environment.

## Common Causes

```python
# Cause 1: toml not installed
import toml  # ImportError: No module named 'toml'

# Cause 2: Using toml instead of tomllib (Python 3.11+)
import tomllib  # Works in Python 3.11+ but not in older versions

# Cause 3: Confusing toml with tomlkit
import tomlkit  # Different package — toml still missing

# Cause 4: Virtual environment mismatch
# toml installed in a different venv

# Cause 5: Python version too old for tomllib
import tomllib  # ModuleNotFoundError in Python < 3.11
```

## How to Fix

### Fix 1: Install toml with pip

```bash
pip install toml

# For a specific version
pip install toml==0.10.2

# Alternative: use tomlkit for round-trip editing
pip install tomlkit
```

### Fix 2: Use tomllib on Python 3.11+

```python
# Python 3.11+ has tomllib built in (read-only)
import tomllib

with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)

# For writing, still install toml or tomlkit
```

### Fix 3: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install toml
python -c "import toml; print(toml.__version__)"
```

## Examples

```python
import toml

config = toml.load("pyproject.toml")
print(config["project"]["name"])
```

## Related Errors

- {{< relref "importerror-pyyaml" >}} — ImportError: yaml
- {{< relref "importerror-configparser" >}} — configparser issues
- {{< relref "importerror-deprecated" >}} — Deprecation warnings
