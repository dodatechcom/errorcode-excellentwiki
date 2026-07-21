---
title: "[Solution] Deprecated Function Migration: dist-packages to site-packages"
description: "Migrate from deprecated dist-packages to site-packages."
deprecated_function: "dist-packages"
replacement_function: "site-packages"
languages: ["python"]
deprecated_since: "Python 3.0+"
---

# [Solution] Deprecated Function Migration: dist-packages to site-packages

The `dist-packages` has been deprecated in favor of `site-packages`.

## Migration Guide

site-packages is the standard.

## Before (Deprecated)

```python
pip install --target=dist-packages pkg
```

## After (Modern)

```python
pip install pkg
```

## Key Differences

- site-packages is the standard
