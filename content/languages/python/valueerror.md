---
title: "[Solution] Python ValueError — Invalid Argument Fix"
description: "Fix Python ValueError when passing invalid arguments. Solutions for empty strings, bad conversions, and invalid input values."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["valueerror", "value", "invalid", "input"]
weight: 20
---

# ValueError — Invalid Argument Fix

A `ValueError` is raised when a function receives an argument of the correct type but an inappropriate value. Unlike `TypeError`, the types match — the data itself is invalid.

## Description

`ValueError` occurs across many standard library functions:

- **`int("")`** — cannot convert an empty string to an integer.
- **`int("abc")`** — non-numeric string passed to `int()`.
- **`json.loads("")`** — empty string is not valid JSON.
- **`float("inf")` might be unexpected** — depending on context, special floats can cause downstream issues.
- **`math.sqrt(-1)`** — negative input to a function that only accepts non-negative values.
- **`open()` with bad mode** — invalid mode string.

The key distinction: the function signature accepts the type, but the value violates the function's preconditions.

## Common Causes

```python
# Cause 1: Converting an empty or whitespace-only string
number = int("")

# Cause 2: Non-numeric string passed to numeric conversion
number = int("hello")

# Cause 3: Malformed JSON string
import json
data = json.loads("not json at all")

# Cause 4: Negative value where positive is required
import math
result = math.sqrt(-4)

# Cause 5: Iterating over a generator that yields an unexpected value
values = [1, 2, -3, 4]
result = max(values)  # This works, but max() of empty sequence raises ValueError
empty = []
result = max(empty)  # ValueError: max() arg is an empty sequence
```

## Solutions

### Fix 1: Validate input before conversion

```python
# Wrong
user_input = ""
number = int(user_input)

# Correct
user_input = ""
if user_input.strip():
    number = int(user_input)
else:
    print("Input cannot be empty")
```

### Fix 2: Use try/except to handle bad conversions gracefully

```python
# Wrong — crashes on invalid input
user_input = "abc"
number = int(user_input)

# Correct — catches the error and provides a fallback
try:
    number = int(user_input)
except ValueError:
    number = 0
    print(f"Invalid number, defaulting to {number}")
```

### Fix 3: Validate before calling math functions

```python
import math

# Wrong
value = -4
result = math.sqrt(value)

# Correct
value = -4
if value >= 0:
    result = math.sqrt(value)
else:
    raise ValueError(f"Cannot compute square root of negative number: {value}")
```

### Fix 4: Validate JSON before parsing

```python
import json

# Wrong
raw = "not json"
data = json.loads(raw)

# Correct
raw = "not json"
try:
    data = json.loads(raw)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
    data = None
```

### Fix 5: Guard against empty sequences

```python
# Wrong
empty = []
result = max(empty)

# Correct
empty = []
if empty:
    result = max(empty)
else:
    result = None
    print("Cannot find max of empty sequence")
```

## Related Errors

- [TypeError](../typeerror) — wrong type entirely (e.g., adding `int + str`).
- [KeyError](../keyerror) — dictionary key does not exist.
- [IndexError](../indexerror) — list index out of valid range.
