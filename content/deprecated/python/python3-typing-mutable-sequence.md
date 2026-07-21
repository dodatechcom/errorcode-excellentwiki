---
title: "[Solution] Deprecated Function Migration: typing.MutableSequence to collections.abc.MutableSequence"
description: "Migrate from deprecated typing.MutableSequence to collections.abc.MutableSequence."
deprecated_function: "typing.MutableSequence"
replacement_function: "collections.abc.MutableSequence"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.MutableSequence to collections.abc.MutableSequence

The `typing.MutableSequence` has been deprecated in favor of `collections.abc.MutableSequence`.

## Migration Guide

collections.abc is the standard.

## Before (Deprecated)

```python
from typing import MutableSequence
def func(data: MutableSequence[int]):
```

## After (Modern)

```python
from collections.abc import MutableSequence
def func(data: MutableSequence[int]):
```

## Key Differences

- collections.abc is the standard
