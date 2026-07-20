---
title: "[Solution] Python ModuleNotFoundError — Module Not Found Fix"
description: "Fix Python ModuleNotFoundError with missing packages, typos, virtual environments, and path issues. Install, configure, and debug import failures."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 22
---

# Python ModuleNotFoundError — Module Not Found Fix

A `ModuleNotFoundError` is raised when Python cannot locate a module during an `import` statement. It is a subclass of `ImportError` and typically indicates a missing package, incorrect module name, or environment misconfiguration.

## Common Causes

```python
# Cause 1: Package not installed
import requests  # ModuleNotFoundError: No module named 'requests'

# Cause 2: Typo in module name
import numpi  # Should be 'numpy'

# Cause 3: Wrong version — module exists in different package
import yaml  # Should be 'pyyaml' — module name differs from pip package name
# Correct: import yaml  (after pip install pyyaml)

# Cause 4: Virtual environment not activated
# Running system Python instead of venv Python
# Module installed in venv but script runs with /usr/bin/python

# Cause 5: Module in subdirectory without __init__.py
# project/
#   mypackage/
#     utils.py
#   main.py
# from mypackage import utils  # ModuleNotFoundError (Python 3.3+ usually works,
#                                 but missing __init__.py can cause issues in some setups)
```

## How to Fix

### Fix 1: Install the missing package with pip

```bash
# Wrong — module not installed
# ModuleNotFoundError: No module named 'requests'

# Correct
pip install requests

# Or for a specific version
pip install requests==2.31.0

# For packages where module name differs from package name
pip install pyyaml    # Then: import yaml
pip install pillow    # Then: from PIL import Image
pip install scikit-learn  # Then: import sklearn
```

### Fix 2: Check for typos in module and package names

```python
# Wrong
import numpi        # Typo
import matploitlib   # Typo
import bsfour        # Wrong

# Correct
import numpy
import matplotlib
from bs4 import BeautifulSoup
```

### Fix 3: Activate the correct virtual environment

```bash
# Check which Python is being used
which python
python -c "import sys; print(sys.executable)"

# Activate virtual environment
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows

# Or use the venv's Python directly
venv/bin/python script.py

# Reinstall the package in the correct environment
pip install requests
```

### Fix 4: Verify the module path is correct

```python
import sys
print(sys.path)

# Add a custom path if needed
import sys
sys.path.append("/path/to/my/modules")
import my_module
```

### Fix 5: Check if the package requires a different install name

```python
# Common mismatches between pip name and import name:
# pip install opencv-python  →  import cv2
# pip install scikit-learn   →  import sklearn
# pip install python-dateutil →  import dateutil
# pip install Pillow         →  from PIL import Image
# pip install PyYAML         →  import yaml

# To find the correct import name:
pip show <package-name>  # Shows the package metadata
```

## Prevention Checklist

- Always activate your virtual environment before installing or running packages.
- Use `pip install <package>` and verify with `pip list` before importing.
- Check package documentation for correct import names — pip names often differ.
- Add a `requirements.txt` and pin versions for reproducible environments.
- Use `python -c "import module_name"` to quickly test if a module is available.

## Related Errors

- [ImportError](/languages/python/importerror/) — broader import failure including missing names within a module.
- [ModuleNotFoundError](/languages/python/importerror/) — base class for import failures.
- [FileNotFoundError](/languages/python/filenotfounderror/) — file not found on disk.
- [SyntaxError](/languages/python/syntaxerror/) — module exists but has syntax errors.
