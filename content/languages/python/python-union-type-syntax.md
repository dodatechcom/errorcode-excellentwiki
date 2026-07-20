---
title: "[Solution] Python 3.10+ X | Y Union Type Syntax — Type Hints, isinstance, Optional"
description: "Fix Python 3.10+ union type syntax errors including X | Y type hints, isinstance() with unions, runtime type checking, and Optional migration."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 514
---

# Python 3.10+ X | Y Union Type Syntax — Type Hints, isinstance, Optional

Python 3.10 introduced `X | Y` as a union type syntax alternative to `Union[X, Y]` and `Optional[X]`. Errors occur when using this syntax in older Python versions, with `isinstance()`, or in runtime type evaluation contexts.

## Common Causes

```python
# Cause 1: Using | syntax in Python < 3.10
def greet(name: str | None) -> str:  # SyntaxError in Python 3.9 and below
    return f"Hello {name}"

# Cause 2: Using | with isinstance (not supported)
value = "hello"
if isinstance(value, str | None):  # TypeError in Python 3.10+
    print("string or None")

# Cause 3: | syntax in runtime type evaluation
value: str | int = "hello"
print(type(value) == str | int)  # TypeError - can't use | with type()

# Cause 4: Old Optional syntax still in use
from typing import Optional
def greet(name: Optional[str]) -> Optional[str]:  # Works but verbose
    return f"Hello {name}"

# Cause 5: Mixed old and new syntax confusion
from typing import Union
def process(data: Union[str | int]) -> str:  # Redundant mixing
    return str(data)
```

## How to Fix

### Fix 1: Use proper union syntax for Python 3.10+

```python
# Wrong - using | syntax in Python < 3.10
def greet(name: str | None) -> str:
    return f"Hello {name}"

# Correct - use typing for compatibility
from typing import Optional, Union

def greet(name: Optional[str]) -> str:  # Optional[str] is Union[str, None]
    return f"Hello {name}"

# Or use Union for multiple types
def process(data: Union[str, int, float]) -> str:
    return str(data)

# For Python 3.10+ only
def greet(name: str | None) -> str:
    return f"Hello {name}"
```

### Fix 2: Fix isinstance with union types

```python
# Wrong - can't use | with isinstance directly in Python < 3.10
value = "hello"
if isinstance(value, str | None):  # TypeError in < 3.10
    print("string")

# Correct for Python 3.10+
value = "hello"
if isinstance(value, str | None):  # Works in 3.10+
    print("string")

# Correct for older Python
from typing import Union
if isinstance(value, (str, type(None))):  # Use tuple
    print("string")

# Or check explicitly
if isinstance(value, str) or value is None:
    print("string or None")
```

### Fix 3: Use | syntax for type aliases

```python
# Old style
from typing import Union, List, Dict
JSON = Union[str, int, float, bool, None, List["JSON"], Dict[str, "JSON"]]

# New style (Python 3.10+)
type JSON = str | int | float | bool | None | list["JSON"] | dict[str, "JSON"]

# Or using TypeAlias (3.10+)
from typing import TypeAlias
JSON: TypeAlias = str | int | float | bool | None | list["JSON"] | dict[str, "JSON"]
```

### Fix 4: Migrate Optional to | syntax

```python
# Old style
from typing import Optional
def find_user(user_id: int) -> Optional[dict]:
    if user_id in users:
        return users[user_id]
    return None

# New style (Python 3.10+)
def find_user(user_id: int) -> dict | None:
    if user_id in users:
        return users[user_id]
    return None
```

### Fix 5: Use typing.get_type_hints for runtime evaluation

```python
# Wrong - evaluating union type at runtime
from typing import get_type_hints
hints = get_type_hints(my_func)  # Works but union types evaluate differently

# Correct - use | for clean type hints
def process(data: str | int | float) -> str:
    return str(data)

# For runtime type checking
def check_type(value, expected_type):
    import typing
    origin = getattr(expected_type, "__origin__", None)
    if origin is typing.Union:
        return isinstance(value, expected_type.__args__)
    return isinstance(value, expected_type)
```

## Examples

```python
# API response typing with unions
from typing import TypeAlias

# Old
from typing import Union, Optional
APIResponse = Union[dict, list, str, None]

# New (Python 3.10+)
APIResponse: TypeAlias = dict | list | str | None

def handle_response(data: APIResponse) -> str:
    match data:
        case dict(d):
            return str(d)
        case list(l):
            return str(l)
        case str(s):
            return s
        case None:
            return "No data"

# Function with multiple return types
def parse_input(value: str) -> int | float | str | None:
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            if value.strip():
                return value.strip()
            return None

# Type guard with union
from typing import TypeGuard

def is_string_list(val: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in val)

def process(items: list[str | int]) -> str:
    if is_string_list(items):
        return ", ".join(items)  # Type checker knows items is list[str]
    return str(items)
```

## Related Errors

- [python-typing-error](../python-typing-error) — General typing errors
- [python-typing-self-error](../python-typing-self-error) — Self type usage
- [python310-deprecation](../python310-deprecation) — Python 3.10 changes
- [mypy-error](../mypy-error) — Type checking errors
