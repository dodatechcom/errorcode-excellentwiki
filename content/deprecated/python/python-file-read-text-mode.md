---
title: "[Solution] Deprecated Function Migration: text mode file reading to explicit encoding"
description: "Migrate from deprecated implicit encoding to explicit encoding parameter in Python file operations."
deprecated_function: "open(file) for text"
replacement_function: "open(file, encoding='utf-8')"
languages: ["python"]
deprecated_since: "Python 3.0+"
---

# [Solution] Deprecated Function Migration: text mode file reading to explicit encoding

The `open(file) for text` has been deprecated in favor of `open(file, encoding='utf-8')`.

## Migration Guide

In Python 3, always specify encoding when opening text files to avoid platform-dependent defaults.

## Before (Deprecated)

```python
# Platform-dependent encoding
f = open("data.txt")
data = f.read()
```

## After (Modern)

```python
# Explicit encoding
with open("data.txt", encoding="utf-8") as f:
    data = f.read()

# Or use errors parameter
with open("data.txt", encoding="utf-8", errors="replace") as f:
    data = f.read()
```

## Key Differences

- Always specify encoding for text files
- Use errors parameter for handling bad encoding
- Python 3.10+ warns about missing encoding
