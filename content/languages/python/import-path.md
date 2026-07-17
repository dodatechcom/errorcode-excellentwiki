---
title: "[Solution] Python ModuleNotFoundError — No Module Named"
description: "Fix Python ModuleNotFoundError when a module cannot be found. Learn why this error occurs and how to install or locate missing modules."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ModuleNotFoundError — No Module Named

A `ModuleNotFoundError` with the message "No module named 'X'" is raised when Python cannot find a module during an import statement. This is a subclass of `ImportError` introduced in Python 3.6.

## Description

Python searches for modules in the `sys.path` list, which includes the current directory, installed packages, and standard library. When a module is not found in any of these locations, `ModuleNotFoundError` is raised. This is different from `ImportError`, which indicates the module was found but failed to load.

Common patterns:

- **Typo in module name** — `import nump` instead of `import numpy`.
- **Module not installed** — using a third-party package without installing it.
- **Wrong import path** — incorrect package structure.
- **Virtual environment not activated** — packages installed in a different environment.

## Common Causes

```python
# Cause 1: Typo in module name
import nump  # ModuleNotFoundError: No module named 'nump'

# Cause 2: Module not installed
import pandas  # ModuleNotFoundError if pandas is not installed

# Cause 3: Wrong import path
from mypackage.subpackage import module  # ModuleNotFoundError if path is wrong

# Cause 4: Virtual environment not activated
# Packages installed in venv but running outside it
import requests  # ModuleNotFoundError
```

## Solutions

### Fix 1: Install the missing module

```bash
# Check if the module is installed
pip list | grep module_name

# Install the module
pip install module_name

# Or with specific version
pip install module_name==1.2.3
```

### Fix 2: Check for typos in module name

```python
# Wrong
import nump  # ModuleNotFoundError

# Correct
import numpy
```

### Fix 3: Verify the import path

```python
# Wrong — wrong package structure
from mypackage.module import function

# Correct — check package structure
import mypackage
print(mypackage.__file__)  # Shows where the package is located
```

### Fix 4: Activate the correct virtual environment

```bash
# Check current Python
which python

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Verify
python -c "import sys; print(sys.path)"
```

### Fix 5: Add module path to sys.path

```python
import sys
sys.path.append("/path/to/your/module")

import your_module  # Now importable
```

## Related Errors

- [ImportError](../importerror) — module found but failed to load.
- [Import circular](import-circular) — circular import dependencies.
- [Import version](import-version) — wrong name in import.
