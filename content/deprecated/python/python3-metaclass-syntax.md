---
title: "[Solution] Deprecated Function Migration: __metaclass__ to metaclass= parameter"
description: "Migrate from deprecated __metaclass__ to metaclass= class parameter."
deprecated_function: "__metaclass__ = Meta"
replacement_function: "class Foo(metaclass=Meta):"
languages: ["python"]
deprecated_since: "Python 3.0+"
---

# [Solution] Deprecated Function Migration: __metaclass__ to metaclass= parameter

The `__metaclass__ = Meta` has been deprecated in favor of `class Foo(metaclass=Meta):`.

## Migration Guide

metaclass= parameter is the standard syntax

The __metaclass__ attribute was removed in Python 3.

## Before (Deprecated)

```python
class MyMeta(type): pass
class MyClass:
    __metaclass__ = MyMeta
```

## After (Modern)

```python
class MyMeta(type): pass
class MyClass(metaclass=MyMeta):
    pass
```

## Key Differences

- metaclass= is the Python 3 syntax
- __metaclass__ attribute was removed
- Same functionality
- Use 2to3 for automatic conversion
