---
title: "[Solution] Deprecated Function Migration: open without encoding to explicit encoding"
description: "Migrate from deprecated open() without encoding to explicit encoding."
deprecated_function: "open('file.txt')"
replacement_function: "open('file.txt', encoding='utf-8')"
languages: ["python"]
deprecated_since: "Python 3.10+"
---

# [Solution] Deprecated Function Migration: open without encoding to explicit encoding

The `open('file.txt')` has been deprecated in favor of `open('file.txt', encoding='utf-8')`.

## Migration Guide

Python 3.10+ warns about missing encoding.

## Before (Deprecated)

```python
with open("data.txt") as f:
    data = f.read()
```

## After (Modern)

```python
with open("data.txt", encoding="utf-8") as f:
    data = f.read()
```

## Key Differences

- Always specify encoding for text files
