---
title: "[Solution] Deprecated Function Migration: typing.OrderedDict to collections.OrderedDict"
description: "Migrate from deprecated typing.OrderedDict to collections.OrderedDict."
deprecated_function: "typing.OrderedDict[str, int]"
replacement_function: "collections.OrderedDict[str, int]"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.OrderedDict to collections.OrderedDict

The `typing.OrderedDict[str, int]` has been deprecated in favor of `collections.OrderedDict[str, int]`.

## Migration Guide

Built-in generics are more natural.

## Before (Deprecated)

```python
from typing import OrderedDict
def func(data: OrderedDict[str, int]):
```

## After (Modern)

```python
from collections import OrderedDict
def func(data: OrderedDict[str, int]):
```

## Key Differences

- Built-in generics are more natural
