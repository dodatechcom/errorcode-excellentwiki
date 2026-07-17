---
title: "[Solution] Python TypeError — 'bool' Object Is Not Iterable"
description: "Fix Python TypeError when trying to iterate over a boolean value. Learn why booleans are not iterable and how to handle this error."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# TypeError — 'bool' Object Is Not Iterable

A `TypeError` with the message "'bool' object is not iterable" is raised when you try to iterate over a boolean value using a `for` loop, `list()`, `sum()`, or other iteration constructs. Booleans are not iterable in Python.

## Description

In Python, `bool` is a subclass of `int`, with `True` equal to 1 and `False` equal to 0. However, booleans are not iterable. You cannot use `for x in True:` or `list(True)`. This error commonly occurs when a function returns a boolean instead of a list, or when a variable that should be a collection is unexpectedly a boolean.

Common patterns:

- **Iterating over a boolean** — `for x in True:`.
- **Using sum() on a boolean** — `sum(True)`.
- **Function returns bool instead of list** — `result = process(); for x in result:`.
- **Unpacking a boolean** — `a, b = True`.

## Common Causes

```python
# Cause 1: Iterating over a boolean
for x in True:
    print(x)  # TypeError: 'bool' object is not iterable

# Cause 2: Using sum() on a boolean
total = sum(True)  # TypeError: 'bool' object is not iterable

# Cause 3: Function returns bool instead of list
def process():
    return True  # Should return a list

result = process()
for item in result:  # TypeError
    print(item)

# Cause 4: Unpacking a boolean
a, b = True  # TypeError: cannot unpack non-iterable bool object
```

## Solutions

### Fix 1: Check if value is iterable before iterating

```python
value = True

# Wrong
for x in value:  # TypeError
    print(x)

# Correct
if hasattr(value, '__iter__'):
    for x in value:
        print(x)
else:
    print(f"Value {value} is not iterable")
```

### Fix 2: Convert boolean to appropriate type

```python
# Wrong
value = True
for x in value:  # TypeError
    print(x)

# Correct
value = True
if value:
    items = [1, 2, 3]  # Or whatever the collection should be
    for x in items:
        print(x)
```

### Fix 3: Fix function return type

```python
# Wrong
def process():
    return True  # Should be a list

result = process()
for item in result:  # TypeError
    print(item)

# Correct
def process():
    return [True, False, True]  # Return a list

result = process()
for item in result:
    print(item)
```

### Fix 4: Use isinstance() to check before iteration

```python
def process(data):
    if isinstance(data, bool):
        print(f"Got boolean: {data}")
        return
    if hasattr(data, '__iter__'):
        for item in data:
            print(item)

process(True)  # Prints "Got boolean: True"
process([1, 2, 3])  # Prints 1, 2, 3
```

## Related Errors

- [Object not iterable](object-not-iterable) — general non-iterable errors.
- [Iteration over non-sequence](iteration-over-non-sequence) — similar iteration errors.
- [TypeError](../typeerror) — general type mismatch errors.
