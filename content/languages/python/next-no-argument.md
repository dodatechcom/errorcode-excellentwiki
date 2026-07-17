---
title: "[Solution] Python TypeError — next() Missing Required Argument"
description: "Fix Python TypeError when calling next() without required arguments. Learn the correct usage of next() and how to handle StopIteration."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# TypeError — next() Missing Required Argument

A `TypeError` with the message "next() missing required argument" is raised when you call `next()` without providing an iterator argument. The `next()` function requires at least one argument: an iterator with a `__next__()` method.

## Description

The `next()` function retrieves the next item from an iterator. It has two forms: `next(iterator)` and `next(iterator, default)`. Calling `next()` with no arguments raises a `TypeError` because Python doesn't know which iterator to advance.

Common patterns:

- **No arguments** — `next()`.
- **Passing a non-iterator** — `next(42)`.
- **Passing a list directly** — `next([1, 2, 3])`.
- **Using next() after iterator is exhausted** — without a default value.

## Common Causes

```python
# Cause 1: No arguments
value = next()  # TypeError: next() missing required argument 'iterator'

# Cause 2: Passing a non-iterator
value = next(42)  # TypeError: 'int' object is not an iterator

# Cause 3: Passing a list directly
value = next([1, 2, 3])  # TypeError: 'list' object is not an iterator

# Cause 4: No default and iterator exhausted
my_iter = iter([1, 2, 3])
next(my_iter)
next(my_iter)
next(my_iter)
next(my_iter)  # StopIteration — no default provided
```

## Solutions

### Fix 1: Provide an iterator argument

```python
# Wrong
value = next()  # TypeError

# Correct
my_iter = iter([1, 2, 3])
value = next(my_iter)  # Returns 1
```

### Fix 2: Convert list to iterator first

```python
# Wrong
value = next([1, 2, 3])  # TypeError

# Correct
value = next(iter([1, 2, 3]))  # Returns 1
```

### Fix 3: Use a default value for exhausted iterators

```python
my_iter = iter([1, 2, 3])

# Wrong — raises StopIteration when exhausted
value = next(my_iter)  # 1
value = next(my_iter)  # 2
value = next(my_iter)  # 3
value = next(my_iter)  # StopIteration!

# Correct — provide a default value
value = next(my_iter, None)  # Returns None instead of raising StopIteration
```

### Fix 4: Use a while loop to safely iterate

```python
# Wrong
my_iter = iter([1, 2, 3])
while True:
    value = next(my_iter)  # StopIteration at end

# Correct
my_iter = iter([1, 2, 3])
while True:
    try:
        value = next(my_iter)
    except StopIteration:
        break
    print(value)
```

## Related Errors

- [StopIteration](../stopiteration) — iterator exhausted.
- [Object not iterable](object-not-iterable) — trying to iterate over non-iterable.
- [Iteration over non-sequence](iteration-over-non-sequence) — similar iteration error.
