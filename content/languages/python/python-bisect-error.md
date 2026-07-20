---
title: "[Solution] Python bisect Module Error — Sorted Sequence Insertion Failures"
description: "Fix Python bisect module errors including bisect.insort, insort_right/left, index errors, and sorted sequence maintenance. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 251
---

# Python bisect Module Error — Sorted Sequence Insertion Failures

The `bisect` module provides functions for maintaining sorted lists. Errors occur when sequences are not actually sorted, wrong function variants are used, or when the sequence type doesn't support the required operations.

## Common Causes

```python
# Cause 1: Inserting into unsorted list
import bisect

lst = [3, 1, 4, 1, 5]  # Not sorted!
bisect.insort(lst, 2)  # No error, but result is incorrect

# Cause 2: Using insort_right when insort_left is needed (or vice versa)
import bisect

lst = [1, 2, 2, 3, 3, 3]
bisect.insort_right(lst, 2)  # Inserts after existing 2s
bisect.insort_left(lst, 2)   # Inserts before existing 2s
# Order matters for duplicate handling

# Cause 3: Sequence doesn't support item assignment
import bisect

# Tuples are immutable — cannot use insort
tpl = (1, 2, 3, 4)
bisect.insort(tpl, 5)  # AttributeError: 'tuple' object has no attribute '__setitem__'

# Cause 4: Index out of range
import bisect

lst = [10, 20, 30]
index = bisect.bisect_right(lst, 100)
# index = 3, but lst[3] would be IndexError

# Cause 5: Comparing incompatible types
import bisect

lst = [1, 2, 3, "four"]  # Mixed types
bisect.insort(lst, 2.5)  # TypeError in Python 3
```

## How to Fix

### Fix 1: Ensure list is sorted before using bisect

```python
import bisect

# Sort the list first
lst = [3, 1, 4, 1, 5, 9, 2, 6]
lst.sort()  # Now sorted: [1, 1, 2, 3, 4, 5, 6, 9]
bisect.insort(lst, 7)
print(lst)  # [1, 1, 2, 3, 4, 5, 6, 7, 9]

# Or use bisect on a copy that's sorted
original = [3, 1, 4, 1, 5]
sorted_lst = sorted(original)
bisect.insort(sorted_lst, 2)
```

### Fix 2: Choose insort_left vs insort_right correctly

```python
import bisect

lst = [1, 2, 2, 3, 3, 3]

# insort_right: insert after any existing entries
bisect.insort_right(lst, 2)
print(lst)  # [1, 2, 2, 2, 3, 3, 3] — new 2 after the two existing 2s

# insort_left: insert before any existing entries
lst = [1, 2, 2, 3, 3, 3]
bisect.insort_left(lst, 2)
print(lst)  # [1, 2, 2, 2, 3, 3, 3] — new 2 before the two existing 2s

# For priority ordering, use insort_left
# For stable append behavior, use insort_right
```

### Fix 3: Convert immutable sequences to lists

```python
import bisect

# Cannot insert into tuple directly
tpl = (1, 2, 3, 4)

# Convert to list first
lst = list(tpl)
bisect.insort(lst, 5)
print(lst)  # [1, 2, 3, 4, 5]

# Or maintain a separate sorted list
sorted_lst = sorted(tpl)
bisect.insort(sorted_lst, 0)
print(sorted_lst)  # [0, 1, 2, 3, 4]
```

### Fix 4: Handle boundary conditions safely

```python
import bisect

lst = [10, 20, 30]

# Check index before accessing
index = bisect.bisect_right(lst, 5)
if index < len(lst):
    print(f"Next larger value: {lst[index]}")
else:
    print("Value is larger than all elements")

# Find the correct position safely
def safe_insert(lst, value):
    index = bisect.bisect_left(lst, value)
    if index < len(lst) and lst[index] == value:
        print(f"Value {value} already exists at index {index}")
    else:
        lst.insert(index, value)
        print(f"Inserted {value} at index {index}")

safe_insert([10, 20, 30], 20)  # Already exists
safe_insert([10, 20, 30], 25)  # Inserted at index 2
```

### Fix 5: Use with custom key functions

```python
import bisect

# Sort by a key function
data = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
]

# Sort data by score
data.sort(key=lambda x: x["score"])

# Find insertion point for a new score
new_score = 88
index = bisect.bisect_left(
    [d["score"] for d in data],
    new_score
)
data.insert(index, {"name": "New", "score": new_score})

for d in data:
    print(f"{d['name']}: {d['score']}")
```

## Examples

```python
# Real-world: Maintain a ranked leaderboard
import bisect

class Leaderboard:
    def __init__(self):
        self.scores = []
        self.names = []

    def add_score(self, name, score):
        index = bisect.bisect_left(self.scores, -score)  # Negative for descending
        self.scores.insert(index, -score)
        self.names.insert(index, name)

    def get_top(self, n=10):
        return [(self.names[i], -self.scores[i])
                for i in range(min(n, len(self.scores)))]

lb = Leaderboard()
lb.add_score("Alice", 85)
lb.add_score("Bob", 92)
lb.add_score("Charlie", 78)
lb.add_score("Diana", 95)

print(lb.get_top(3))
# [('Diana', 95), ('Bob', 92), ('Alice', 85)]

# Real-world: Find closest value in sorted list
import bisect

def find_closest(sorted_lst, target):
    index = bisect.bisect_left(sorted_lst, target)
    if index == 0:
        return sorted_lst[0]
    if index == len(sorted_lst):
        return sorted_lst[-1]
    before = sorted_lst[index - 1]
    after = sorted_lst[index]
    if target - before <= after - target:
        return before
    return after

numbers = [10, 20, 30, 40, 50]
print(find_closest(numbers, 33))  # 30
print(find_closest(numbers, 37))  # 40
```

## Related Errors

- [IndexError](/languages/python/indexerror/) — index out of range
- [TypeError](/languages/python/typeerror/) — comparing incompatible types
- [AttributeError](/languages/python/attributeerror/) — immutable sequence type
