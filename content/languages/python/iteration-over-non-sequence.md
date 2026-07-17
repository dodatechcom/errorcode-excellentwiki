---
title: "[Solution] Python TypeError — Iteration Over Non-Sequence"
description: "Fix Python TypeError: 'int' object is not iterable when trying to iterate over a non-iterable type. Learn common causes and solutions."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# TypeError — 'int' Object Is Not Iterable

A `TypeError` with the message "'int' object is not iterable" is raised when you try to iterate over a non-iterable object, such as an integer, float, or `None`. Only objects that implement the `__iter__` method can be used in `for` loops or with `list()`, `sum()`, etc.

## Description

Iterables in Python include lists, tuples, strings, dictionaries, sets, and generators. Non-iterables include integers, floats, booleans, and `None`. This error commonly occurs when a function returns a single value instead of a collection, or when you accidentally pass a number to an iteration construct.

Common patterns:

- **Iterating over an integer** — `for i in 5:`.
- **Using sum() on a non-iterable** — `sum(42)`.
- **Unpacking a non-iterable** — `a, b = 5`.
- **Function returns a value instead of a list** — `result = process(); for x in result:`.

## Common Causes

```python
# Cause 1: Trying to iterate over an integer
for i in 5:
    print(i)  # TypeError: 'int' object is not iterable

# Cause 2: Using sum() on a non-iterable
total = sum(42)  # TypeError: 'int' object is not iterable

# Cause 3: Unpacking a non-iterable
a, b = 5  # TypeError: cannot unpack non-iterable int object

# Cause 4: Function returns a value instead of a collection
def get_data():
    return 42  # Returns a single value

data = get_data()
for item in data:  # TypeError: 'int' object is not iterable
    print(item)
```

## Solutions

### Fix 1: Wrap the value in a list or range

```python
# Wrong
for i in 5:
    print(i)

# Correct
for i in range(5):
    print(i)

# Or wrap in a list
for i in [5]:
    print(i)
```

### Fix 2: Ensure function returns an iterable

```python
# Wrong
def get_data():
    return 42

# Correct — return a list
def get_data():
    return [42]

# Or return a range
def get_data():
    return range(42)
```

### Fix 3: Use isinstance to check before iterating

```python
value = 42

# Wrong
for item in value:
    print(item)

# Correct
if hasattr(value, '__iter__'):
    for item in value:
        print(item)
else:
    print(f"Value {value} is not iterable")
```

### Fix 4: Handle single values and collections differently

```python
def process(data):
    if isinstance(data, (list, tuple)):
        return sum(data)
    else:
        return data

# Works with both
print(process([1, 2, 3]))  # 6
print(process(5))  # 5
```

## Related Errors

- [Iteration over non-sequence](iteration-over-non-sequence) — similar iteration errors.
- [Object not iterable](object-not-iterable) — general non-iterable errors.
- [TypeError](../typeerror) — general type mismatch errors.
