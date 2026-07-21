---
title: "[Solution] Deprecated Function Migration: Python 2 string encode/decode patterns"
description: "Migrate Python 2 string encoding patterns to Python 3 bytes and str separation."
deprecated_function: "str.encode()/unicode.encode()"
replacement_function: "str.encode() for bytes, str stays str"
languages: ["python"]
deprecated_since: "Python 3.0"
---

# [Solution] Deprecated Function Migration: Python 2 string encode/decode patterns

The `str.encode()/unicode.encode()` has been deprecated in favor of `str.encode() for bytes, str stays str`.

## Migration Guide

In Python 2, str is bytes and unicode is text. In Python 3, str is always text and bytes is separate.

## Before (Deprecated)

```python
# Python 2
text = u"Hello"
encoded = text.encode("utf-8")
raw = "bytes here"
converted = raw.decode("latin-1")
```

## After (Modern)

```python
# Python 3
text = "Hello"
encoded = text.encode("utf-8")  # bytes
decoded = encoded.decode("utf-8")  # str
raw = b"bytes here"
converted = raw.decode("latin-1")
```

## Key Differences

- str is always text in Python 3
- bytes is for raw binary data
- Use b prefix for byte literals
