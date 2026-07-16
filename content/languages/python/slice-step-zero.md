---
title: "[Solution] Python ValueError — Slice Step Cannot Be Zero"
description: "Fix Python ValueError when using a slice with step=0. Learn why slice steps must be non-zero and how to use slicing correctly."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["valueerror", "slice", "step", "range"]
weight: 5
---

# ValueError — Slice Step Cannot Be Zero

A `ValueError` with the message "slice step cannot be zero" is raised when you use `0` as the step in a slice operation like `list[start:stop:0]` or `range(0)`. The step parameter determines how many elements to skip, and skipping zero elements creates an infinite loop.

## Description

Slicing in Python uses the syntax `sequence[start:stop:step]`. The `step` parameter controls the increment between elements. A step of 0 would mean "take the same element forever," which is undefined behavior. Valid steps are positive (forward) or negative (backward).

Common patterns:

- **Step of 0 in slice** — `my_list[::0]`.
- **Range with step 0** — `range(0, 10, 0)`.
- **Variable step is 0** — computed step that evaluates to 0.
- **Step from user input** — unvalidated input used as step.

## Common Causes

```python
# Cause 1: Direct step of 0
my_list = [1, 2, 3, 4, 5]
result = my_list[::0]  # ValueError: slice step cannot be zero

# Cause 2: Range with step 0
for i in range(0, 10, 0):  # ValueError: range() arg 3 must not be zero
    print(i)

# Cause 3: Variable step is 0
step = 0
my_list = [1, 2, 3, 4, 5]
result = my_list[::step]  # ValueError

# Cause 4: Computed step that evaluates to 0
def get_step(n):
    return n - n  # Always returns 0

my_list = [1, 2, 3, 4, 5]
result = my_list[::get_step(5)]  # ValueError
```

## Solutions

### Fix 1: Use a non-zero step

```python
# Wrong
my_list = [1, 2, 3, 4, 5]
result = my_list[::0]  # ValueError

# Correct — step of 1 (default)
result = my_list[::1]  # [1, 2, 3, 4, 5]

# Or step of 2 (every other element)
result = my_list[::2]  # [1, 3, 5]
```

### Fix 2: Validate step before using it

```python
def safe_slice(sequence, start, stop, step):
    if step == 0:
        raise ValueError("Step cannot be zero")
    return sequence[start:stop:step]

my_list = [1, 2, 3, 4, 5]
result = safe_slice(my_list, 0, 5, 0)  # Raises ValueError with message
```

### Fix 3: Provide a default step when step is 0

```python
step = 0
my_list = [1, 2, 3, 4, 5]

# Wrong
result = my_list[::step]

# Correct
if step == 0:
    step = 1
result = my_list[::step]
```

### Fix 4: Use abs() for absolute step values

```python
step = -2
my_list = [1, 2, 3, 4, 5]

# Wrong — negative step reverses
result = my_list[::step]  # [5, 3, 1]

# Correct — use abs() if you want forward iteration
result = my_list[::abs(step)]  # [1, 3, 5]
```

## Related Errors

- [ValueError: slice length must be positive](wrong-slice-length) — invalid slice length.
- [ValueError](../valueerror) — general value errors.
- [TypeError](../typeerror) — general type mismatch errors.
