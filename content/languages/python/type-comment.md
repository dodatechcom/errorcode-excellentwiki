---
title: "[Solution] Python SyntaxError — Invalid Type Comment"
description: "Fix Python SyntaxError caused by invalid type comments. Learn about type comments in Python and how to write them correctly."
languages: ["python"]
severities: ["error"]
error_types: ["syntax"]
tags: ["syntaxerror", "type", "comment", "annotation", "typing"]
weight: 5
---

# SyntaxError — Invalid Type Comment

A `SyntaxError` with the message "invalid type comment" is raised when a type comment is malformed. Type comments are special comments that provide type annotations for variables and function signatures, typically used with tools like mypy.

## Description

Type comments are a way to add type information to Python code using comments. They follow the format `# type: <type>` for variables and `# type: (<args>) -> <return>` for functions. Invalid syntax in these comments causes `SyntaxError`. Modern Python prefers inline annotations over type comments.

Common patterns:

- **Malformed type comment** — `# type: int str` (too many types).
- **Wrong function type comment** — `# type: (int, str) ->` (missing return type).
- **Invalid type syntax** — using unsupported type syntax in comment.
- **Type comment in wrong position** — not on the same line as the assignment.

## Common Causes

```python
# Cause 1: Invalid type syntax
x = 5  # type: invalid type  # SyntaxError

# Cause 2: Wrong function type comment
def func(x, y):
    # type: (int, str) ->  # SyntaxError — missing return type
    return str(x) + y

# Cause 3: Type comment on wrong line
x = 5
# type: int  # SyntaxError — must be on same line as assignment

# Cause 4: Invalid generic syntax in type comment
from typing import List
items = []  # type: List<int>  # SyntaxError — should be List[int]
```

## Solutions

### Fix 1: Use correct type comment syntax

```python
# Wrong
x = 5  # type: invalid type  # SyntaxError

# Correct
x = 5  # type: int
```

### Fix 2: Complete function type comments

```python
# Wrong
def func(x, y):
    # type: (int, str) ->  # SyntaxError
    return str(x) + y

# Correct
def func(x, y):
    # type: (int, str) -> str
    return str(x) + y
```

### Fix 3: Place type comment on same line

```python
# Wrong
x = 5
# type: int  # SyntaxError

# Correct
x = 5  # type: int
```

### Fix 4: Use inline annotations instead (Python 3.5+)

```python
# Old style — type comments
def func(x, y):
    # type: (int, str) -> str
    return str(x) + y

# Modern style — inline annotations
def func(x: int, y: str) -> str:
    return str(x) + y

# Variable annotations (Python 3.6+)
x: int = 5
items: list[int] = []
```

### Fix 5: Use typing module for complex types

```python
from typing import List, Dict, Optional

# Wrong — using angle brackets in type comment
items = []  # type: List<int>  # SyntaxError

# Correct
items = []  # type: List[int]

# Or modern syntax
items: List[int] = []
```

## Related Errors

- [SyntaxError](../syntaxerror) — general syntax errors.
- [SyntaxWarning](../syntaxwarning) — syntax-related warnings.
- [Future import](future-import) — __future__ import issues.
