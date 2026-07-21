---
title: "[Solution] Deprecated Function Migration: typing.Type to type"
description: "Migrate from deprecated typing.Type to built-in type."
deprecated_function: "typing.Type[int]"
replacement_function: "type[int]"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.Type to type

The `typing.Type[int]` has been deprecated in favor of `type[int]`.

## Migration Guide

Built-in generics are more natural.

## Before (Deprecated)

```python
from typing import Type
def func(cls: Type[int]):
```

## After (Modern)

```python
def func(cls: type[int]):
```

## Key Differences

- Built-in generics are more natural
