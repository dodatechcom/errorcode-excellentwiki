---
title: "[Solution] Python Pylint Configuration Error — How to Fix"
description: "Fix Python Pylint configuration errors. Resolve import errors, false positives, and plugin issues with Pylint."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Pylint Configuration Error

A Pylint error occurs when the static analysis tool fails to check Python code due to import resolution issues, configuration problems, or incompatible plugins.

## Why It Happens

Pylint attempts to statically analyze Python code by importing modules and resolving types. When modules are not installed, have C extensions, or use dynamic features like __getattr__, Pylint cannot resolve imports and reports false positives.

## Common Error Messages

- `E0401: Unable to import 'module_name'`
- `E1101: Module 'X' has no 'Y' member`
- `W0511: TODO/FIXME in code`
- `E0611: No name 'Y' in module 'X'`

## How to Fix It

### Fix 1: Configure ignored modules

```python
# .pylintrc or pyproject.toml
[tool.pylint]
ignored-modules = ["cv2", "numpy", "pandas"]
ignored-classes = ["numpy.ndarray"]
```

### Fix 2: Use pyproject.toml for configuration

```python
[tool.pylint.'messages control']
disable = [
    'import-error',
    'no-member',
    'too-few-public-methods',
]

[tool.pylint.format]
max-line-length = 120
```

### Fix 3: Add type stubs for third-party libraries

```python
# py.typed marker file
# For custom modules, add __init__.pyi stubs
from typing import Any

def my_function(x: Any) -> Any: ...
```

### Fix 4: Run Pylint with specific paths

```python
# .pylintrc
[MASTER]
source-roots = ["src", "tests"]
init-hook = ['import sys; sys.path.insert(0, "src")']
```

## Common Scenarios

- **Virtual environment issues** — Pylint installed globally cannot find packages in virtualenv.
- **C extension modules** — Modules with C extensions like numpy fail to import.
- **Dynamic imports** — Code using importlib or __getattr__ triggers false import errors.

## Prevent It

- Install Pylint in the same virtual environment as your project
- Use pyproject.toml instead of .pylintrc for centralized configuration
- Run pylint with --generate-rcfile to see all options

## Related Errors

- - [flake8 Error](/languages/python/flake8-error/) — linter configuration issues
- - [ImportError](/languages/python/importerror/) — module not found
