---
title: "[Solution] Deprecated Function Migration: raw_input() to input()"
description: "Migrate from Python 2 raw_input() to the input() function in Python 3."
deprecated_function: "raw_input()"
replacement_function: "input()"
languages: ["python"]
deprecated_since: "Python 3.0"
---

# [Solution] Deprecated Function Migration: raw_input() to input()

The `raw_input()` has been deprecated in favor of `input()`.

## Migration Guide

In Python 2, raw_input() reads a string. In Python 3, raw_input() was renamed to input().

## Before (Deprecated)

```python
# Python 2
name = raw_input("Enter name: ")
age = raw_input("Enter age: ")
```

## After (Modern)

```python
# Python 3
name = input("Enter name: ")
age = input("Enter age: ")
```

## Key Differences

- Simple rename -- no behavior change
- Use 2to3 -f input for conversion
