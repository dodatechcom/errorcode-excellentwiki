---
title: "[Solution] Python ImportError: No module named 'colorama' — Fix"
description: "Fix Python ImportError: No module named 'colorama'. Install colorama with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 329
---

# Python ImportError: No module named 'colorama'

Colorama provides cross-platform colored terminal text output in Python. This error means the `colorama` package is missing from the active Python environment.

## Common Causes

```python
# Cause 1: colorama not installed
from colorama import Fore, Back, Style  # ImportError: No module named 'colorama'

# Cause 2: Installed as dependency but missing from requirements
# colorama pulled in by another package but not in requirements.txt

# Cause 3: Wrong virtual environment
# pip install colorama ran in a different venv

# Cause 4: Windows-only import path assumed
# Some code conditionally imports colorama only on Windows

# Cause 5: Package name vs import name confusion
# pip install colorama works; import Colorama does not
```

## How to Fix

### Fix 1: Install colorama with pip

```bash
pip install colorama

# For a specific version
pip install colorama==0.4.6

# Force reinstall if corrupted
pip install --force-reinstall colorama
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install colorama
python -c "from colorama import Fore; print(Fore.RED + 'OK')"
```

### Fix 3: Add to requirements.txt

```bash
echo "colorama==0.4.6" >> requirements.txt
pip install -r requirements.txt
```

## Examples

```python
from colorama import Fore, Style, init

init()
print(Fore.BLUE + "Information" + Style.RESET_ALL)
print(Fore.RED + "Error" + Style.RESET_ALL)
```

## Related Errors

- {{< relref "importcolorama" >}} — ImportError: colorama (variant)
- {{< relref "importerror-rich" >}} — ImportError: rich
- {{< relref "importerror-tqdm" >}} — ImportError: tqdm
