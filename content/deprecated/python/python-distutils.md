---
title: "[Solution] Deprecated Function Migration: distutils to setuptools"
description: "Migrate from deprecated distutils to setuptools for Python package building and distribution."
deprecated_function: "distutils"
replacement_function: "setuptools"
languages: ["python"]
deprecated_since: "Python 3.10+"
---

# [Solution] Deprecated Function Migration: distutils to setuptools

The `distutils` has been deprecated in favor of `setuptools`.

## Migration Guide

distutils has been deprecated since Python 3.10 and was removed in Python 3.12. Use setuptools instead.

## Before (Deprecated)

```python
from distutils.core import setup

setup(
    name="mypackage",
    version="1.0.0",
    packages=["mypackage"],
)
```

## After (Modern)

```python
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0.0",
    packages=find_packages(),
    python_requires=">=3.7",
)
```

## Key Differences

- Replace distutils imports with setuptools
- Use find_packages() to auto-discover packages
- Add python_requires for version constraints
