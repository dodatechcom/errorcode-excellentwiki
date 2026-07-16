---
title: "[Solution] Python TypeError: argument of type 'NoneType' is not iterable"
description: "Fix Python TypeError: argument of type 'NoneType' is not iterable. Add null checks before using 'in' operator on values that may be None."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["typeerror", "nonetype", "iterable", "none", "in-operator"]
weight: 5
---

# TypeError: argument of type 'NoneType' is not iterable

A `TypeError` with the message `argument of type 'NoneType' is not iterable` is raised when you use the `in` operator on `None`. This means a variable you expected to be a list, string, dict, or other collection is actually `None`.

## Description

The `in` operator checks membership in a collection. Python requires the right-hand side to implement `__iter__` or `__contains__`. Since `None` implements neither, the operation fails. This typically means a function returned `None` and the code didn't check for it.

Common patterns:

- **Function returns `None` implicitly** — no `return` statement or bare `return`.
- **Dictionary `.get()` returns `None`** — key missing and no default provided.
- **Variable never assigned** — declared but not initialized before use.
- **Optional value not checked** — database query returned no result.

## Common Causes

```python
# Cause 1: Function without explicit return
def find_user(user_id):
    user = db.query(user_id)
    if not user:
        return  # Returns None implicitly

result = find_user(42)
if "admin" in result:  # TypeError: argument of type 'NoneType' is not iterable
    print("Admin found")

# Cause 2: Dictionary .get() returns None
config = {"host": "localhost"}
port = config.get("port")  # Returns None
if 8080 in port:  # TypeError
    print("Port found")

# Cause 3: Uninitialized variable
data = None
if "key" in data:  # TypeError
    print("Found")

# Cause 4: Pandas DataFrame operations returning None
df = None
if "column" in df:  # TypeError
    print("Column exists")
```

## How to Fix

### Fix 1: Add a None check before using `in`

```python
# Wrong
result = find_user(42)
if "admin" in result:
    print("Admin found")

# Correct
result = find_user(42)
if result is not None and "admin" in result:
    print("Admin found")
```

### Fix 2: Provide a default value for `.get()`

```python
# Wrong
port = config.get("port")
if 8080 in port:
    print("Default port")

# Correct
port = config.get("port", [])
if 8080 in port:
    print("Default port")
```

### Fix 3: Use a default empty collection

```python
# Wrong
data = get_something()  # May return None
if "key" in data:
    process(data)

# Correct
data = get_something() or []
if "key" in data:
    process(data)
```

### Fix 4: Use a guard clause for functions that return None

```python
def find_user(user_id):
    user = db.query(user_id)
    if not user:
        return None
    return user

user = find_user(42)
if user is None:
    print("User not found")
elif "admin" in user["roles"]:
    print("Admin found")
```

## Examples

This error commonly occurs when:

- A database query returns no results and the result is used without checking
- A dictionary `.get()` with no default is used with `in`
- An optional dependency returns `None` when the feature is unavailable
- A list comprehension filters to an empty result that becomes `None`

## Related Errors

- [TypeError: unhashable type](typeerror-hashable) — using a non-hashable type as a dict key
- [AttributeError](#) — calling a method on `None` instead of using `in`
- [KeyError](#) — accessing a missing dictionary key
