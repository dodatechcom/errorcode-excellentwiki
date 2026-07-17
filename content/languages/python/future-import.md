---
title: "[Solution] Python SyntaxError — from __future__ Must Be First"
description: "Fix Python SyntaxError when __future__ import is not at the top of the file. Learn the rules for __future__ imports and how to place them correctly."
languages: ["python"]
severities: ["error"]
error_types: ["syntax"]
weight: 5
---

# SyntaxError — from __future__ Must Be First

A `SyntaxError` with the message "from __future__ imports must occur at the beginning of the file" is raised when a `from __future__ import` statement appears after other code. These imports must be the first non-comment, non-docstring statement in the file.

## Description

`from __future__ import` statements enable features from future Python versions. They must appear at the very beginning of the file, before any other code (except comments, docstrings, and blank lines). This is because they affect how Python parses the rest of the file.

Common patterns:

- **Import after code** — `print("hello")` before `from __future__ import annotations`.
- **Import after other imports** — regular imports before `__future__` imports.
- **Import inside function** — `from __future__ import` inside a function body.
- **Import after string** — module docstring before `__future__` import.

## Common Causes

```python
# Cause 1: Import after code
print("hello")
from __future__ import annotations  # SyntaxError

# Cause 2: Import after other imports
import os
from __future__ import annotations  # SyntaxError

# Cause 3: Import inside function
def func():
    from __future__ import annotations  # SyntaxError

# Cause 4: Import after docstring
"""Module docstring."""
from __future__ import annotations  # SyntaxError
```

## Solutions

### Fix 1: Place __future__ import at the very beginning

```python
# Wrong
import os
from __future__ import annotations

# Correct
from __future__ import annotations
import os
```

### Fix 2: Place before docstring or after it in specific position

```python
# Wrong
"""Module docstring."""
from __future__ import annotations  # SyntaxError

# Correct — __future__ import before docstring
from __future__ import annotations
"""Module docstring."""
```

### Fix 3: Don't use __future__ imports inside functions

```python
# Wrong
def func():
    from __future__ import annotations  # SyntaxError

# Correct — at module level
from __future__ import annotations

def func():
    pass
```

### Fix 4: Use multiple __future__ imports together

```python
# Wrong
from __future__ import annotations
import os
from __future__ import generators  # SyntaxError — second __future__ import

# Correct — all __future__ imports together at the top
from __future__ import annotations, generators
import os
```

## Related Errors

- [SyntaxError](../syntaxerror) — general syntax errors.
- [ImportError](../importerror) — import-related errors.
- [SyntaxWarning](../syntaxwarning) — syntax-related warnings.
