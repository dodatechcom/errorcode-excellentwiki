---
title: "[Solution] Python 3.8 Deprecation — Positional-Only Params, Walrus Operator, importlib.resources"
description: "Fix Python 3.8 deprecation warnings from positional-only parameter syntax, walrus operator changes, and importlib.resources updates."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 506
---

# Python 3.8 Deprecation — Positional-Only Params, Walrus Operator, importlib.resources

Python 3.8 introduced the positional-only parameter syntax (`/`) and the walrus operator (`:=`), while deprecating several older patterns. Code using `**kwargs` hacks for positional-only behavior or older `importlib.resources` APIs needs updating.

## Common Causes

```python
# Cause 1: Using **kwargs to enforce positional-only (old pattern)
def old_positional_only(a, b, **kwargs):
    if kwargs:
        raise TypeError("unexpected keyword arguments")
    return a + b

old_positional_only(1, 2, c=3)  # Should be caught but pattern is ugly

# Cause 2: Old importlib.resources API
from importlib.resources import read_text, read_binary  # Deprecated in 3.11

# Cause 3: Using os.popen (deprecated behavior)
import os
result = os.popen("ls").read()  # subprocess.run preferred

# Cause 4: Old-style string formatting with deprecated features
value = 1.5
f"{value:.2f}"  # Fine, but old format() patterns may warn

# Cause 5: Deprecated typing patterns
from typing import Dict, List, Optional  # Still works but Union[] style deprecated later
```

## How to Fix

### Fix 1: Use positional-only parameter syntax

```python
# Wrong — using **kwargs hack for positional-only
def multiply(a, b, **kwargs):
    if kwargs:
        raise TypeError("multiply() takes 2 positional arguments")
    return a * b

# Correct — use / syntax (Python 3.8+)
def multiply(a, b, /):
    return a * b

multiply(3, 4)     # Works
multiply(3, b=4)   # TypeError: multiply() got an unexpected keyword argument 'b'

# Mix positional-only with regular parameters
def func(a, b, /, c, d):
    return a + b + c + d

func(1, 2, 3, d=4)  # Works
func(1, 2, c=3, d=4)  # Works
```

### Fix 2: Update importlib.resources usage

```python
# Wrong — deprecated importlib.resources API (removed in 3.12)
from importlib.resources import read_text, read_binary
data = read_text("my_package", "data.txt")

# Correct — use importlib.resources.files (3.9+)
from importlib.resources import files
data = files("my_package").joinpath("data.txt").read_text()

# For binary data
data = files("my_package").joinpath("data.bin").read_bytes()

# For packages with subdirectories
data = files("my_package.subpackage").joinpath("config.json").read_text()
```

### Fix 3: Use subprocess instead of os.popen

```python
# Wrong — os.popen deprecated
import os
result = os.popen("ls -la").read()

# Correct — use subprocess
import subprocess
result = subprocess.run(
    ["ls", "-la"],
    capture_output=True,
    text=True
).stdout

# Or for simple cases
result = subprocess.check_output(["ls", "-la"], text=True)
```

### Fix 4: Modern typing annotations

```python
# Wrong — old typing imports (deprecated in 3.9)
from typing import Dict, List, Optional, Tuple, Set

# Correct — use built-in generics (3.9+)
def process(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

def find_first(items: list[str]) -> str | None:
    return items[0] if items else None
```

## Examples

```python
# Full migration of a function using old positional-only pattern
# Old:
# def connect(host, port, **kwargs):
#     timeout = kwargs.get("timeout", 30)
#     retries = kwargs.get("retries", 3)
#     if any(k not in ("timeout", "retries") for k in kwargs):
#         raise TypeError("unexpected keyword arguments")
#     return f"Connecting to {host}:{port}"

# New:
def connect(host, port, /, timeout=30, retries=3):
    return f"Connecting to {host}:{port}"

connect("localhost", 8080)  # Works
connect("localhost", 8080, timeout=10)  # Works
connect(host="localhost", port=8080)  # TypeError

# Resource loading migration
# Old:
# from importlib.resources import read_text
# config = read_text("myapp", "config.json")

# New:
from importlib.resources import files
config = files("myapp").joinpath("config.json").read_text()

# Walrus operator usage (introduced in 3.8)
# Useful for assignment expressions in conditions
data = [1, 2, 3, 4, 5]

# Old pattern:
# result = compute(x)
# if result > 0:
#     process(result)

# New with walrus:
# if (result := compute(x)) > 0:
#     process(result)

# In list comprehensions
# filtered = [y for x in data if (y := process(x)) is not None]
```

## Related Errors

- [python-positional-only-params](../python-positional-only-params) — Positional-only parameter errors
- [walrus-operator](../walrus-operator) — Walrus operator issues
- [python-union-type-syntax](../python-union-type-syntax) — Modern type hint syntax
- [python310-deprecation](../python310-deprecation) — Python 3.10 deprecation changes
