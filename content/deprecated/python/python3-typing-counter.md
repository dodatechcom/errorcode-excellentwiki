---
title: "[Solution] Deprecated Function Migration: typing.Counter to collections.Counter"
description: "Migrate from deprecated typing.Counter to collections.Counter."
deprecated_function: "typing.Counter[str]"
replacement_function: "collections.Counter[str]"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.Counter to collections.Counter

The `typing.Counter[str]` has been deprecated in favor of `collections.Counter[str]`.

## Migration Guide

Built-in generics are more natural.

## Before (Deprecated)

```python
from typing import Counter
def func(data: Counter[str]):
```

## After (Modern)

```python
from collections import Counter
def func(data: Counter[str]):
```

## Key Differences

- Built-in generics are more natural
