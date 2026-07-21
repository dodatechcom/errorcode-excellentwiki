---
title: "[Solution] Deprecated Function Migration: typing.Optional to X | None"
description: "Migrate from deprecated typing.Optional to X | None union syntax."
deprecated_function: "Optional[str]"
replacement_function: "str | None"
languages: ["python"]
deprecated_since: "Python 3.10+"
---

# [Solution] Deprecated Function Migration: typing.Optional to X | None

The `Optional[str]` has been deprecated in favor of `str | None`.

## Migration Guide

| union syntax is more readable

typing.Optional[X] is equivalent to X | None.

## Before (Deprecated)

```python
from typing import Optional
def greet(name: Optional[str]) -> Optional[str]:
    pass
```

## After (Modern)

```python
def greet(name: str | None) -> str | None:
    pass
```

## Key Differences

- str | None is equivalent to Optional[str]
- Union syntax since Python 3.10
- typing.Optional still works
- For Python < 3.10, use typing.Optional
