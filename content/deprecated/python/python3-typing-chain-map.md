---
title: "[Solution] Deprecated Function Migration: typing.ChainMap to collections.ChainMap"
description: "Migrate from deprecated typing.ChainMap to collections.ChainMap."
deprecated_function: "typing.ChainMap[str, int]"
replacement_function: "collections.ChainMap[str, int]"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.ChainMap to collections.ChainMap

The `typing.ChainMap[str, int]` has been deprecated in favor of `collections.ChainMap[str, int]`.

## Migration Guide

Built-in generics are more natural.

## Before (Deprecated)

```python
from typing import ChainMap
def func(data: ChainMap[str, int]):
```

## After (Modern)

```python
from collections import ChainMap
def func(data: ChainMap[str, int]):
```

## Key Differences

- Built-in generics are more natural
