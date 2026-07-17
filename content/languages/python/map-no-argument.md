---
title: "[Solution] Python TypeError — map() Missing Required Argument"
description: "Fix Python TypeError: map() missing required argument when calling map without proper arguments. Learn correct map() usage and alternatives."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# TypeError — map() Missing Required Argument

A `TypeError` with the message "map() missing required argument" is raised when you call `map()` without providing the required function and iterable arguments. `map()` requires at least two arguments: a function and one or more iterables.

## Description

The `map()` function applies a given function to each item of an iterable. Its signature is `map(function, iterable, ...)`. You must provide at least a function and one iterable. Forgetting either argument, or passing `None` as the function, causes a `TypeError`.

Common patterns:

- **No arguments** — `map()`.
- **Only function, no iterable** — `map(func)`.
- **Only iterable, no function** — `map(None, [1, 2, 3])`.
- **Wrong argument order** — `map([1, 2, 3], str)`.

## Common Causes

```python
# Cause 1: No arguments
result = map()  # TypeError: map() missing required argument 'function'

# Cause 2: Only function, no iterable
result = map(str)  # TypeError: map() missing required argument 'iterable'

# Cause 3: None as function (Python 2 behavior, fails in Python 3)
result = map(None, [1, 2, 3])  # TypeError in Python 3

# Cause 4: Wrong argument order
result = map([1, 2, 3], str)  # TypeError — first arg must be callable
```

## Solutions

### Fix 1: Provide both function and iterable

```python
# Wrong
result = map()  # TypeError
result = map(str)  # TypeError

# Correct
result = map(str, [1, 2, 3])
print(list(result))  # ['1', '2', '3']
```

### Fix 2: Use the correct argument order

```python
# Wrong
result = map([1, 2, 3], str)  # TypeError

# Correct — function first, iterable second
result = map(str, [1, 2, 3])
print(list(result))  # ['1', '2', '3']
```

### Fix 3: Use a lambda for simple operations

```python
# Wrong
result = map()  # No arguments

# Correct — use lambda
result = map(lambda x: x * 2, [1, 2, 3])
print(list(result))  # [2, 4, 6]
```

### Fix 4: Use list comprehension instead of map

```python
# Wrong — map with no arguments
result = map()

# Correct — list comprehension
numbers = [1, 2, 3]
result = [x * 2 for x in numbers]
print(result)  # [2, 4, 6]

# Or use map correctly
result = list(map(lambda x: x * 2, numbers))
```

## Related Errors

- [TypeError](../typeerror) — general type mismatch errors.
- [Object not iterable](object-not-iterable) — non-iterable argument.
- [Next missing argument](next-no-argument) — similar missing argument issue.
