---
title: "[Solution] Python heapq Error — Heap Queue Algorithm Errors"
description: "Fix Python heapq errors including heapify, heappush, heappop failures, comparison errors, and more. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 222
---

# Python heapq Error — Heap Queue Algorithm Errors

The `heapq` module provides an implementation of the heap queue algorithm. Errors typically involve comparison failures, empty heap operations, and invalid arguments.

## Common Causes

```python
import heapq

# Error: heappop from an empty heap
heap = []
heapq.heappop(heap)
# IndexError: index out of range
```

```python
import heapq

# Error: comparing objects that don't support comparison
class Task:
    def __init__(self, name):
        self.name = name

heap = [Task("a"), Task("b")]
heapq.heapify(heap)
# TypeError: '<' not supported between instances of 'Task' and 'Task'
```

```python
import heapq

# Error: heapreplace on an empty heap
heap = []
heapq.heapreplace(heap, 99)
# IndexError: index out of range
```

```python
import heapq

# Error: nlargest/nsmallest with invalid k
heap = [3, 1, 4]
heapq.nlargest(0, heap)
# ValueError: k must be >= 1
```

```python
import heapq

# Error: mixing comparable types in the heap
heap = [1, "two", 3]
heapq.heapify(heap)
# TypeError: '<' not supported between instances of 'str' and 'int'
```

## How to Fix

### Fix 1: Check That the Heap Is Non-Empty Before Popping

```python
import heapq

heap = []
if heap:  # guard before pop
    val = heapq.heappop(heap)
else:
    print("Heap is empty")

# Or use a try/except block
try:
    val = heapq.heappop(heap)
except IndexError:
    print("Cannot pop from an empty heap")
```

### Fix 2: Implement Comparison for Custom Objects

```python
import heapq

class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name

    def __lt__(self, other):
        return self.priority < other.priority

tasks = [Task(3, "low"), Task(1, "high"), Task(2, "medium")]
heapq.heapify(tasks)
top = heapq.heappop(tasks)
print(top.name)  # "high"
```

### Fix 3: Use a Sentinel Value Instead of heapreplace on Empty Heap

```python
import heapq

heap = []
if heap:
    old = heapq.heapreplace(heap, 99)
else:
    heapq.heappush(heap, 99)

# Or push first, then replace
if not heap:
    heapq.heappush(heap, 99)
else:
    heapq.heapreplace(heap, 99)
```

### Fix 4: Ensure k >= 1 for nlargest/nsmallest

```python
import heapq

data = [5, 1, 3, 9, 7]
k = max(1, min(3, len(data)))
result = heapq.nlargest(k, data)
print(result)  # [9, 7, 5]
```

## Examples

```python
import heapq

# Merge multiple sorted lists
lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
merged = list(heapq.merge(*lists))
print(merged)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Priority queue with tie-breaking
import itertools
counter = itertools.count()
tasks = []
for priority, task_name in [(3, "low"), (1, "high"), (1, "urgent")]:
    heapq.heappush(tasks, (priority, next(counter), task_name))
next_task = heapq.heappop(tasks)
print(next_task[2])  # "high" or "urgent" depending on insertion order
```

## Related Errors

- [Python TypeError](/languages/python/python-typeerror/)
- [Python IndexError](/languages/python/python-indexerror/)
- [Python ValueError](/languages/python/python-valueerror/)
