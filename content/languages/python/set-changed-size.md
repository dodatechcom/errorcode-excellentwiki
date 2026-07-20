---
title: "[Solution] Python RuntimeError — Set changed size during iteration"
description: "Fix Python RuntimeError: Set changed size during iteration. Learn safe patterns for modifying sets while looping through them."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 706
---

# Python RuntimeError — Set changed size during iteration

A `RuntimeError` with the message `Set changed size during iteration` is raised when you add or remove elements from a set while iterating over it. Like dictionaries and lists, Python does not allow modifying a set's size during iteration.

## Common Causes

```python
# Cause 1: Removing elements during iteration
numbers = {1, 2, 3, 4, 5}
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # RuntimeError: Set changed size during iteration

# Cause 2: Adding elements during iteration
numbers = {1, 2, 3}
for num in numbers:
    numbers.add(num * 10)  # RuntimeError: Set changed size during iteration

# Cause 3: Using .discard() during iteration
numbers = {1, 2, 3, 4, 5}
for num in numbers:
    if num > 3:
        numbers.discard(num)  # RuntimeError

# Cause 4: Using .pop() during iteration
numbers = {1, 2, 3}
for num in numbers:
    numbers.pop()  # RuntimeError

# Cause 5: Updating set during iteration
numbers = {1, 2, 3}
for num in numbers:
    numbers.update({num * 2})  # RuntimeError
```

## How to Fix

### Fix 1: Use set comprehension to create a new set

```python
# Wrong
numbers = {1, 2, 3, 4, 5}
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # RuntimeError

# Correct — use set comprehension
numbers = {1, 2, 3, 4, 5}
numbers = {num for num in numbers if num % 2 != 0}
print(numbers)  # {1, 3, 5}
```

### Fix 2: Iterate over a copy

```python
# Wrong
numbers = {1, 2, 3, 4, 5}
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # RuntimeError

# Correct — iterate over a copy
numbers = {1, 2, 3, 4, 5}
for num in numbers.copy():
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)  # {1, 3, 5}
```

### Fix 3: Use set operations instead of iteration

```python
# Wrong
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)

# Correct — use set difference
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
evens = {num for num in numbers if num % 2 == 0}
numbers -= evens  # Or: numbers = numbers - evens
print(numbers)  # {1, 3, 5, 7, 9}
```

### Fix 4: Use explicit loop with set operations

```python
# Correct — collect items to add/remove, then apply
numbers = {1, 2, 3, 4, 5}
to_add = set()
to_remove = set()

for num in numbers:
    if num % 2 == 0:
        to_remove.add(num)
    else:
        to_add.add(num * 10)

numbers -= to_remove
numbers |= to_add
print(numbers)  # {10, 30, 50, 1, 3, 5}
```

## Examples

```python
# Real-world: Filtering unique words while normalizing
words = {"Hello", "hello", "HELLO", "World", "world"}
normalized = {w.lower() for w in words}
print(normalized)  # {'hello', 'world'}

# Real-world: Building a set of reachable nodes in a graph
graph = {
    "A": {"B", "C"},
    "B": {"D"},
    "C": {"D", "E"},
    "D": set(),
    "E": set(),
}

def bfs(graph, start):
    visited = set()
    queue = {start}
    while queue:
        current = queue.pop()
        visited.add(current)
        queue |= graph[current] - visited
    return visited

reachable = bfs(graph, "A")
print(reachable)  # {'A', 'B', 'C', 'D', 'E'}

# Real-world: Removing duplicates from multiple sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {5, 6, 7, 8}

# Elements common to all three
common = set1 & set2 & set3
print(common)  # set()

# Elements unique to each set
only_set1 = set1 - set2 - set3
print(only_set1)  # {1, 2}
```

## Related Errors

- [Dictionary changed size during iteration](dict-changed-size) — same error for dicts.
- [List changed size during iteration](list-changed-size) — same error for lists.
- [RuntimeError](../runtimeerror) — general runtime errors.
