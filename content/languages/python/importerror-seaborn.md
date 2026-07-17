---
title: "[Solution] Python ImportError: seaborn not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: seaborn not found or ModuleNotFoundError: No module named 'seaborn'. Install seaborn properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: seaborn not found — ModuleNotFoundError Fix

An `ImportError: seaborn not found` or `ModuleNotFoundError: No module named 'seaborn'` means Python cannot locate the seaborn package.

## What This Error Means

seaborn is a statistical data visualization library built on matplotlib. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: seaborn not installed
import seaborn  # ModuleNotFoundError: No module named 'seaborn'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install seaborn
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install seaborn
python -c "import seaborn; print(seaborn.__version__)"
```

## Related Errors

- {{< relref "importerror-matplotlib" >}} — ImportError: matplotlib
- {{< relref "importerror-pandas" >}} — ImportError: pandas
- {{< relref "importerror-numpy" >}} — ImportError: numpy
