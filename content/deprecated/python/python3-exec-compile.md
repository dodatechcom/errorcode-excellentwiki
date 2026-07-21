---
title: "[Solution] Deprecated Function Migration: exec string to exec with compile"
description: "Migrate from deprecated exec(string) to exec with compile for better error reporting."
deprecated_function: "exec(string)"
replacement_function: "exec(compile(string, '<string>', 'exec'))"
languages: ["python"]
deprecated_since: "Python 3.0+"
---

# [Solution] Deprecated Function Migration: exec string to exec with compile

The `exec(string)` has been deprecated in favor of `exec(compile(string, '<string>', 'exec'))`.

## Migration Guide

compile provides better error messages with file/line info

exec with compile provides better error reporting.

## Before (Deprecated)

```python
code = "x = 1\nprint(x)"
exec(code)
```

## After (Modern)

```python
code = "x = 1\nprint(x)"
compiled = compile(code, '<dynamic>', 'exec')
exec(compiled)
```

## Key Differences

- compile provides source location for errors
- Better debugging with file/line info
- compile can be cached for repeated execution
- Use compile for dynamic code generation
