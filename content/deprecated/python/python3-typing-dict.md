---
title: "[Solution] Deprecated Function Migration: typing.Dict to dict"
description: "Migrate from deprecated typing.Dict to built-in dict for type hints."
deprecated_function: "typing.Dict[str, int]"
replacement_function: "dict[str, int]"
languages: ["python"]
deprecated_since: "Python 3.9+"
---

# [Solution] Deprecated Function Migration: typing.Dict to dict

The `typing.Dict[str, int]` has been deprecated in favor of `dict[str, int]`.

## Migration Guide

Built-in types support generic syntax since Python 3.9

typing.Dict was used before built-in types supported generics.

## Before (Deprecated)

```python
from typing import Dict
data: Dict[str, int] = {}
```

## After (Modern)

```python
data: dict[str, int] = {}
items: list[int] = [1, 2, 3]
```

## Key Differences

- dict/list/tuple are generic since Python 3.9
- | union syntax since Python 3.10
- typing.Dict still works but not preferred
- For Python < 3.9, keep using typing
