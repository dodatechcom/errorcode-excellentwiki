---
title: "[Solution] Python ImportError: No module named 'colorama' — Fix"
description: "Fix Python ImportError: No module named 'colorama'. Install colorama with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 329
---

# Python ImportError: No module named 'colorama'

Colorama is a Python library that provides cross-platform colored terminal text. This error occurs when the `colorama` package is not installed in the current Python environment.

## Common Causes

```python
# Cause 1: colorama not installed
import colorama  # ImportError: No module named 'colorama'

# Cause 2: Capital letter confusion
import Colorama  # ImportError — must be lowercase

# Cause 3: Installed for wrong Python version
pip install colorama  # installs for python3 but you run python3.12

# Cause 4: Virtual environment mismatch
# colorama installed in a different venv than active one

# Cause 5: Dependency conflict
# Another package requires a specific colorama version
```

## How to Fix

### Fix 1: Install colorama with pip

```bash
pip install colorama

# For a specific version
pip install colorama==0.4.6
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install colorama
python -c "import colorama; print(colorama.__version__)"
```

### Fix 3: Install alongside common companions

```bash
pip install colorama rich click tqdm
```

## Examples

```python
import colorama
colorama.init()

from colorama import Fore, Style
print(Fore.GREEN + "Success!" + Style.RESET_ALL)
```

## Related Errors

- {{< relref "importerror-colorama" >}} — ImportError: colorama (variant)
- {{< relref "importerror-tqdm" >}} — ImportError: tqdm
- {{< relref "importerror-click" >}} — ImportError: click
