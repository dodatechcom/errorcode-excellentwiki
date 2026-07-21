---
title: "[Solution] Deprecated Function Migration: typing.Deque to collections.deque"
description: "Migrate from deprecated typing.Deque to collections.deque."
deprecated_function: "typing.Deque[int]"
replacement_function: "collections.deque[int]"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.Deque to collections.deque

The `typing.Deque[int]` has been deprecated in favor of `collections.deque[int]`.

## Migration Guide

Built-in generics are more natural.

## Before (Deprecated)

```python
from typing import Deque
def func(items: Deque[int]):
```

## After (Modern)

```python
from collections import deque
def func(items: deque[int]):
```

## Key Differences

- Built-in generics are more natural
