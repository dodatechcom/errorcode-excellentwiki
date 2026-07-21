---
title: "[Solution] Deprecated Function Migration: configparser.readfp to configparser.read_file"
description: "Migrate from deprecated configparser.readfp() to configparser.read_file()."
deprecated_function: "configparser.readfp()"
replacement_function: "configparser.read_file()"
languages: ["python"]
deprecated_since: "Python 3.2"
---

# [Solution] Deprecated Function Migration: configparser.readfp to configparser.read_file

The `configparser.readfp()` has been deprecated in favor of `configparser.read_file()`.

## Migration Guide

read_file accepts any file-like object

readfp was deprecated in Python 3.2. read_file is the modern replacement.

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

- read_file takes a file object
- Use with statement for proper closing
- More explicit about what it expects
