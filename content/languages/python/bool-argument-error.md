---
title: "[Solution] Python TypeError — argument of type 'bool' is not iterable"
description: "Fix Python TypeError: argument of type 'bool' is not iterable. Learn proper usage of 'in' operator and isinstance() with booleans."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 709
---

# Python TypeError — argument of type 'bool' is not iterable

A `TypeError` with the message `argument of type 'bool' is not iterable` is raised when you use the `in` operator on a boolean value (`True` or `False`). Booleans are not iterable — they are scalar values. This commonly happens due to operator confusion or misuse of `isinstance()`.

## Common Causes

```python
# Cause 1: Using 'in' operator on a boolean
result = True
if "x" in result:  # TypeError: argument of type 'bool' is not iterable
    print("found")

# Cause 2: Confusing 'in' with 'is'
is_valid = True
if "True" in is_valid:  # TypeError
    print("valid")

# Cause 3: Using 'in' on the result of a comparison
items = [1, 2, 3]
found = 2 in items  # found is True (a bool)
if "something" in found:  # TypeError
    print("found")

# Cause 4: Passing boolean to a function expecting iterable
def find_item(collection, item):
    return item in collection

find_item(True, "something")  # TypeError

# Cause 5: Using 'in' on isinstance() result
if "str" in isinstance("hello", str):  # TypeError
    print("is string")
```

## How to Fix

### Fix 1: Use 'is' or '==' for boolean comparison

```python
# Wrong
result = True
if "True" in result:  # TypeError
    print("found")

# Correct — use 'is' or '=='
result = True
if result is True:
    print("found")

# Or simply
if result:
    print("found")
```

### Fix 2: Use 'in' on the original collection, not on the boolean result

```python
# Wrong
items = [1, 2, 3]
found = 2 in items
if "something" in found:  # TypeError

# Correct — check the boolean directly
items = [1, 2, 3]
if 2 in items:
    print("found")

# Or if you need the boolean
found = 2 in items
if found:
    print("2 is in the list")
```

### Fix 3: Use isinstance() correctly without 'in'

```python
# Wrong
if "str" in isinstance("hello", str):  # TypeError

# Correct — isinstance() returns a bool
if isinstance("hello", str):
    print("is string")

# Or check the type name
if type("hello").__name__ == "str":
    print("is string")
```

### Fix 4: Check the variable type before using 'in'

```python
# Wrong — assuming variable is iterable
def search(data, query):
    return query in data

search(True, "something")  # TypeError if data is a bool

# Correct — validate input type
def search(data, query):
    if not hasattr(data, "__contains__"):
        raise TypeError(f"Expected iterable, got {type(data).__name__}")
    return query in data

# Or handle bool explicitly
def search(data, query):
    if isinstance(data, bool):
        return False  # or raise an error
    return query in data
```

### Fix 5: Use 'is' or 'is not' for None checks

```python
# Wrong — confusing 'in' with 'is'
value = None
if "None" in value:  # TypeError
    print("is None")

# Correct — use 'is'
value = None
if value is None:
    print("is None")

# Or use 'not' for truthiness
value = None
if not value:
    print("is falsy")
```

## Examples

```python
# Real-world: Searching through search results
results = {"query": "python", "total": 100, "items": ["a", "b", "c"]}

# Wrong
if "python" in results.get("found", False):  # TypeError if "found" returns False
    print("found")

# Correct
if results.get("found", False) is True:
    print("found")
# Or check if key exists and has value
if results.get("found"):
    print("found")

# Real-world: Validating API response
response = {"status": 200, "data": {"users": 10}}

# Wrong
if "success" in response.get("ok", False):  # TypeError
    print("API call succeeded")

# Correct
if response.get("ok") is True:
    print("API call succeeded")
# Or more Pythonic
if response.get("ok"):
    print("API call succeeded")

# Real-world: Checking membership in a collection
def check_permission(user, permission):
    # user.permissions is a list
    return permission in user.permissions

class User:
    def __init__(self, permissions):
        self.permissions = permissions

user = User(["read", "write", "execute"])
print(check_permission(user, "read"))  # True

# Wrong usage — passing the bool result instead of the collection
has_permission = check_permission(user, "read")  # True
# if "admin" in has_permission:  # TypeError
#     print("is admin")
```

## Related Errors

- [TypeError](../typeerror) — general type mismatch errors.
- [Bool not iterable](bool-not-iterable) — similar boolean iteration issues.
- [ValueError: bool](valueerror-bool) — boolean value errors.
