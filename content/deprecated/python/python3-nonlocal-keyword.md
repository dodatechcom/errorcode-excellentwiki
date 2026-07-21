---
title: "[Solution] Deprecated Function Migration: global to nonlocal for nested scopes"
description: "Migrate from deprecated global usage to nonlocal for nested function variable access."
deprecated_function: "global var"
replacement_function: "nonlocal var"
languages: ["python"]
deprecated_since: "Python 3.0+"
---

# [Solution] Deprecated Function Migration: global to nonlocal for nested scopes

The `global var` has been deprecated in favor of `nonlocal var`.

## Migration Guide

nonlocal targets enclosing function scope

global targets module scope. nonlocal targets the nearest enclosing function scope.

## Before (Deprecated)

```python
def outer():
    x = 10
    def inner():
        global x
        x = 20
```

## After (Modern)

```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
```

## Key Differences

- nonlocal for enclosing function scope
- global for module scope
- nonlocal was added in Python 3
- Use nonlocal for closures
