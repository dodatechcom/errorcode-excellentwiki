---
title: "[Solution] Python StopIteration — Iterator Exhausted Fix"
description: "Fix Python StopIteration error when an iterator runs out of items. Use for loops, default values, and itertools patterns."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 110
---

# StopIteration — Iterator Exhausted Fix

A `StopIteration` is raised when you call `next()` on an iterator that has no more items to return. This signals the end of iteration, but becomes an error when not handled properly.

## Description

Every iterator raises `StopIteration` internally when exhausted. Python's `for` loop catches it automatically, but calling `next()` directly without a default or try/except will crash.

Common scenarios:

- **Calling next() too many times** — iterating past the end of a list or generator.
- **Manual iterator advancement** — using `next()` without checking availability.
- **Generators with premature exhaustion** — a generator runs out of yield statements.
- **Chained iterator operations** — `zip()`, `map()`, or `filter()` on uneven iterables.
- **Missing default value in next()** — not providing a fallback for exhausted iterators.

## Common Causes

```python
# Cause 1: Calling next() past the end
nums = iter([1, 2, 3])
next(nums)  # 1
next(nums)  # 2
next(nums)  # 3
next(nums)  # StopIteration

# Cause 2: Empty iterator
empty = iter([])
next(empty)  # StopIteration

# Cause 3: Generator runs out
def count_up_to(n):
    for i in range(n):
        yield i

gen = count_up_to(2)
list(gen)  # [0, 1]
next(gen)  # StopIteration

# Cause 4: next() without default on input stream
user_input = iter(["hello", "world"])
first = next(user_input)
second = next(user_input)
third = next(user_input)  # StopIteration
```

## Solutions

### Fix 1: Use a for loop instead of manual next()

```python
# Wrong
nums = iter([1, 2, 3])
while True:
    val = next(nums)  # StopIteration when exhausted

# Correct
nums = [1, 2, 3]
for val in nums:
    process(val)
```

### Fix 2: Provide a default value to next()

```python
# Wrong
nums = iter([1, 2, 3])
val = next(nums)
val = next(nums)
val = next(nums)
val = next(nums)  # StopIteration

# Correct
nums = iter([1, 2, 3])
val = next(nums, None)  # Returns None instead of raising StopIteration
if val is None:
    print("Iterator exhausted")
```

### Fix 3: Use try/except StopIteration

```python
# Wrong
def get_next_item(iterator):
    return next(iterator)  # Crashes on exhaustion

# Correct
def get_next_item(iterator):
    try:
        return next(iterator)
    except StopIteration:
        return None
```

### Fix 4: Check length before advancing

```python
# Wrong
items = iter(range(5))
for _ in range(10):
    print(next(items))  # StopIteration after 5 items

# Correct
items = list(range(5))
for item in items:
    print(item)
```

### Fix 5: Use itertools patterns for safe iteration

```python
from itertools import zip_longest, chain

# Wrong — zip stops at shortest, but chaining might exhaust
nums = iter([1, 2])
pairs = zip(nums, nums)
list(pairs)  # [(1, 2)]
next(nums)   # StopIteration

# Correct — use zip_longest with fillvalue
a = [1, 2, 3]
b = [10, 20]
list(zip_longest(a, b, fillvalue=None))  # [(1, 10), (2, 20), (3, None)]

# Correct — use chain.from_iterable safely
from itertools import islice
data = [[1, 2], [3, 4]]
flat = chain.from_iterable(data)
print(list(islice(flat, 3)))  # [1, 2, 3] — no crash
```

### Fix 6: Write generators that signal exhaustion cleanly

```python
# Wrong
def bad_generator():
    yield 1
    yield 2
    # Implicit StopIteration — callers must handle it

# Correct
def safe_generator():
    """Yields items and signals completion via return."""
    yield 1
    yield 2
    return  # Clean exhaustion

# Correct — wrapper with fallback
def safe_next(generator, default=None):
    try:
        return next(generator)
    except StopIteration:
        return default
```

## Related Errors

- [IndexError](../indexerror) — sequence index out of range.
- [ValueError](../valueerror) — wrong value passed to a function.
- [RuntimeError](./runtimeerror) — generic runtime error during iteration.
