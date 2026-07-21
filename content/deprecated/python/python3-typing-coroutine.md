---
title: "[Solution] Deprecated Function Migration: typing.Coroutine to collections.abc.Coroutine"
description: "Migrate from deprecated typing.Coroutine to collections.abc.Coroutine."
deprecated_function: "typing.Coroutine"
replacement_function: "collections.abc.Coroutine"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.Coroutine to collections.abc.Coroutine

The `typing.Coroutine` has been deprecated in favor of `collections.abc.Coroutine`.

## Migration Guide

collections.abc is the standard.

## Before (Deprecated)

```python
from typing import Coroutine
def func() -> Coroutine[Any, None, int]:
```

## After (Modern)

```python
from collections.abc import Coroutine
def func() -> Coroutine[Any, None, int]:
```

## Key Differences

- collections.abc is the standard
