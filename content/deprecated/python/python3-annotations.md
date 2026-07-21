---
title: "[Solution] Deprecated Function Migration: type comments to Python 3 annotations"
description: "Migrate from deprecated Python 2 type comments to Python 3 function annotations."
deprecated_function: "# type: ignore comment"
replacement_function: "def func(x: int) -> str:"
languages: ["python"]
deprecated_since: "Python 3.0+"
---

# [Solution] Deprecated Function Migration: type comments to Python 3 annotations

The `# type: ignore comment` has been deprecated in favor of `def func(x: int) -> str:`.

## Migration Guide

Type comments are verbose; annotations are built into the language

Type comments (# type: int) were used before Python 3 annotations. Annotations are cleaner and supported by mypy/pyright.

## Before (Deprecated)

```python
# type: (int) -> str
def func(x):  # type: ignore
    pass
```

## After (Modern)

```python
def func(x: int) -> str:
    pass

def greet(name: str, age: int = 0) -> str:
    return f"Hello {name}, age {age}"
```

## Key Differences

- Annotations are native Python syntax
- Supported by mypy, pyright, pytype
- No special comments needed
- Available at runtime via __annotations__
