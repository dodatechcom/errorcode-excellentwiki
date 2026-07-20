---
title: "[Solution] Python queue Error — Queue Module Threading Errors"
description: "Fix Python queue errors including Full/Empty exceptions, blocking put/get, Queue.join, priority queue, and LifoQueue issues. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 223
---

# Python queue Error — Queue Module Threading Errors

The `queue` module implements multi-producer, multi-consumer queues for threading. Errors involve full/empty exceptions, blocking behavior, and priority queue issues.

## Common Causes

```python
import queue

# Error: Getting from an empty queue without blocking
q = queue.Queue()
q.get_nowait()
# queue.Empty
```

```python
import queue

# Error: Putting to a full queue without blocking
q = queue.Queue(maxsize=1)
q.put("item1")
q.put_nowait("item2")
# queue.Full
```

```python
import queue

# Error: Invalid maxsize
q = queue.Queue(maxsize=-1)
# ValueError: maxsize must be >= 0
```

```python
import queue

# Error: Priority queue with incomparable items
pq = queue.PriorityQueue()
pq.put((1, "task"))
pq.put("invalid")
# TypeError: '<' not supported between instances of 'str' and 'tuple'
```

```python
import queue

# Error: task_done() called more times than items were put
q = queue.Queue()
q.put("item1")
q.get()
q.task_done()
q.task_done()
# ValueError: task_done() called too many times
```

## How to Fix

### Fix 1: Use try/except for Empty and Full

```python
import queue

q = queue.Queue()

# Handle empty queue
try:
    item = q.get_nowait()
except queue.Empty:
    print("Queue is empty")

# Handle full queue
q.maxsize = 1
q.put("item1")
try:
    q.put_nowait("item2")
except queue.Full:
    print("Queue is full")
```

### Fix 2: Use Non-Negative maxsize

```python
import queue

# maxsize=0 means unlimited queue
q = queue.Queue(maxsize=0)
q.put("item1")
q.put("item2")

# Use a positive maxsize for bounded queues
q = queue.Queue(maxsize=100)
```

### Fix 3: Use Comparable Items in PriorityQueue

```python
import queue

pq = queue.PriorityQueue()

# Use tuples with priority first
pq.put((1, "urgent_task"))
pq.put((3, "low_task"))
pq.put((2, "medium_task"))

# Or implement __lt__ on your objects
class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
    def __lt__(self, other):
        return self.priority < other.priority

pq.put(Task(1, "urgent"))
```

### Fix 4: Call task_done() Only After a Successful get()

```python
import queue
import threading

q = queue.Queue()
q.put("task1")
q.put("task2")

def worker():
    while True:
        item = q.get()
        try:
            process(item)
        finally:
            q.task_done()  # call exactly once per get()

threading.Thread(target=worker, daemon=True).start()
q.join()
```

## Examples

```python
import queue
import threading
import time

# Producer-consumer pattern with timeout
q = queue.Queue(maxsize=5)

def producer():
    for i in range(10):
        try:
            q.put(i, timeout=2)
            print(f"Produced: {i}")
        except queue.Full:
            print("Producer timed out")

def consumer():
    while True:
        try:
            item = q.get(timeout=2)
            print(f"Consumed: {item}")
            q.task_done()
        except queue.Empty:
            break

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start()
t2.start()
t1.join()
t2.join()
```

## Related Errors

- [Python threading Error](/languages/python/python-threading-error/)
- [Python TypeError](/languages/python/python-typeerror/)
- [Python RuntimeError](/languages/python/python-runtimeerror/)
