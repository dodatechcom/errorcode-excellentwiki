---
title: "[Solution] Python attrs or dataclass Error — How to Fix"
description: "Fix Python attrs and dataclass errors. Resolve init, frozen, and validator issues with attrs and dataclasses."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python attrs or dataclass Error

A `TypeError` or `AttributeError` from `attrs` or `dataclasses` occurs when class definitions conflict with runtime expectations. These libraries generate `__init__`, `__repr__`, and comparison methods automatically, but misconfiguration causes subtle failures.

## Why It Happens

attrs and dataclasses generate boilerplate code for `__init__`, `__repr__`, `__eq__`, and other dunder methods. When you override or misconfigure these generated methods, Python raises errors about unexpected arguments, frozen attribute assignment, or field ordering violations.

## Common Error Messages

- `TypeError: __init__() got an unexpected keyword argument`
- `AttributeError: cannot assign to field in frozen dataclass`
- `TypeError: non-default argument follows default argument`
- `FrozenInstanceError: cannot assign to frozen attribute`

## How to Fix It

### Fix 1: Add __init__ generation explicitly

```python
from dataclasses import dataclass

@dataclass
class Config:
    name: str
    count: int = 0

    def __post_init__(self):
        if self.count < 0:
            raise ValueError('count must be non-negative')

config = Config(name='test', count=5)
```

### Fix 2: Fix field ordering

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str          # required - no default
    age: int = 0        # default - must come after required
    email: str = ''     # default - must come last
```

### Fix 3: Use attrs validators properly

```python
import attr

@attr.s
class User:
    name = attr.ib(validator=attr.validators.instance_of(str))
    age = attr.ib(validator=[
        attr.validators.instance_of(int),
        attr.validators.gt(0)
    ])

user = User(name='Alice', age=25)
```

### Fix 4: Unfreeze dataclass for mutation

```python
from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Config:
    name: str
    value: int

config = Config('key', 1)
new_config = replace(config, value=10)
```

## Common Scenarios

- **Dataclass inheritance** — Child class overrides a field type without calling super().__init__() properly.
- **attrs slot classes** — slots=True prevents setting undeclared attributes on instances.
- **Serialization with slots** — Dataclass instances lack __dict__ when using slots=True, breaking some serialization.

## Prevent It

- Use __post_init__ for validation instead of custom __init__ methods
- Order fields with defaults after fields without defaults
- Use replace() from dataclasses to create modified copies of frozen instances

## Related Errors

- - [TypeError](/languages/python/typeerror/) — unsupported operand type
- - [AttributeError](/languages/python/attributeerror/) — object has no attribute
