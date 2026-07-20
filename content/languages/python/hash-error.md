---
title: "[Solution] Python TypeError — unhashable type"
description: "Fix Python TypeError: unhashable type. Understand hash requirements for dict keys, set elements, and how to implement __hash__ correctly."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 708
---

# Python TypeError — unhashable type

A `TypeError` with the message `unhashable type: 'TYPE'` is raised when you try to use an unhashable object as a dictionary key, set element, or in any context that requires a hashable value. Hashable objects must have a `__hash__` method and must be immutable (their hash value never changes during their lifetime).

## Common Causes

```python
# Cause 1: Using a list as a dict key
data = {[1, 2, 3]: "value"}  # TypeError: unhashable type: 'list'

# Cause 2: Using a dict as a set element
s = set()
s.add({"a": 1})  # TypeError: unhashable type: 'dict'

# Cause 3: Using a list in a set
s = set()
s.add([1, 2, 3])  # TypeError: unhashable type: 'list'

# Cause 4: Custom class without __hash__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

s = {Point(1, 2)}  # TypeError: unhashable type: 'Point'

# Cause 5: Using mutable default argument in @lru_cache
from functools import lru_cache

@lru_cache(maxsize=128)
def process(items=[]):  # TypeError: unhashable type: 'list'
    return sum(items)
```

## How to Fix

### Fix 1: Use tuples instead of lists for hashable sequences

```python
# Wrong — list is unhashable
data = {[1, 2, 3]: "value"}  # TypeError

# Correct — use tuple
data = {(1, 2, 3): "value"}  # Works
print(data[(1, 2, 3)])  # value

# For sets
s = set()
s.add((1, 2, 3))  # Works
```

### Fix 2: Implement __hash__ for custom classes

```python
# Wrong — unhashable class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Correct — implement __hash__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

points = {Point(1, 2), Point(3, 4)}  # Works
print(Point(1, 2) in points)  # True
```

### Fix 3: Use frozenset for nested mutable structures

```python
# Wrong — set is unhashable
s = {{1, 2}, {3, 4}}  # TypeError

# Correct — use frozenset
s = {frozenset([1, 2]), frozenset([3, 4])}  # Works
print(s)

# For dict keys
data = {frozenset([1, 2]): "pair"}
```

### Fix 4: Use immutable types as @lru_cache arguments

```python
from functools import lru_cache

# Wrong — list is unhashable
@lru_cache(maxsize=128)
def process(items=[]):  # TypeError
    return sum(items)

# Correct — use tuple
@lru_cache(maxsize=128)
def process(items=()):
    return sum(items)

print(process((1, 2, 3)))  # 6
print(process((4, 5)))     # 9
```

### Fix 5: Convert mutable objects to hashable equivalents before caching

```python
from functools import lru_cache

# Wrong — dict is unhashable
@lru_cache(maxsize=128)
def get_value(data, key):
    return data.get(key)

get_value({"a": 1}, "a")  # TypeError

# Correct — convert dict to tuple of items
@lru_cache(maxsize=128)
def get_value(data_items, key):
    return dict(data_items).get(key)

get_value(tuple({"a": 1}.items()), "a")  # Works
```

## Examples

```python
# Real-world: Using custom objects as dictionary keys
class UserId:
    def __init__(self, user_id):
        self.user_id = user_id

    def __hash__(self):
        return hash(self.user_id)

    def __eq__(self, other):
        return isinstance(other, UserId) and self.user_id == other.user_id

users = {
    UserId(1): "Alice",
    UserId(2): "Bob",
}

print(users[UserId(1)])  # Alice

# Real-world: Caching with complex arguments
from functools import lru_cache

@lru_cache(maxsize=100)
def process_config(host, port, options_tuple):
    # options must be a tuple (hashable), not a dict
    return f"Connecting to {host}:{port} with {options_tuple}"

result = process_config("localhost", 5432, (("timeout", 30), ("retry", 3)))
print(result)

# Real-world: Using frozenset for set-based dictionary keys
def count_set_combinations(sets):
    counter = {}
    for s in sets:
        key = frozenset(s)
        counter[key] = counter.get(key, 0) + 1
    return counter

sets = [{1, 2}, {3, 4}, {1, 2}, {5, 6}]
print(count_set_combinations(sets))  # {frozenset({1, 2}): 2, frozenset({3, 4}): 1, frozenset({5, 6}): 1}
```

## Related Errors

- [KeyError](keyerror) — key not found in dictionary.
- [TypeError](../typeerror) — general type mismatch errors.
- [Callable not hashable](callable-not-hashable) — callable objects that can't be hashed.
