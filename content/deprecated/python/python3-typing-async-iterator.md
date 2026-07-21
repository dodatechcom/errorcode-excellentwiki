---
title: "[Solution] Deprecated Function Migration: typing.AsyncIterator to collections.abc.AsyncIterator"
description: "Migrate from deprecated typing.AsyncIterator to collections.abc.AsyncIterator."
deprecated_function: "typing.AsyncIterator"
replacement_function: "collections.abc.AsyncIterator"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.AsyncIterator to collections.abc.AsyncIterator

The `typing.AsyncIterator` has been deprecated in favor of `collections.abc.AsyncIterator`.

## Migration Guide

collections.abc is the standard.

## Before (Deprecated)

```python
from typing import AsyncIterator
def func() -> AsyncIterator[int]:
```

## After (Modern)

```python
from collections.abc import AsyncIterator
def func() -> AsyncIterator[int]:
```

## Key Differences

- collections.abc is the standard
