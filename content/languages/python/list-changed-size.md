---
title: "[Solution] Python RuntimeError — list changed size during iteration"
description: "Fix Python RuntimeError: list changed size during iteration. Learn safe patterns for removing items while looping through a list."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 705
---

# Python RuntimeError — list changed size during iteration

A `RuntimeError` with the message `list changed size during iteration` is raised when you add or remove elements from a list while iterating over it with a `for` loop. Python detects the size change and raises this error to prevent skipped or repeated elements.

## Common Causes

```python
# Cause 1: Removing items during forward iteration
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)  # RuntimeError: list changed size during iteration

# Cause 2: Appending items during iteration
items = [1, 2, 3]
for item in items:
    items.append(item * 10)  # RuntimeError: list changed size during iteration

# Cause 3: Using list.pop() during iteration
items = ["a", "b", "c", "d"]
for item in items:
    if item == "b":
        items.pop(1)  # RuntimeError

# Cause 4: Extending list during iteration
items = [1, 2, 3]
for item in items:
    items.extend([item * 2])  # RuntimeError

# Cause 5: Removing with filter() on the original list
items = [1, 2, 3, 4, 5]
filtered = filter(lambda x: x > 2, items)
items.clear()  # May cause issues if filtered is still referencing items
```

## How to Fix

### Fix 1: Use list comprehension to create a new list

```python
# Wrong
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)  # RuntimeError

# Correct — use list comprehension
items = [1, 2, 3, 4, 5]
items = [item for item in items if item % 2 != 0]
print(items)  # [1, 3, 5]
```

### Fix 2: Iterate over a copy

```python
# Wrong
items = ["a", "b", "c", "d"]
for item in items:
    if item == "b":
        items.remove(item)  # RuntimeError

# Correct — iterate over a copy
items = ["a", "b", "c", "d"]
for item in items[:]:  # items[:] creates a shallow copy
    if item == "b":
        items.remove(item)

print(items)  # ['a', 'c', 'd']
```

### Fix 3: Use enumerate() + filter pattern

```python
# Wrong
items = [1, 2, 3, 4, 5]
for i, item in enumerate(items):
    if item % 2 == 0:
        items.pop(i)  # RuntimeError

# Correct — collect indices first, then remove in reverse
items = [1, 2, 3, 4, 5]
indices_to_remove = [i for i, item in enumerate(items) if item % 2 == 0]
for i in reversed(indices_to_remove):
    items.pop(i)

print(items)  # [1, 3, 5]
```

### Fix 4: Use a while loop with manual index control

```python
# Correct — while loop allows safe removal
items = [1, 2, 3, 4, 5]
i = 0
while i < len(items):
    if items[i] % 2 == 0:
        items.pop(i)
    else:
        i += 1

print(items)  # [1, 3, 5]
```

## Examples

```python
# Real-world: Removing inactive users from a list
users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Charlie", "active": True},
    {"name": "Diana", "active": False},
]

# Correct — filter to a new list
active_users = [u for u in users if u["active"]]
print(active_users)  # [{'name': 'Alice', 'active': True}, {'name': 'Charlie', 'active': True}]

# Or modify in place safely
indices_to_remove = [i for i, u in enumerate(users) if not u["active"]]
for i in reversed(indices_to_remove):
    users.pop(i)

print(users)  # [{'name': 'Alice', 'active': True}, {'name': 'Charlie', 'active': True}]

# Real-world: Deduplicating while preserving order
items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
seen = set()
result = []
for item in items:
    if item not in seen:
        seen.add(item)
        result.append(item)

print(result)  # [3, 1, 4, 5, 9, 2, 6]
```

## Related Errors

- [Dictionary changed size during iteration](dict-changed-size) — same error for dicts.
- [Set changed size during iteration](set-changed-size) — same error for sets.
- [RuntimeError](../runtimeerror) — general runtime errors.
