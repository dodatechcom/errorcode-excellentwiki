---
title: "[Solution] Python ImportError: scipy — Missing C Extensions"
description: "Fix Python ImportError: scipy missing C extensions. Reinstall SciPy, fix system dependencies, and resolve architecture mismatches."
languages: ["python"]
severities: ["error"]
error_types: ["runtime-error"]
tags: ["importerror", "scipy", "c-extension", "shared-library", "installation"]
weight: 5
---

# ImportError: scipy — Missing C Extensions

An `ImportError: cannot import name 'X' from partially initialized module 'scipy'` or `ImportError: scipy.X` means SciPy's compiled C/Fortran extensions failed to load. SciPy depends on BLAS, LAPACK, and Fortran runtime libraries.

## Description

SciPy wraps Fortran and C libraries (BLAS, LAPACK, FITPACK, etc.) for numerical computing. When the compiled `.so`/`.dll` files are missing or incompatible, Python raises an ImportError at import time.

- `ImportError: cannot import name '_minpack' from 'scipy'`
- `ImportError: liblapack.so.3: cannot open shared object file`
- `ImportError: scipy.optimize._minpack_pyx.cpython-311-x86_64-linux-gnu.so: undefined symbol`

## Common Causes

```python
# Cause 1: SciPy installed with wrong Python version
import scipy  # ImportError: cannot import name '_cython'

# Cause 2: Missing BLAS/LAPACK system libraries
import scipy  # ImportError: libopenblas.so

# Cause 3: NumPy and SciPy version incompatibility
import scipy  # ImportError: numpy.core.multiarray failed to import

# Cause 4: Partial installation from source
import scipy  # ImportError: cannot import name 'bandwidth'
```

## How to Fix

### Fix 1: Reinstall SciPy with correct wheel

```bash
pip uninstall scipy -y
pip install scipy --no-cache-dir --force-reinstall
```

### Fix 2: Install system dependencies

```bash
# Ubuntu/Debian
sudo apt-get install libopenblas-dev liblapack-dev gfortran

# macOS with Homebrew
brew install openblas lapack gfortran
```

### Fix 3: Pin compatible NumPy/SciPy versions

```bash
# Ensure compatibility
pip install "numpy>=1.25,<2" "scipy>=1.11,<2"
```

## Related Errors

- [ImportError: numpy — Missing C Extensions](importerror-numpy) — similar native extension issue
- [ModuleNotFoundError: No module named 'scipy'](#) — SciPy not installed at all
- [ValueError: non-broadcastable operands](scipy-sparse) — SciPy runtime shape mismatch
