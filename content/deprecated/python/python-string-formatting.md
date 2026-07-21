---
title: "[Solution] Deprecated Function Migration: % formatting to f-strings"
description: "Migrate from deprecated % string formatting to f-strings in Python."
deprecated_function: "%s %d % ()"
replacement_function: "f{name} {age}"
languages: ["python"]
deprecated_since: "Python 3.6+"
---

# [Solution] Deprecated Function Migration: % formatting to f-strings

The `"%s %d" % (name, age)` has been deprecated in favor of `f"{name} {age}"`.

## Migration Guide

f-strings (Python 3.6+) are faster, more readable, and support expressions.

## Before (Deprecated)

```python
name = "Alice"
age = 30
greeting = "Hello, %s! You are %d years old." % (name, age)
```

## After (Modern)

```python
name = "Alice"
age = 30
greeting = f"Hello, {name}! You are {age} years old."

# Expressions
result = f"{'adult' if age >= 18 else 'minor'}"
pi = 3.14159
formatted = f"Pi is {pi:.2f}"
```

## Key Differences

- f-strings are 2-3x faster than % formatting
- Support expressions inside {}
- Support format specs ({:.2f})
