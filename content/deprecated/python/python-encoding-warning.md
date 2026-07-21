---
title: "[Solution] Deprecated Function Migration: open() without encoding to open with explicit encoding"
description: "Migrate from deprecated open() without encoding to explicit encoding in Python 3.10+."
deprecated_function: "open('file.txt')"
replacement_function: "open('file.txt', encoding='utf-8')"
languages: ["python"]
deprecated_since: "Python 3.10"
---

# [Solution] Deprecated Function Migration: open() without encoding to open with explicit encoding

The `open('file.txt')` has been deprecated in favor of `open('file.txt', encoding='utf-8')`.

## Migration Guide

Python 3.10+ emits DeprecationWarning when opening text files without explicit encoding.

## Before (Deprecated)

```python
with open("data.txt") as f:
    data = f.read()

with open("output.txt", "w") as f:
    f.write("hello")
```

## After (Modern)

```python
with open("data.txt", encoding="utf-8") as f:
    data = f.read()

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

## Key Differences

- Always specify encoding for text files
- Python 3.10+ warns without encoding
- Prevents platform-dependent behavior
