---
title: "[Solution] Python Dataclass Error — How to Fix"
description: "Fix Python dataclass errors. Resolve field default issues, frozen dataclass problems, and serialization failures."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Dataclass Error

A `TypeError` or `dataclasses.FrozenInstanceError` occurs when dataclass definitions have invalid default values, frozen instances are modified, or mutable default values are used without `field(default_factory=...)`.

## Why It Happens

Python dataclasses auto-generate `__init__`, `__repr__`, and comparison methods. Errors arise when mutable defaults (like lists or dicts) are used directly, when fields with defaults precede fields without defaults, or when frozen instances are modified.

## Common Error Messages

- `TypeError: non-default argument 'name' follows default argument`
- `TypeError: mutable default <class 'list'> for field`
- `dataclasses.FrozenInstanceError: cannot assign to field 'name'`
- `TypeError: __init__() got an unexpected keyword argument 'extra'`

## How to Fix It

### Fix 1: Fix mutable default values

```python
from dataclasses import dataclass, field
from typing import List

# Wrong — mutable default value shared across instances
# @dataclass
# class User:
#     name: str
#     tags: List[str] = []  # TypeError

# Correct — use field(default_factory=...)
@dataclass
class User:
    name: str
    tags: List[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

user1 = User(name="Alice")
user2 = User(name="Bob")
user1.tags.append("admin")
print(user1.tags)  # ['admin']
print(user2.tags)  # [] — independent instance
```

### Fix 2: Fix field ordering

```python
from dataclasses import dataclass, field

# Wrong — non-default argument follows default argument
# @dataclass
# class User:
#     name: str = "unknown"
#     age: int  # TypeError: no default follows default

# Correct — required fields first, optional fields last
@dataclass
class User:
    name: str
    age: int
    nickname: str = ""
    active: bool = True

user = User(name="Alice", age=25)
print(user)

# Use field with default_factory for complex defaults
@dataclass
class Config:
    host: str
    port: int
    headers: dict = field(default_factory=lambda: {"Content-Type": "application/json"})
```

### Fix 3: Handle frozen dataclasses

```python
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(x=1.0, y=2.0)

# Wrong — cannot modify frozen instance
# p.x = 3.0  # FrozenInstanceError

# Correct — use __post_init__ for derived values
@dataclass(frozen=True)
class Rectangle:
    width: float
    height: float

    @property
    def area(self):
        return self.width * self.height

    def with_width(self, new_width):
        return Rectangle(new_width, self.height)

rect = Rectangle(10, 20)
print(rect.area)  # 200
new_rect = rect.with_width(15)
print(new_rect.area)  # 300
```

### Fix 4: Use InitVar for init-only variables

```python
from dataclasses import dataclass, field, InitVar

@dataclass
class User:
    name: str
    age: int
    raw_data: InitVar[str] = None

    def __post_init__(self, raw_data):
        if raw_data:
            self.name = raw_data.split(",")[0]

user = User(name="Alice", age=25, raw_data="Alice,25,admin")
print(user)

# Serialize and deserialize
import json
from dataclasses import asdict

user_dict = asdict(user)
print(json.dumps(user_dict, indent=2))

# Recreate from dict
user2 = User(**user_dict)
print(user2)
```

## Common Scenarios

- **Mutable default shared** — All instances share the same list or dict default, causing unexpected mutations.
- **Field ordering wrong** — Required fields placed after optional fields causes TypeError at class definition.
- **Frozen modification attempt** — Attempting to set attributes on `frozen=True` dataclasses raises FrozenInstanceError.

## Prevent It

- Always use `field(default_factory=list)` for list defaults and `field(default_factory=dict)` for dict defaults.
- Place required fields before optional fields in dataclass definitions.
- Use `asdict()` and `astuple()` for serialization instead of manual dict construction.

## Related Errors

- [TypeError](/languages/python/typeerror/) — invalid field ordering or mutable default
- [FrozenInstanceError](/languages/python/frozeninstanceerror/) — cannot assign to frozen field
- [AttributeError](/languages/python/attributeerror/) — attribute does not exist
