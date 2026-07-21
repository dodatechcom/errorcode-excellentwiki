---
title: "[Solution] Deprecated Function Migration: os.path to pathlib.Path"
description: "Migrate from deprecated os.path module to pathlib.Path for modern filesystem operations in Python."
deprecated_function: "os.path.exists()"
replacement_function: "pathlib.Path.exists()"
languages: ["python"]
deprecated_since: "Python 3.4+"
---

# [Solution] Deprecated Function Migration: os.path to pathlib.Path

The `os.path.exists()` has been deprecated in favor of `pathlib.Path.exists()`.

## Migration Guide

pathlib.Path provides an object-oriented interface to filesystem paths.

## Before (Deprecated)

```python
import os

path = os.path.join("dir", "file.txt")
exists = os.path.exists(path)
name = os.path.basename(path)
```

## After (Modern)

```python
from pathlib import Path

path = Path("dir") / "file.txt"
exists = path.exists()
name = path.name
ext = path.suffix
```

## Key Differences

- Use Path / operator instead of os.path.join
- Use path.suffix instead of splitext
- pathlib objects convert to str via str(path)
