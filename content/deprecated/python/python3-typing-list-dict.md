---
title: "[Solution] Deprecated Function Migration: typing.List to list"
description: "Migrate from deprecated typing.List to built-in list."
deprecated_function: "typing.List[int]"
replacement_function: "list[int]"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.List to list

The `typing.List[int]` has been deprecated in favor of `list[int]`.

## Migration Guide

Built-in generics are more natural.

## Before (Deprecated)

```python
from typing import List
def func(items: List[int]) -> List[str]:
```

## After (Modern)

```python
def func(items: list[int]) -> list[str]:
```

## Key Differences

- Built-in generics are more natural
