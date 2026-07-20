---
title: "[Solution] Python 3.11 ExceptionGroup Error — BaseExceptionGroup, except*, TaskGroups"
description: "Fix Python 3.11+ ExceptionGroup errors including BaseExceptionGroup usage, except* syntax, raising ExceptionGroups, nesting, and TaskGroup integration."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 508
---

# Python 3.11 ExceptionGroup Error — BaseExceptionGroup, except*, TaskGroups

Python 3.11 introduced `ExceptionGroup` and `except*` for handling multiple exceptions simultaneously. Common errors include incorrect `except*` syntax, improper ExceptionGroup construction, and confusion about when exceptions get grouped.

## Common Causes

```python
# Cause 1: Using except instead of except*
try:
    raise ExceptionGroup("errors", [ValueError("bad"), TypeError("wrong")])
except ValueError:  # This won't catch the ExceptionGroup
    print("caught")

# Cause 2: Raising ExceptionGroup incorrectly
raise ExceptionGroup("group", [ValueError("a"), TypeError("b")])  # Must be list of exceptions

# Cause 3: Wrong except* syntax
try:
    raise ExceptionGroup("errors", [ValueError("bad")])
except* ValueError as eg:  # Wrong - need * after except
    print(eg.exceptions)

# Cause 4: Nesting ExceptionGroups without flattening
inner = ExceptionGroup("inner", [ValueError("a")])
outer = ExceptionGroup("outer", [inner, TypeError("b")])  # Creates nested group

# Cause 5: Not handling partial matches
try:
    raise ExceptionGroup("mixed", [ValueError("a"), TypeError("b")])
except* ValueError:
    print("value error")
# TypeError is unhandled - will propagate as unhandled exception
```

## How to Fix

### Fix 1: Use except* for ExceptionGroup handling

```python
# Wrong - regular except doesn't catch ExceptionGroup
try:
    raise ExceptionGroup("errors", [ValueError("bad"), TypeError("wrong")])
except ValueError:
    print("caught value error")  # Never reached

# Correct - use except*
try:
    raise ExceptionGroup("errors", [ValueError("bad"), TypeError("wrong")])
except* ValueError as eg:
    print(f"Value errors: {eg.exceptions}")
except* TypeError as eg:
    print(f"Type errors: {eg.exceptions}")
```

### Fix 2: Raise ExceptionGroup correctly

```python
# Wrong - non-exception objects in the group
raise ExceptionGroup("errors", ["not an exception", ValueError("good")])  # TypeError

# Correct - all items must be exceptions
raise ExceptionGroup("errors", [
    ValueError("first error"),
    TypeError("second error"),
    RuntimeError("third error"),
])

# For single exceptions, wrap in list
raise ExceptionGroup("error", [ValueError("single")])
```

### Fix 3: Handle partial except* matches properly

```python
# Wrong - not handling all exception types
try:
    process_multiple_tasks()
except* ValueError as eg:
    handle_value_errors(eg)
# TypeError propagates unhandled

# Correct - handle all expected exception types
try:
    process_multiple_tasks()
except* ValueError as eg:
    handle_value_errors(eg)
except* TypeError as eg:
    handle_type_errors(eg)
except* Exception as eg:
    handle_other_errors(eg)
```

### Fix 4: Flatten nested ExceptionGroups

```python
# Nested groups can be confusing
inner = ExceptionGroup("inner", [ValueError("a")])
outer = ExceptionGroup("outer", [inner, TypeError("b")])

# Use .split() to separate by exception type
value_errors, rest = outer.split(ValueError)
if value_errors:
    print(f"Got {len(value_errors.exceptions)} value errors")
if rest:
    print(f"Remaining: {rest}")

# Or use .subgroup() to get matching exceptions
value_group = outer.subgroup(ValueError)
if value_group:
    for exc in value_group.exceptions:
        print(f"ValueError: {exc}")
```

### Fix 5: Create ExceptionGroup with correct nesting

```python
# Correct way to build nested groups
def create_error_group(errors):
    if not errors:
        return None
    by_type = {}
    for exc in errors:
        by_type.setdefault(type(exc).__name__, []).append(exc)
    groups = []
    for exc_type, excs in by_type.items():
        if len(excs) == 1:
            groups.append(excs[0])
        else:
            groups.append(ExceptionGroup(exc_type, excs))
    if len(groups) == 1:
        return groups[0]
    return ExceptionGroup("combined", groups)
```

## Examples

```python
# Practical: collecting errors from parallel validation
def validate_user(data):
    errors = []
    if not data.get("name"):
        errors.append(ValueError("Name is required"))
    if not data.get("email"):
        errors.append(ValueError("Email is required"))
    if data.get("age", 0) < 0:
        errors.append(ValueError("Age must be positive"))
    if errors:
        raise ExceptionGroup("Validation failed", errors)

# Handling with except*
try:
    validate_user({"name": "", "email": "", "age": -1})
except* ValueError as eg:
    for exc in eg.exceptions:
        print(f"Validation error: {exc}")

# Using BaseExceptionGroup for non-Exception subclasses
import asyncio

async def fetch_all(urls):
    async def fetch(url):
        try:
            return await asyncio.get_event_loop().run_in_executor(None, fetch_url, url)
        except Exception as e:
            return e
    results = await asyncio.gather(*[fetch(url) for url in urls])
    errors = [r for r in results if isinstance(r, Exception)]
    successes = [r for r in results if not isinstance(r, Exception)]
    if errors:
        raise ExceptionGroup("Fetch errors", errors)
    return successes
```

## Related Errors

- [BaseException](../baseexception) — Base exception class
- [python-taskgroup-error](../python-taskgroup-error) — asyncio.TaskGroup with ExceptionGroup
- [RuntimeError](../runtimeerror) — Runtime errors
- [python311-deprecation](../python311-deprecation) — Python 3.11 changes
