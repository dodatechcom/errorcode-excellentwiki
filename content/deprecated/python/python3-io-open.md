---
title: "[Solution] Deprecated Function Migration: io.open to built-in open"
description: "Migrate from deprecated io.open to built-in open in Python 3."
deprecated_function: "io.open(file)"
replacement_function: "open(file)"
languages: ["python"]
deprecated_since: "Python 3.0+"
---

# [Solution] Deprecated Function Migration: io.open to built-in open

The `io.open(file)` has been deprecated in favor of `open(file)`.

## Migration Guide

Built-in open supports encoding by default

io.open was needed in Python 2. In Python 3, built-in open handles encoding.

## Before (Deprecated)

```python
import io
with io.open("data.txt", encoding="utf-8") as f:
    data = f.read()
```

## After (Modern)

```python
with open("data.txt", encoding="utf-8") as f:
    data = f.read()
```

## Key Differences

- Built-in open is equivalent
- No need for io.open in Python 3
- Both accept encoding parameter
- Use built-in open for new code
