---
title: "[Solution] Python TypeError — zip_longest Issues"
description: "Fix Python TypeError related to itertools.zip_longest. Learn how zip_longest works and resolve common issues with it."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# TypeError — zip_longest Issues

A `TypeError` related to `itertools.zip_longest` is raised when you call it incorrectly, such as passing non-iterable arguments, using wrong keyword arguments, or misunderstanding its behavior. `zip_longest` is used to iterate over multiple iterables until the longest one is exhausted.

## Description

`itertools.zip_longest` takes multiple iterables and an optional `fillvalue` keyword argument. It continues until the longest iterable is exhausted, filling missing values with `fillvalue`. Errors occur when you pass non-iterables, use incorrect keyword arguments, or confuse it with `zip()`.

Common patterns:

- **Passing non-iterable** — `zip_longest(42, [1, 2, 3])`.
- **Wrong keyword argument** — `zip_longest([1, 2], fill="x")`.
- **Confusing zip with zip_longest** — `zip_longest` behavior differs from `zip`.
- **Missing import** — using `zip_longest` without importing `itertools`.

## Common Causes

```python
from itertools import zip_longest

# Cause 1: Non-iterable argument
result = list(zip_longest(42, [1, 2, 3]))  # TypeError: 'int' object is not iterable

# Cause 2: Wrong keyword argument
result = list(zip_longest([1, 2], fill="x"))  # TypeError: unexpected keyword argument 'fill'

# Cause 3: Missing import
result = list(zip_longest([1, 2], [3, 4]))  # NameError: name 'zip_longest' is not defined

# Cause 4: Using zip_longest without iterables
result = list(zip_longest())  # Returns empty list — but may confuse users
```

## Solutions

### Fix 1: Import itertools first

```python
# Wrong
result = list(zip_longest([1, 2], [3, 4]))  # NameError

# Correct
from itertools import zip_longest
result = list(zip_longest([1, 2], [3, 4]))
```

### Fix 2: Use the correct keyword argument

```python
from itertools import zip_longest

# Wrong
result = list(zip_longest([1, 2], fill="x"))  # TypeError

# Correct
result = list(zip_longest([1, 2], [3, 4], fillvalue="x"))
```

### Fix 3: Ensure all arguments are iterable

```python
from itertools import zip_longest

# Wrong
result = list(zip_longest(42, [1, 2, 3]))  # TypeError

# Correct
result = list(zip_longest([42], [1, 2, 3]))
```

### Fix 4: Use zip_longest for unequal-length iterables

```python
from itertools import zip_longest

# zip stops at shortest
list(zip([1, 2, 3], ["a", "b"]))  # [(1, 'a'), (2, 'b')]

# zip_longest continues to longest
list(zip_longest([1, 2, 3], ["a", "b"]))  # [(1, 'a'), (2, 'b'), (3, None)]

# With custom fill value
list(zip_longest([1, 2, 3], ["a", "b"], fillvalue="?"))  # [(1, 'a'), (2, 'b'), (3, '?')]
```

## Related Errors

- [TypeError](../typeerror) — general type mismatch errors.
- [Object not iterable](object-not-iterable) — non-iterable argument.
- [Iteration over non-sequence](iteration-over-non-sequence) — similar iteration errors.
