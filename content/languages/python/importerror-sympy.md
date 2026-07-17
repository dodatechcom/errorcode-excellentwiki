---
title: "[Solution] Python ImportError: sympy not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: sympy not found or ModuleNotFoundError: No module named 'sympy'. Install SymPy properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: sympy not found — ModuleNotFoundError Fix

An `ImportError: sympy not found` or `ModuleNotFoundError: No module named 'sympy'` means Python cannot locate the SymPy package.

## What This Error Means

SymPy is a Python library for symbolic mathematics. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: sympy not installed
import sympy  # ModuleNotFoundError: No module named 'sympy'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install sympy

# For a specific version
pip install sympy==1.12
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install sympy
python -c "import sympy; print(sympy.__version__)"
```

## Related Errors

- {{< relref "importerror-numpy" >}} — ImportError: numpy
- {{< relref "importerror-scipy" >}} — ImportError: scipy
- {{< relref "importerror-sklearn" >}} — ImportError: sklearn
