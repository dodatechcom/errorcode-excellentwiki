---
title: "[Solution] Python TypeError — 'module' Object Is Not Callable"
description: "Fix Python TypeError when trying to call a module as a function. Learn why this happens and how to correctly call functions from modules."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["typeerror", "module", "callable", "import"]
weight: 5
---

# TypeError — 'module' Object Is Not Callable

A `TypeError` with the message "'module' object is not callable" is raised when you try to call a module using parentheses `()` instead of accessing a function from that module. Modules are not callable; you must call specific functions or classes within them.

## Description

When you `import module`, you get a module object. Module objects contain functions, classes, and other attributes, but they are not callable themselves. You need to access the specific function with dot notation before calling it.

Common patterns:

- **Calling the module directly** — `json()` instead of `json.loads()`.
- **Wrong import style** — `import json; json(data)` instead of `json.loads(data)`.
- **Shadowed function name** — a variable shadows the function name.
- **Missing function access** — forgetting to specify the function name.

## Common Causes

```python
# Cause 1: Calling module directly
import json
data = json('{"key": "value"}')  # TypeError: 'module' object is not callable

# Cause 2: Wrong import for function
import math
result = math(4)  # TypeError: 'module' object is not callable

# Cause 3: Shadowing function with module name
import json
json = json  # Module object assigned to variable named json
result = json('{"key": "value"}')  # TypeError

# Cause 4: Importing package instead of function
import os
result = os()  # TypeError: 'module' object is not callable
```

## Solutions

### Fix 1: Call the specific function from the module

```python
# Wrong
import json
data = json('{"key": "value"}')

# Correct
import json
data = json.loads('{"key": "value"}')
```

### Fix 2: Use from-import for direct function access

```python
# Wrong
import math
result = math(4)

# Correct — import the specific function
from math import sqrt
result = sqrt(4)  # Returns 2.0
```

### Fix 3: Don't shadow function names with variables

```python
# Wrong
import json
json = json  # Shadows the module
json('{"key": "value"}')  # TypeError

# Correct
import json
result = json.loads('{"key": "value"}')
```

### Fix 4: Check what you're importing

```python
import json

# Debug — check what json is
print(type(json))  # <class 'module'>

# The functions are attributes of the module
print(dir(json))  # Shows all available functions
```

## Related Errors

- [Call unsupported](call-unsupported) — calling non-callable objects.
- [Module attribute](module-attribute) — accessing non-existent module attributes.
- [Builtin function](builtin-function) — built-in function attribute errors.
