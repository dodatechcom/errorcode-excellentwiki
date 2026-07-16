---
title: "[Solution] Python TypeError — 'X' Object Is Not Iterable"
description: "Fix Python TypeError when trying to iterate over a non-iterable object. Learn which types are iterable and how to make custom objects iterable."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["typeerror", "iterable", "iteration", "object"]
weight: 5
---

# TypeError — 'X' Object Is Not Iterable

A `TypeError` with the message "'X' object is not iterable" is raised when you try to iterate over an object that doesn't implement the `__iter__` method. This includes integers, floats, booleans, `None`, and custom objects without iteration support.

## Description

Iterable objects implement the `__iter__` method, which returns an iterator. Built-in iterables include lists, tuples, strings, dictionaries, sets, and generators. Non-iterables include `int`, `float`, `bool`, `None`, and custom objects that don't implement `__iter__`.

Common patterns:

- **Iterating over an integer** — `for i in 5:`.
- **Using in on non-iterable** — `3 in 42`.
- **Unpacking non-iterable** — `a, b = 5`.
- **Passing non-iterable to sum/min/max** — `sum(42)`.

## Common Causes

```python
# Cause 1: Iterating over an integer
for i in 5:
    print(i)  # TypeError: 'int' object is not iterable

# Cause 2: Using 'in' on non-iterable
result = 3 in 42  # TypeError: argument of type 'int' is not iterable

# Cause 3: Unpacking non-iterable
a, b = 5  # TypeError: cannot unpack non-iterable int object

# Cause 4: Custom object without __iter__
class MyClass:
    pass

for item in MyClass():
    print(item)  # TypeError: 'MyClass' object is not iterable
```

## Solutions

### Fix 1: Wrap non-iterables in a list or range

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

### Fix 2: Implement __iter__ on custom objects

```python
# Wrong
class MyClass:
    pass

for item in MyClass():  # TypeError
    print(item)

# Correct
class MyClass:
    def __init__(self):
        self.data = [1, 2, 3]

    def __iter__(self):
        return iter(self.data)

for item in MyClass():
    print(item)  # 1, 2, 3
```

### Fix 3: Use hasattr() to check before iterating

```python
value = 42

# Wrong
for item in value:  # TypeError
    print(item)

# Correct
if hasattr(value, '__iter__'):
    for item in value:
        print(item)
else:
    print(f"Value {value} is not iterable")
```

### Fix 4: Use isinstance() for type checking

```python
def process(data):
    if isinstance(data, (list, tuple, set)):
        return sum(data)
    elif isinstance(data, (int, float)):
        return data
    else:
        raise TypeError(f"Cannot process {type(data)}")

print(process([1, 2, 3]))  # 6
print(process(5))  # 5
```

## Related Errors

- [Iteration over non-sequence](iteration-over-non-sequence) — similar iteration error.
- [Object not iterable](object-not-iterable) — general non-iterable errors.
- [TypeError](../typeerror) — general type mismatch errors.
