---
title: "[Solution] Deprecated Function Migration: exec statement to exec() function"
description: "Migrate from Python 2 exec statement to the exec() function in Python 3."
deprecated_function: "exec code"
replacement_function: "exec(code)"
languages: ["python"]
deprecated_since: "Python 3.0"
---

# [Solution] Deprecated Function Migration: exec statement to exec() function

The `exec code` has been deprecated in favor of `exec(code)`.

## Migration Guide

In Python 2, exec is a statement. In Python 3, exec is a function requiring parentheses.

## Before (Deprecated)

```python
# Python 2
exec "print('hello')"
exec code
```

## After (Modern)

```python
# Python 3
exec("print('hello')")
exec(code)
exec("x = 5", globals_dict, locals_dict)
```

## Key Differences

- Add parentheses around exec arguments
- exec is now a function, not a statement
