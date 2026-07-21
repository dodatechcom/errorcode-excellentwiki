---
title: "[Solution] Deprecated Function Migration: Optional[X] to X | None"
description: "Migrate from deprecated Optional[X] to X | None union type."
deprecated_function: "Optional[X]"
replacement_function: "X | None"
languages: ["python"]
deprecated_since: "Python 3.10+"
---

# [Solution] Deprecated Function Migration: Optional[X] to X | None

The `Optional[X]` has been deprecated in favor of `X | None`.

## Migration Guide

Union syntax is more concise.

## Before (Deprecated)

```python
from typing import Optional
def func(x: Optional[int]) -> Optional[str]:
```

## After (Modern)

```python
def func(x: int | None) -> str | None:
```

## Key Differences

- Union syntax is more concise
