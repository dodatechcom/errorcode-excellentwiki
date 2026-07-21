---
title: "[Solution] Deprecated Function Migration: unicode() to str() in Python 3"
description: "Migrate from Python 2 unicode() function to str() in Python 3 where strings are Unicode by default."
deprecated_function: "unicode()"
replacement_function: "str()"
languages: ["python"]
deprecated_since: "Python 3.0"
---

# [Solution] Deprecated Function Migration: unicode() to str() in Python 3

The `unicode()` has been deprecated in favor of `str()`.

## Migration Guide

In Python 2, str is bytes and unicode is text. In Python 3, str is always Unicode text and unicode() was removed.

## Before (Deprecated)

```python
# Python 2
name = unicode("Alice")
text = u"Hello, World!"
```

## After (Modern)

```python
# Python 3
name = str("Alice")
text = "Hello, World!"
encoded = text.encode("utf-8")
```

## Key Differences

- Replace unicode(x) with str(x)
- Remove u prefix from string literals
- Use bytes for raw byte data
