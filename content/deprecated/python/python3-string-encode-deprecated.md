---
title: "[Solution] Deprecated Function Migration: str.encode ascii to str.encode utf-8"
description: "Migrate from deprecated ASCII encoding to UTF-8."
deprecated_function: "str.encode('ascii')"
replacement_function: "str.encode('utf-8')"
languages: ["python"]
deprecated_since: "Python 3.0+"
---

# [Solution] Deprecated Function Migration: str.encode ascii to str.encode utf-8

The `str.encode('ascii')` has been deprecated in favor of `str.encode('utf-8')`.

## Migration Guide

UTF-8 is the modern standard.

## Before (Deprecated)

```python
text.encode('ascii')
```

## After (Modern)

```python
text.encode('utf-8')
```

## Key Differences

- UTF-8 handles all Unicode
