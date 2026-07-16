---
title: "[Solution] Python ImportError — Circular Import"
description: "Fix Python ImportError caused by circular imports. Learn why circular imports happen and how to restructure your code to avoid them."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["importerror", "circular", "import", "module"]
weight: 5
---

# ImportError — Circular Import

An `ImportError` caused by a circular import occurs when two or more modules import each other, directly or indirectly. Python cannot resolve the imports because each module depends on the other being fully loaded first.

## Description

When Python imports a module, it executes the module's code from top to bottom. If module A imports module B, and module B imports module A, Python gets into a circular dependency. During the second import, module A is not yet fully loaded, so names defined later in module A are not yet available.

Common patterns:

- **Two modules importing each other** — `a.py` imports `b.py` and `b.py` imports `a.py`.
- **Package circular imports** — modules within the same package importing each other.
- **Importing at module level** — top-level imports create circular dependencies.
- **Deep import chains** — A imports B, B imports C, C imports A.

## Common Causes

```python
# Cause 1: Two modules importing each other
# module_a.py
from module_b import func_b

def func_a():
    return "a"

# module_b.py
from module_a import func_a  # ImportError: cannot import name 'func_a'

def func_b():
    return "b"

# Cause 2: Circular import within a package
# mypackage/__init__.py
from .module_a import func_a

# mypackage/module_a.py
from .module_b import func_b

# mypackage/module_b.py
from .module_a import func_a  # Circular!

# Cause 3: Importing at module level when not needed
# config.py
DATABASE_URL = "sqlite:///db.sqlite"

# models.py
from config import DATABASE_URL  # Fine if no circular dependency

# main.py
import config
import models
```

## Solutions

### Fix 1: Move imports inside functions (lazy imports)

```python
# Wrong — circular import at module level
# module_a.py
from module_b import func_b

def func_a():
    return func_b()

# Correct — import inside the function
# module_a.py
def func_a():
    from module_b import func_b
    return func_b()
```

### Fix 2: Restructure code to break the cycle

```python
# Wrong — circular dependency
# a.py
from b import helper
def func_a(): return helper()

# b.py
from a import func_a  # Circular!

# Correct — extract shared code to a third module
# shared.py
def helper():
    return "shared"

# a.py
from shared import helper
def func_a():
    return helper()

# b.py
from a import func_a
```

### Fix 3: Use import at module level for types, inside functions for usage

```python
# Wrong
# module_a.py
from module_b import ClassB  # Circular

def create_b():
    return ClassB()

# Correct — use TYPE_CHECKING for type hints only
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from module_b import ClassB

def create_b() -> "ClassB":
    from module_b import ClassB
    return ClassB()
```

### Fix 4: Delay imports until needed

```python
# Wrong — importing everything at the top
import module_a
import module_b
import module_c

# Correct — import only when needed
def process_data():
    import module_a
    return module_a.process()

def generate_report():
    import module_b
    return module_b.report()
```

## Related Errors

- [ModuleNotFoundError](import-path) — module cannot be found.
- [ImportError](../importerror) — general import errors.
- [RecursionError](../recursionerror) — related to deep dependency chains.
