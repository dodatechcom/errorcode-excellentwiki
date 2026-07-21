---
title: "[Solution] Deprecated Function Migration: typing.Set to set"
description: "Migrate from deprecated typing.Set to built-in set."
deprecated_function: "typing.Set[int]"
replacement_function: "set[int]"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.Set to set

The `typing.Set[int]` has been deprecated in favor of `set[int]`.

## Migration Guide

Built-in generics are more natural.

## Before (Deprecated)

```python
from typing import Set
def func(items: Set[int]):
```

## After (Modern)

```python
def func(items: set[int]):
```

## Key Differences

- Built-in generics are more natural
