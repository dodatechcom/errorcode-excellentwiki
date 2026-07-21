---
title: "[Solution] Deprecated Function Migration: typing.MutableMapping to collections.abc.MutableMapping"
description: "Migrate from deprecated typing.MutableMapping to collections.abc.MutableMapping."
deprecated_function: "typing.MutableMapping"
replacement_function: "collections.abc.MutableMapping"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.MutableMapping to collections.abc.MutableMapping

The `typing.MutableMapping` has been deprecated in favor of `collections.abc.MutableMapping`.

## Migration Guide

collections.abc is the standard.

## Before (Deprecated)

```python
from typing import MutableMapping
def func(data: MutableMapping[str, int]):
```

## After (Modern)

```python
from collections.abc import MutableMapping
def func(data: MutableMapping[str, int]):
```

## Key Differences

- collections.abc is the standard
