---
title: "[Solution] Python ImportError: numpy not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: numpy not found or ModuleNotFoundError: No module named 'numpy'. Install NumPy with pip, conda, or fix virtual environment."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ImportError: numpy not found — ModuleNotFoundError Fix

An `ImportError: numpy not found` or `ModuleNotFoundError: No module named 'numpy'` means Python cannot locate the NumPy package. This is one of the most common import errors because NumPy is a compiled C extension that must be installed separately and has architecture-specific requirements.

## Description

NumPy is not part of the Python standard library and must be installed via pip, conda, or your system package manager. The error can also occur when:

- NumPy is installed for a different Python version
- The virtual environment doesn't have NumPy
- NumPy was partially installed or corrupted
- A NumPy dependency (like BLAS/LAPACK) is missing on the system

## Common Causes

```python
# Cause 1: NumPy not installed at all
import numpy  # ModuleNotFoundError: No module named 'numpy'

# Cause 2: Installed for wrong Python version
# NumPy installed for Python 3.10, but running Python 3.11
python3.11 -c "import numpy"  # ModuleNotFoundError

# Cause 3: Virtual environment doesn't have NumPy
# Activated venv but NumPy was installed system-wide
source venv/bin/activate
python -c "import numpy"  # ModuleNotFoundError

# Cause 4: Corrupted installation
import numpy  # ImportError: numpy.core.multiarray failed to import
```

## How to Fix

### Fix 1: Install NumPy with pip

```bash
# Standard installation
pip install numpy

# For a specific Python version
pip3 install numpy

# For a specific version
pip install numpy==1.26.4
```

### Fix 2: Install in the correct virtual environment

```bash
# Make sure the venv is activated
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install NumPy in the activated environment
pip install numpy

# Verify installation
python -c "import numpy; print(numpy.__version__)"
```

### Fix 3: Install with conda

```bash
# If using Anaconda or Miniconda
conda install numpy

# For a specific environment
conda install -n myenv numpy

# Update NumPy
conda update numpy
```

### Fix 4: Fix corrupted installation

```bash
# Uninstall and reinstall
pip uninstall numpy
pip install numpy --force-reinstall

# Or install with --no-cache-dir
pip install numpy --no-cache-dir
```

### Fix 5: Install system-level dependencies (Linux)

```bash
# Ubuntu/Debian
sudo apt-get install python3-numpy
# or
sudo apt-get install python3-numpy-dev

# CentOS/RHEL
sudo yum install python3-numpy

# For building from source
sudo apt-get install build-essential libopenblas-dev liblapack-dev
pip install numpy
```

### Fix 6: Check which Python is being used

```bash
# Verify which Python and pip are being used
which python
which pip

# Check if NumPy is installed for that Python
python -m pip show numpy

# Install for the correct Python
python -m pip install numpy
```

## Examples

This error commonly occurs when:

- After cloning a project and running it without installing dependencies first
- When switching between Python versions without reinstalling packages
- After upgrading macOS/Linux which may break compiled packages
- When using Docker without NumPy in the Dockerfile

## Related Errors

- [ImportError: cannot import name](#) — NumPy installed but specific function missing
- [ModuleNotFoundError: No module named](#) — general missing module
- [ImportError: DLL load failed](#) — Windows-specific NumPy binary issue
