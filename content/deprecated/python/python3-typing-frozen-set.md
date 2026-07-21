---
title: "[Solution] Deprecated Function Migration: typing.FrozenSet to frozenset"
description: "Migrate from deprecated typing.FrozenSet to built-in frozenset."
deprecated_function: "typing.FrozenSet[int]"
replacement_function: "frozenset[int]"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.FrozenSet to frozenset

The `typing.FrozenSet[int]` has been deprecated in favor of `frozenset[int]`.

## Migration Guide

Built-in generics are more natural.

## Before (Deprecated)

```python
from typing import FrozenSet
def func(items: FrozenSet[int]):
```

## After (Modern)

```python
def func(items: frozenset[int]):
```

## Key Differences

- Built-in generics are more natural
