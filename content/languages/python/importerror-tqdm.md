---
title: "[Solution] Python ImportError: tqdm not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: tqdm not found or ModuleNotFoundError: No module named 'tqdm'. Install tqdm properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: tqdm not found — ModuleNotFoundError Fix

An `ImportError: tqdm not found` or `ModuleNotFoundError: No module named 'tqdm'` means Python cannot locate the tqdm package.

## What This Error Means

tqdm is a fast, extensible progress bar library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: tqdm not installed
from tqdm import tqdm  # ModuleNotFoundError: No module named 'tqdm'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install tqdm

# For a specific version
pip install tqdm==4.66.1
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install tqdm
python -c "from tqdm import tqdm; print('OK')"
```

## Related Errors

- {{< relref "importerror-numpy" >}} — ImportError: numpy
- {{< relref "importerror-pandas" >}} — ImportError: pandas
- {{< relref "importerror-rich" >}} — ImportError: rich
