---
title: "[Solution] Python PendingDeprecationWarning — Planned Deprecation Fix"
description: "Handle Python PendingDeprecationWarning when features are planned for deprecation. Update code proactively, migrate to new APIs, and suppress warnings."
languages: ["python"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PendingDeprecationWarning — Planned Deprecation Fix

A `PendingDeprecationWarning` is raised when a feature is planned for deprecation but hasn't been officially deprecated yet. It's a subclass of `Warning` and is ignored by default. This gives developers advance notice that a feature will eventually be removed.

## Description

`PendingDeprecationWarning` is a step before `DeprecationWarning`. When Python maintainers or library authors want to signal that a feature will be deprecated but hasn't decided exactly when, they use this warning. It's even less visible than `DeprecationWarning` (both are ignored by default), but it indicates that migration should begin.

Note: `PendingDeprecationWarning` is rarely used in practice. Most Python developers skip straight to `DeprecationWarning` when marking features for removal. If you see this warning, it's a strong signal to migrate your code.

Common scenarios:

- **Upcoming API changes** — library plans to change function signatures.
- **Module reorganization** — modules that will be moved or renamed.
- **Behavior changes** — functions that will change default behavior.
- **Feature removal** — functionality scheduled for eventual removal.

## Common Causes

```python
import warnings

# Cause 1: Using a function with pending deprecation
def old_api():
    """This function will be deprecated."""
    warnings.warn(
        "old_api() will be deprecated, use new_api()",
        PendingDeprecationWarning
    )
    return "result"

result = old_api()  # PendingDeprecationWarning

# Cause 2: Using deprecated module attribute
import json
# Some module attributes may trigger pending deprecation

# Cause 3: Old-style patterns
class OldStyle:
    """Using old-style class patterns."""
    pass

# Cause 4: Deprecated usage patterns
import re
pattern = re.compile(r"\d+")  # Some regex patterns may trigger warnings

# Cause 5: Using soon-to-be-deprecated parameters
def process(data, legacy_mode=False):
    if legacy_mode:
        warnings.warn(
            "legacy_mode parameter will be deprecated",
            PendingDeprecationWarning
        )
    return data
```

## Solutions

### Fix 1: Migrate to new APIs proactively

```python
# Wrong — using deprecated function
def process_data():
    import imp  # Will be deprecated
    return imp.find_module("json")

# Correct — use modern alternative now
def process_data():
    import importlib
    return importlib.find_loader("json")
```

### Fix 2: Suppress PendingDeprecationWarnings

```python
import warnings

# Wrong — warnings may clutter output
result = old_api()

# Correct — suppress in specific contexts
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=PendingDeprecationWarning)
    result = old_api()  # No warning shown
```

### Fix 3: Show PendingDeprecationWarnings for proactive migration

```python
import warnings

# Correct — show all warnings to catch pending deprecations early
warnings.filterwarnings("always", category=PendingDeprecationWarning)

# Or use command line flag
# python -W all::PendingDeprecationWarning myscript.py
```

### Fix 4: Create compatibility wrapper

```python
import warnings
import sys

# Wrong — code breaks when function is actually deprecated
result = old_function()

# Correct — compatibility wrapper
def compatible_function(*args, **kwargs):
    if sys.version_info >= (3, 12):
        warnings.warn(
            "old_function is deprecated, use new_function",
            PendingDeprecationWarning
        )
    return new_function(*args, **kwargs)
```

### Fix 5: Check Python version before using deprecated features

```python
import sys

# Wrong — assumes feature is available
result = deprecated_feature()

# Correct — version-aware code
if sys.version_info < (3, 12):
    result = deprecated_feature()
else:
    result = new_feature()
```

## Related Errors

- [DeprecationWarning](../deprecationwarning) — feature is officially deprecated.
- [FutureWarning](../futurewarning) — changes in future Python versions.
- [ImportWarning](../importwarning) — import-related issues.
