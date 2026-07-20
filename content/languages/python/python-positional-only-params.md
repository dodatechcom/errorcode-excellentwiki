---
title: "[Solution] Python 3.8+ Positional-Only Parameters — / Syntax, Keyword Argument Errors"
description: "Fix Python 3.8+ positional-only parameter errors including / syntax usage, keyword argument rejection, migration from **kwargs patterns, and C extension compatibility."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 513
---

# Python 3.8+ Positional-Only Parameters — / Syntax, Keyword Argument Errors

Python 3.8 introduced positional-only parameters using the `/` syntax. Errors occur when callers try to pass positional-only arguments as keywords, or when migrating from the old `**kwargs` pattern used to enforce positional-only behavior.

## Common Causes

```python
# Cause 1: Passing positional-only argument as keyword
def func(a, b, /):
    return a + b

func(a=1, b=2)  # TypeError: func() got some positional-only arguments

# Cause 2: Confusing positional-only with keyword-only
def func(a, b, /, c, d):  # a, b positional-only; c, d can be either
    pass

func(1, 2, c=3, d=4)   # Works
func(1, 2, 3, d=4)     # Works
func(a=1, b=2, c=3, d=4)  # TypeError - a, b are positional-only

# Cause 3: Old **kwargs pattern still in use
def old_style(a, b, **kwargs):
    if kwargs:
        raise TypeError("unexpected keyword arguments")
    return a + b

old_style(1, 2, c=3)  # Should raise but pattern is ugly

# Cause 4: C extension functions with positional-only params
# Built-in functions like len(), print() are positional-only
len([1, 2, 3])    # Works
len(obj=[1, 2, 3])  # TypeError

# Cause 5: Mixing positional-only with default values
def func(a, b=10, /):
    return a + b

func(5)      # Works - uses default b=10
func(5, 15)  # Works - b=15
func(a=5)    # TypeError - a is positional-only
```

## How to Fix

### Fix 1: Use positional-only syntax correctly

```python
# Wrong - allowing keyword arguments for internal params
def connect(host, port, timeout=30, retries=3):
    pass

connect(host="localhost", port=8080)  # Works but not ideal for refactoring

# Correct - use / for parameters that should be positional only
def connect(host, port, /, timeout=30, retries=3):
    pass

connect("localhost", 8080)              # Works
connect("localhost", 8080, timeout=10)  # Works - timeout is keyword-able
connect(host="localhost", port=8080)    # TypeError - host, port are positional-only
```

### Fix 2: Migrate from **kwargs enforcement

```python
# Wrong - old **kwargs hack
def multiply(a, b, **kwargs):
    if kwargs:
        raise TypeError(f"multiply() got unexpected keyword arguments: {kwargs}")
    return a * b

# Correct - use / syntax
def multiply(a, b, /):
    return a * b

multiply(3, 4)      # Returns 12
multiply(3, b=4)    # TypeError
```

### Fix 3: Understand positional-only vs keyword-only

```python
# Positional-only (/) - must be passed by position
# Keyword-only (*) - must be passed by name
# Normal - can be passed either way

def example(pos_only, /, normal, *, kw_only):
    print(f"pos_only={pos_only}, normal={normal}, kw_only={kw_only}")

example(1, 2, kw_only=3)      # Works: pos_only=1, normal=2, kw_only=3
example(1, normal=2, kw_only=3)  # Works
example(1, 2, 3)              # TypeError - kw_only must be keyword
example(pos_only=1, normal=2, kw_only=3)  # TypeError - pos_only is positional-only
```

### Fix 4: Handle built-in positional-only functions

```python
# Built-in functions are positional-only
len([1, 2, 3])       # Works
len(obj=[1, 2, 3])   # TypeError

sorted([3, 1, 2])    # Works
sorted(iterable=[3, 1, 2])  # TypeError

# Solution: pass as positional arguments
len(my_list)
sorted(my_list)
```

### Fix 5: Use positional-only for API stability

```python
# Good practice: internal parameters as positional-only
def _internal_impl(data, encoding, /):
    """Internal function - don't let callers use keyword args
    so we can rename parameters later without breaking API."""
    return data.decode(encoding)

# Public API - allow both positional and keyword
def public_api(data, encoding="utf-8"):
    """Public function - keyword args for readability."""
    return _internal_impl(data, encoding)
```

## Examples

```python
# Data processing with positional-only params
def normalize(value, min_val, max_val, /):
    """Normalize value to 0-1 range. min_val and max_val are positional-only."""
    return (value - min_val) / (max_val - min_val)

normalize(0.5, 0.0, 1.0)      # Works
normalize(5, 0, 10)           # Works
normalize(value=0.5, min_val=0.0, max_val=1.0)  # TypeError

# API endpoint handler
def handle_request(method, path, /, headers=None, body=None):
    """method and path are positional-only, headers and body are keyword-optional."""
    return {"method": method, "path": path, "headers": headers, "body": body}

handle_request("GET", "/api/users")
handle_request("POST", "/api/users", headers={"Content-Type": "application/json"}, body=b"data")
```

## Related Errors

- [TypeError](../typeerror) — Wrong argument types
- [python38-deprecation](../python38-deprecation) — Python 3.8 deprecation changes
- [python310-deprecation](../python310-deprecation) — Python 3.10 changes
- [method-argument](../method-argument) — Method argument errors
