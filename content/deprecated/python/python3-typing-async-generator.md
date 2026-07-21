---
title: "[Solution] Deprecated Function Migration: typing.AsyncGenerator to collections.abc.AsyncGenerator"
description: "Migrate from deprecated typing.AsyncGenerator to collections.abc.AsyncGenerator."
deprecated_function: "typing.AsyncGenerator"
replacement_function: "collections.abc.AsyncGenerator"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.AsyncGenerator to collections.abc.AsyncGenerator

The `typing.AsyncGenerator` has been deprecated in favor of `collections.abc.AsyncGenerator`.

## Migration Guide

collections.abc is the standard.

## Before (Deprecated)

```python
from typing import AsyncGenerator
def func() -> AsyncGenerator[int, None]:
```

## After (Modern)

```python
from collections.abc import AsyncGenerator
def func() -> AsyncGenerator[int, None]:
```

## Key Differences

- collections.abc is the standard
