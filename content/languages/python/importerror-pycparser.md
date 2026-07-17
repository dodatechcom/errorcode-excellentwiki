---
title: "[Solution] Python ImportError: pycparser not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: pycparser not found or ModuleNotFoundError: No module named 'pycparser'. Install pycparser properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: pycparser not found — ModuleNotFoundError Fix

An `ImportError: pycparser not found` or `ModuleNotFoundError: No module named 'pycparser'` means Python cannot locate the pycparser package.

## What This Error Means

pycparser is a C parser in Python. It is a dependency of cffi. It is not part of the standard library.

## Common Causes

```python
# Cause 1: pycparser not installed
import pycparser  # ModuleNotFoundError: No module named 'pycparser'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install pycparser
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install pycparser
python -c "import pycparser; print(pycparser.__version__)"
```

## Related Errors

- {{< relref "importerror-cffi" >}} — ImportError: cffi
- {{< relref "importerror-cryptography" >}} — ImportError: cryptography
- {{< relref "importerror-lxml" >}} — ImportError: lxml
