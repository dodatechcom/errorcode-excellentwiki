---
title: "[Solution] Python SyntaxError — Starred Assignment Target Must Be In List or Tuple"
description: "Fix Python SyntaxError with starred assignment targets. Learn about extended iterable unpacking and how to use star expressions correctly."
languages: ["python"]
severities: ["error"]
error_types: ["syntax"]
tags: ["syntaxerror", "star", "expression", "unpacking", "assignment"]
weight: 5
---

# SyntaxError — Starred Assignment Target Must Be In List or Tuple

A `SyntaxError` with the message "starred assignment target must be in a list or tuple" is raised when you use a starred expression (`*variable`) as a standalone assignment target instead of inside a list or tuple. Star expressions can only appear in unpacking contexts.

## Description

Star expressions (`*variable`) are used for extended iterable unpacking. They capture "remaining" elements from a sequence. However, they must appear inside a list `[...]`, tuple `(...)`, or as part of a function call. Using `*variable` as a direct assignment target is not allowed.

Common patterns:

- **Star as standalone target** — `*rest = [1, 2, 3]`.
- **Star outside list/tuple in assignment** — `first, *rest = value` is fine, but `*rest = value` alone is not.
- **Star in wrong context** — `*variable` used where a regular variable is expected.
- **Star in function call** — `func(*args)` is fine, but `func(*args, **kwargs)` has rules.

## Common Causes

```python
# Cause 1: Star as standalone target
*rest = [1, 2, 3]  # SyntaxError: starred assignment target must be in a list or tuple

# Cause 2: Star outside unpacking context
x = *range(5)  # SyntaxError

# Cause 3: Star in wrong position
*first, last = [1, 2, 3]  # This is fine — but:
first, *middle, last = value  # Fine — but standalone * is not

# Cause 4: Star in expression context
result = *range(5)  # SyntaxError
```

## Solutions

### Fix 1: Use star expression inside a list or tuple

```python
# Wrong
*rest = [1, 2, 3]  # SyntaxError

# Correct — use in unpacking context
first, *rest = [1, 2, 3]  # first=1, rest=[2, 3]

# Or wrap in list/tuple
[*rest] = [1, 2, 3]  # Still SyntaxError — must be in unpacking
```

### Fix 2: Use unpacking with multiple targets

```python
# Wrong
*rest = [1, 2, 3]  # SyntaxError

# Correct
first, *rest = [1, 2, 3]  # first=1, rest=[2, 3]

*init, last = [1, 2, 3]  # init=[1, 2], last=3

first, *middle, last = [1, 2, 3, 4, 5]  # first=1, middle=[2, 3, 4], last=5
```

### Fix 3: Use list() or tuple() for conversion

```python
# Wrong
*rest = range(5)  # SyntaxError

# Correct
rest = list(range(5))  # [0, 1, 2, 3, 4]

# Or
first, *rest = range(5)  # first=0, rest=[1, 2, 3, 4]
```

### Fix 4: Use extended unpacking in for loops

```python
# Wrong
*items = [1, 2, 3]  # SyntaxError

# Correct
first, *rest = [1, 2, 3]
for item in rest:
    print(item)  # 2, 3
```

## Related Errors

- [SyntaxError](../syntaxerror) — general syntax errors.
- [ValueError: not enough values to unpack](unpack-non-sequence) — unpacking errors.
- [TypeError](../typeerror) — general type mismatch errors.
