---
title: "[Solution] Deprecated Function Migration: configparser.readfp to configparser.read_file"
description: "Migrate from deprecated configparser.readfp() to configparser.read_file() in Python 3."
deprecated_function: "configparser.readfp()"
replacement_function: "configparser.read_file()"
languages: ["python"]
deprecated_since: "Python 3.2"
---

# [Solution] Deprecated Function Migration: configparser.readfp to configparser.read_file

The `configparser.readfp()` has been deprecated in favor of `configparser.read_file()`.

## Migration Guide

configparser.readfp() was deprecated in Python 3.2 in favor of read_file().

## Before (Deprecated)

```python
import configparser

config = configparser.ConfigParser()
config.readfp(open("config.ini"))
```

## After (Modern)

```python
import configparser

config = configparser.ConfigParser()
with open("config.ini") as f:
    config.read_file(f)
```

## Key Differences

- Use read_file with a file object
- Use with statement to close files
- read_file accepts any file-like object
