---
title: "[Solution] Python MemoryError — Out of Memory Fix"
description: "Fix Python MemoryError when your program runs out of RAM. Use generators, optimize data structures, and process in chunks."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["memoryerror", "memory", "ram", "optimization", "generators"]
weight: 100
---

# MemoryError — Out of Memory Fix

A `MemoryError` is raised when Python cannot allocate memory because the system has run out of RAM or the process exceeds its memory limit.

## Description

Python's `MemoryError` occurs when an operation requires more memory than is available. This happens when loading large datasets, creating huge lists, or when memory leaks accumulate over time.

Common scenarios:

- **Loading entire large files into memory** — reading multi-GB files at once.
- **Creating massive lists or dicts** — `[0] * 10_000_000_000` exhausts RAM.
- **Memory leaks** — circular references or accumulations that never free.
- **Inefficient data structures** — using Python objects instead of arrays or NumPy.
- **Recursive deep calls** — each frame consumes memory on the call stack.

## Common Causes

```python
# Cause 1: Creating a massive list
huge_list = [0] * 10_000_000_000  # MemoryError: ~40GB required

# Cause 2: Loading entire file into memory
with open("huge_log.txt", "r") as f:
    data = f.read()  # MemoryError for multi-GB files

# Cause 3: Expanding data without cleanup
results = []
for i in range(10_000_000):
    results.append(i ** 2)  # List grows unbounded in memory

# Cause 4: Inefficient data representation
from datetime import datetime
timestamps = [datetime.now() for _ in range(100_000_000)]  # Huge overhead per datetime object
```

## Solutions

### Fix 1: Use generators instead of lists

```python
# Wrong — creates entire list in memory
squares = [x ** 2 for x in range(10_000_000)]
for s in squares:
    process(s)

# Correct — generator yields one item at a time
squares = (x ** 2 for x in range(10_000_000))
for s in squares:
    process(s)
```

### Fix 2: Process large files in chunks

```python
# Wrong — loads entire file into memory
with open("huge_log.txt", "r") as f:
    lines = f.readlines()  # MemoryError for large files

# Correct — read line by line
with open("huge_log.txt", "r") as f:
    for line in f:
        process(line)

# Correct — read in fixed-size chunks
CHUNK_SIZE = 8192
with open("huge_file.bin", "rb") as f:
    while chunk := f.read(CHUNK_SIZE):
        process(chunk)
```

### Fix 3: Use NumPy arrays instead of Python lists for numeric data

```python
# Wrong — Python list of integers is memory-heavy
data = list(range(10_000_000))  # ~400MB for Python ints

# Correct — NumPy array is much more compact
import numpy as np
data = np.arange(10_000_000, dtype=np.int32)  # ~40MB
```

### Fix 4: Process data in batches

```python
# Wrong — loads all data at once
import pandas as pd
df = pd.read_csv("huge_dataset.csv")  # MemoryError for large files

# Correct — process in chunks
import pandas as pd
for chunk in pd.read_csv("huge_dataset.csv", chunksize=10_000):
    process(chunk)
    del chunk  # Explicitly free memory
```

### Fix 5: Use del and gc to free memory proactively

```python
import gc

# Wrong — reference kept after use
big_data = load_huge_dataset()
result = analyze(big_data)
# big_data still in memory

# Correct — free immediately after use
big_data = load_huge_dataset()
result = analyze(big_data)
del big_data
gc.collect()
```

### Fix 6: Use memory-efficient alternatives

```python
# Wrong — storing millions of Python objects
class Record:
    def __init__(self, id, name, value):
        self.id = id
        self.name = name
        self.value = value

records = [Record(i, f"name_{i}", i * 1.5) for i in range(1_000_000)]

# Correct — use dataclass with __slots__ to reduce per-instance memory
from dataclasses import dataclass

@dataclass
class Record:
    __slots__ = ['id', 'name', 'value']
    id: int
    name: str
    value: float

records = [Record(i, f"name_{i}", i * 1.5) for i in range(1_000_000)]
```

## Related Errors

- [RecursionError](./recursionerror) — stack overflow from too many recursive calls.
- [OverflowError](./overflowerror) — number too large to represent.
- [OSError](./permissionerror) — system-level resource issues.
