---
title: "[Solution] Deprecated Function Migration: typing.Generator to collections.abc.Generator"
description: "Migrate from deprecated typing.Generator to collections.abc.Generator."
deprecated_function: "typing.Generator"
replacement_function: "collections.abc.Generator"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.Generator to collections.abc.Generator

The `typing.Generator` has been deprecated in favor of `collections.abc.Generator`.

## Migration Guide

collections.abc is the standard.

## Before (Deprecated)

```python
from typing import Generator
def func() -> Generator[int, None, None]:
```

## After (Modern)

```python
from collections.abc import Generator
def func() -> Generator[int, None, None]:
```

## Key Differences

- collections.abc is the standard
