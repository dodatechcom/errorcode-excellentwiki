---
title: "[Solution] Python ImportError — Module Not Found Fix"
description: "Fix Python ImportError and ModuleNotFoundError. Install missing packages, check Python path, and resolve circular imports."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 60
---

# ImportError — Module Not Found Fix

An `ImportError` or `ModuleNotFoundError` is raised when Python cannot locate a module or a specific name within a module. This covers missing packages, incorrect paths, circular imports, and misspelled names.

## Description

`ImportError` is a broad category. Python 3.6+ introduced the more specific `ModuleNotFoundError` subclass for when the module file itself cannot be located. Other variants include:

- **`cannot import name 'X' from 'Y'`** — module exists but the specific name doesn't.
- **`No module named 'X'`** — module is not installed or not on `sys.path`.
- **Circular import** — module A imports B, which imports A before either finishes loading.
- **Wrong Python version** — package requires Python 3.10+ but you're running 3.8.

## Common Causes

```python
# Cause 1: Package not installed
import pandas  # ModuleNotFoundError if pandas is not pip-installed

# Cause 2: Typo in module name
import numPy  # ModuleNotFoundError: No module named 'numPy'

# Cause 3: Typo in imported name
from datetime import datetme  # ImportError: cannot import name 'datetme'

# Cause 4: Circular import
# a.py
from b import something
# b.py
from a import something_else  # ImportError due to circular dependency

# Cause 5: Wrong path — local file shadowing a package
# If you have a file named "random.py" in your working directory
import random  # Imports YOUR file, not the standard library
```

## Solutions

### Fix 1: Install the missing package

```bash
# Check if the package is installed
pip list | grep pandas

# Install it
pip install pandas

# Or use a specific version
pip install pandas==2.1.0

# For system-wide install
sudo pip install pandas
```

### Fix 2: Fix import name typos

```python
# Wrong
from datetime import datetme

# Correct
from datetime import datetime

# Verify what names a module exports
import datetime
print(dir(datetime))
```

### Fix 3: Resolve circular imports

```python
# Wrong — circular import
# config.py
from app import create_app

# app.py
from config import settings  # app.py already importing config

# Correct — defer the import to runtime
# config.py
def get_settings():
    from app import create_app  # Import inside the function
    return create_app().settings
```

### Fix 4: Avoid shadowing standard library modules

```bash
# Wrong — you named your file "random.py"
ls
# random.py  main.py

# Rename your file
mv random.py my_random_utils.py
```

```python
# If you must keep the filename, use absolute imports
from __future__ import absolute_import

# Or import from the full path
import importlib
random = importlib.import_module("random")
```

### Fix 5: Check sys.path when running scripts from other directories

```python
import sys

# See where Python looks for modules
for path in sys.path:
    print(path)

# Add a path manually if needed
sys.path.append("/home/user/my_project")
```

### Fix 6: Use virtual environments to isolate dependencies

```bash
# Create a virtual environment
python -m venv venv

# Activate it
source venv/bin/activate

# Install packages inside the venv
pip install requests pandas

# Deactivate when done
deactivate
```

## Related Errors

- [SyntaxError](../syntaxerror) — code can't be parsed before imports are even evaluated.
- [AttributeError](../attributeerror) — module exists but the attribute doesn't.
- [NameError](#) — variable not defined in current scope.
