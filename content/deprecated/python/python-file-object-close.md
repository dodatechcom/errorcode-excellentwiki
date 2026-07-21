---
title: "[Solution] Deprecated Function Migration: manual file close to context manager"
description: "Migrate from manual file.close() to using with statement context managers in Python."
deprecated_function: "f = open(); ...; f.close()"
replacement_function: "with open() as f:"
languages: ["python"]
deprecated_since: "Python 2.5+"
---

# [Solution] Deprecated Function Migration: manual file close to context manager

The `f = open(); ...; f.close()` has been deprecated in favor of `with open() as f:`.

## Migration Guide

Using a with statement ensures the file is properly closed even if an exception occurs.

## Before (Deprecated)

```python
f = open("file.txt", "r")
try:
    data = f.read()
finally:
    f.close()
```

## After (Modern)

```python
with open("file.txt", "r") as f:
    data = f.read()

# Multiple files
with open("in.txt") as fin, open("out.txt", "w") as fout:
    fout.write(fin.read())
```

## Key Differences

- Use with statement for all file operations
- Files auto-close when block exits
- No need for try/finally
