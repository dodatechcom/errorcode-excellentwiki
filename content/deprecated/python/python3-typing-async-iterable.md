---
title: "[Solution] Deprecated Function Migration: typing.AsyncIterable to collections.abc.AsyncIterable"
description: "Migrate from deprecated typing.AsyncIterable to collections.abc.AsyncIterable."
deprecated_function: "typing.AsyncIterable"
replacement_function: "collections.abc.AsyncIterable"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.AsyncIterable to collections.abc.AsyncIterable

The `typing.AsyncIterable` has been deprecated in favor of `collections.abc.AsyncIterable`.

## Migration Guide

collections.abc is the standard.

## Before (Deprecated)

```python
from typing import AsyncIterable
def func(items: AsyncIterable[int]):
```

## After (Modern)

```python
from collections.abc import AsyncIterable
def func(items: AsyncIterable[int]):
```

## Key Differences

- collections.abc is the standard
