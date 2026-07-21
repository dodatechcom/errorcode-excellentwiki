---
title: "[Solution] Deprecated Function Migration: typing.Iterator to collections.abc.Iterator"
description: "Migrate from deprecated typing.Iterator to collections.abc.Iterator."
deprecated_function: "typing.Iterator"
replacement_function: "collections.abc.Iterator"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.Iterator to collections.abc.Iterator

The `typing.Iterator` has been deprecated in favor of `collections.abc.Iterator`.

## Migration Guide

collections.abc is the standard.

## Before (Deprecated)

```python
from typing import Iterator
def func(items: Iterator[int]):
```

## After (Modern)

```python
from collections.abc import Iterator
def func(items: Iterator[int]):
```

## Key Differences

- collections.abc is the standard
