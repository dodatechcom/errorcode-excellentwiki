---
title: "[Solution] Python ImportError — Cannot Import Name"
description: "Fix Python ImportError when trying to import a specific name that doesn't exist. Learn why this happens and how to verify available names."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ImportError — Cannot Import Name

An `ImportError` with the message "cannot import name 'X' from 'Y'" is raised when you try to import a specific name from a module, but that name doesn't exist in the module. This can be due to typos, version differences, or incorrect import paths.

## Description

When using `from module import name`, Python looks for the specified name in the module's namespace. If the name doesn't exist, `ImportError` is raised. This is different from `ModuleNotFoundError`, which means the module itself cannot be found.

Common patterns:

- **Typo in name** — `from math import sqtr` instead of `sqrt`.
- **Version mismatch** — name doesn't exist in installed version.
- **Private name** — trying to import `__private` names.
- **Name defined conditionally** — name only exists in certain code paths.

## Common Causes

```python
# Cause 1: Typo in name
from math import sqtr  # ImportError: cannot import name 'sqtr' from 'math'

# Cause 2: Version mismatch
from collections import MutableMapping  # ImportError in Python 3.10+

# Cause 3: Name doesn't exist in module
from os import nonexistent_function  # ImportError

# Cause 4: Circular import preventing name resolution
# In module_a.py
from module_b import func_b
# In module_b.py
from module_a import func_a  # ImportError during circular import
```

## Solutions

### Fix 1: Check available names with dir()

```python
import math

# Debug — see what's available
print(dir(math))

# Or search for specific pattern
print([name for name in dir(math) if 'sqrt' in name])
```

### Fix 2: Use correct import for your Python version

```python
# Wrong — deprecated in Python 3.10+
from collections import MutableMapping

# Correct — use collections.abc
from collections.abc import MutableMapping
```

### Fix 3: Import the module directly and access the name

```python
# Wrong
from math import sqtr

# Correct
import math
result = math.sqrt(4)
```

### Fix 4: Verify the module path

```python
# Check where the module is located
import os
print(os.__file__)

# Check what names it exports
print(dir(os))
```

## Related Errors

- [ModuleNotFoundError](import-path) — module cannot be found.
- [Module attribute](module-attribute) — accessing non-existent module attributes.
- [Import circular](import-circular) — circular import dependencies.
