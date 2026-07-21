---
title: "[Solution] Deprecated Function Migration: Python 2 print statement to print()"
description: "Migrate from Python 2 print statement to the print() function for Python 3 compatibility."
deprecated_function: "print statement"
replacement_function: "print() function"
languages: ["python"]
deprecated_since: "Python 3.0"
---

# [Solution] Deprecated Function Migration: Python 2 print statement to print()

The `print statement` has been deprecated in favor of `print() function`.

## Migration Guide

In Python 2, print is a statement. In Python 3, it is a function requiring parentheses (PEP 3105).

## Before (Deprecated)

```python
print "Hello, World!"
print "Name:", name
print "Value:", x,
print >> sys.stderr, "Error"
```

## After (Modern)

```python
print("Hello, World!")
print("Name:", name)
print("Value:", x, end=" ")
print("Error", file=sys.stderr)
```

## Key Differences

- Add parentheses around all print arguments
- Use end= instead of trailing comma
- Use file= instead of >> syntax
