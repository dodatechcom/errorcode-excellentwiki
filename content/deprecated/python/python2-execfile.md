---
title: "[Solution] Deprecated Function Migration: execfile() to exec(open().read())"
description: "Migrate from Python 2 execfile() to exec with open and read for file execution in Python 3."
deprecated_function: "execfile()"
replacement_function: "exec(open().read())"
languages: ["python"]
deprecated_since: "Python 3.0"
---

# [Solution] Deprecated Function Migration: execfile() to exec(open().read())

The `execfile()` has been deprecated in favor of `exec(open().read())`.

## Migration Guide

execfile() was removed in Python 3. Use exec with open and read, or use importlib for module imports.

## Before (Deprecated)

```python
# Python 2
execfile("script.py")
execfile("config.py", {"env": "production"})
```

## After (Modern)

```python
exec(open("script.py").read())

with open("config.py") as f:
    exec(f.read(), {"env": "production"})
```

## Key Differences

- execfile(file) becomes exec(open(file).read())
- Use importlib for module imports
- Use with statement to close files
