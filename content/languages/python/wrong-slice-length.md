---
title: "[Solution] Python ValueError — Slice Length Must Be Positive"
description: "Fix Python ValueError when slice length is negative or zero. Learn about slicing rules and how to handle invalid slice lengths."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ValueError — Slice Length Must Be Positive

A `ValueError` with the message "slice length must be positive" is raised when you try to create a slice with a negative or zero length. This typically occurs when the start index is greater than the stop index with a positive step, or when using `range()` with invalid arguments.

## Description

Slicing in Python follows specific rules. When using a positive step, the start index must be less than the stop index. When using a negative step, the start index must be greater than the stop index. Violating these rules results in an empty slice, but certain operations that require positive length will raise this error.

Common patterns:

- **Positive step with start > stop** — `list[5:2:1]`.
- **Negative step with start < stop** — `list[2:5:-1]`.
- **Range with negative length** — `range(5, 2)`.
- **Computed slice bounds that are inverted** — dynamic calculations producing wrong order.

## Common Causes

```python
# Cause 1: Positive step with start > stop
my_list = [1, 2, 3, 4, 5]
result = my_list[5:2:1]  # Empty slice — but some operations may error

# Cause 2: Range with inverted bounds
for i in range(5, 2):  # Empty range — no iterations
    print(i)

# Cause 3: Computed slice with wrong order
start = 10
stop = 5
my_list = [1, 2, 3, 4, 5]
result = my_list[start:stop]  # Empty slice

# Cause 4: Using bytes/bytearray with invalid slice
data = b"hello"
result = data[5:2]  # Empty bytes
```

## Solutions

### Fix 1: Ensure correct slice order

```python
# Wrong — start > stop with positive step
my_list = [1, 2, 3, 4, 5]
result = my_list[5:2:1]  # Empty

# Correct — swap start and stop
result = my_list[2:5]  # [3, 4, 5]
```

### Fix 2: Use min/max to normalize slice bounds

```python
start = 10
stop = 5

# Wrong
my_list = [1, 2, 3, 4, 5]
result = my_list[start:stop]  # Empty

# Correct
s, e = min(start, stop), max(start, stop)
result = my_list[s:e]
```

### Fix 3: Handle empty ranges gracefully

```python
# Wrong
for i in range(5, 2):  # Never executes
    print(i)

# Correct — check range before iterating
start, stop = 5, 2
if start < stop:
    for i in range(start, stop):
        print(i)
else:
    print("Range is empty")
```

### Fix 4: Use step=-1 for reverse iteration

```python
# Wrong
my_list = [1, 2, 3, 4, 5]
result = my_list[2:5:-1]  # Empty — wrong step direction

# Correct — use negative step for reverse
result = my_list[4:1:-1]  # [5, 4, 3]
```

## Related Errors

- [ValueError: slice step cannot be zero](slice-step-zero) — step of zero in slice.
- [ValueError](../valueerror) — general value errors.
- [TypeError](../typeerror) — general type mismatch errors.
