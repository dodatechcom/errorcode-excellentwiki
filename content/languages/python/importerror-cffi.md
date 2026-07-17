---
title: "[Solution] Python ImportError: cffi not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: cffi not found or ModuleNotFoundError: No module named 'cffi'. Install cffi properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: cffi not found — ModuleNotFoundError Fix

An `ImportError: cffi not found` or `ModuleNotFoundError: No module named 'cffi'` means Python cannot locate the cffi package.

## What This Error Means

cffi is the C Foreign Function Interface for Python. Many packages depend on it. It requires a C compiler to build from source.

## Common Causes

```python
# Cause 1: cffi not installed
import cffi  # ModuleNotFoundError: No module named 'cffi'

# Cause 2: Missing C compiler
# pip install cffi fails with compilation errors
```

## How to Fix

### Fix 1: Install with pip

```bash
# Install build tools first (Ubuntu/Debian)
sudo apt-get install build-essential python3-dev

# Then install cffi
pip install cffi
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install cffi
python -c "import cffi; print(cffi.__version__)"
```

## Related Errors

- {{< relref "importerror-pycparser" >}} — ImportError: pycparser
- {{< relref "importerror-cryptography" >}} — ImportError: cryptography
- {{< relref "importerror-lxml" >}} — ImportError: lxml
