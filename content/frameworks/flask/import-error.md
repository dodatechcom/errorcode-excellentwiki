---
title: "ImportError: cannot import name 'X'"
description: "Python raises ImportError when a name cannot be found in the specified module during an import statement."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Python cannot find the specified name (function, class, or variable) in the module you are trying to import. In Flask projects it frequently happens with circular imports or when referencing renamed/removed symbols.

## Common Causes

- Circular import between application modules (e.g. `models.py` importing from `app.py` which imports from `models.py`)
- The name was renamed or removed in the target module
- Typo in the imported name
- The module was not installed or is not on `sys.path`

## How to Fix

Break circular imports by moving shared code into a separate module or using lazy imports:

```python
# Instead of importing at the top of models.py
# from app import db

# Use lazy import inside the function/method
def create_user():
    from app import db
    db.session.add(user)
```

Verify the name exists in the target module:

```python
# Check what is actually exported
from mymodule import *
print(dir(mymodule))
```

## Example

```python
# auth.py
def authenticate():
    pass

# views.py
from auth import authenticte  # typo -- ImportError
```

```text
ImportError: cannot import name 'authenticte' from 'auth'
```

## Related Errors

- [TemplateNotFound: X.html]({{< relref "/frameworks/flask/template-not-found" >}})
