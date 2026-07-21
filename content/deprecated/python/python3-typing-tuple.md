---
title: "[Solution] Deprecated Function Migration: typing.Tuple to tuple"
description: "Migrate from deprecated typing.Tuple to built-in tuple."
deprecated_function: "typing.Tuple[int, str]"
replacement_function: "tuple[int, str]"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.Tuple to tuple

The `typing.Tuple[int, str]` has been deprecated in favor of `tuple[int, str]`.

## Migration Guide

Built-in generics are more natural.

## Before (Deprecated)

```python
from typing import Tuple
def func(x: Tuple[int, str]):
```

## After (Modern)

```python
def func(x: tuple[int, str]):
```

## Key Differences

- Built-in generics are more natural
