---
title: "[Solution] Python ImportError: No module named 'yaml' — Fix"
description: "Fix Python ImportError: No module named 'yaml'. Install PyYAML with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 327
---

# Python ImportError: No module named 'yaml'

PyYAML is a YAML parser and emitter for Python. The import name is `yaml`, not `pyyaml`. This error occurs when the package is not installed in the current environment.

## Common Causes

```python
# Cause 1: PyYAML not installed
import yaml  # ImportError: No module named 'yaml'

# Cause 2: Confusing package name with import name
# pip install pyyaml but then: import pyyaml — ImportError

# Cause 3: C extension build failure falls back to pure Python
# libyaml-dev not installed causes warnings or failures

# Cause 4: Virtual environment mismatch
# PyYAML installed in a different venv than the active one

# Cause 5: Case sensitivity
import YAML  # ImportError — must be lowercase
```

## How to Fix

### Fix 1: Install PyYAML with pip

```bash
pip install pyyaml

# For a specific version
pip install pyyaml==6.0.1

# With C extensions for better performance
pip install pyyaml --no-cache-dir
```

### Fix 2: Install libyaml system dependency first

```bash
# Ubuntu/Debian
sudo apt-get install libyaml-dev

# macOS
brew install libyaml

pip install pyyaml
```

### Fix 3: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pyyaml
python -c "import yaml; print(yaml.__version__)"
```

## Examples

```python
import yaml

data = yaml.safe_load("key: value")
print(data)
```

## Related Errors

- {{< relref "importerror-toml" >}} — ImportError: toml
- {{< relref "importerror-json" >}} — JSON decode errors
- {{< relref "importerror-configparser" >}} — configparser issues
