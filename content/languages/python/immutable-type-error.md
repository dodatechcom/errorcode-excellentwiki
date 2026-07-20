---
title: "[Solution] Python TypeError — 'TYPE' object does not support item assignment"
description: "Fix Python TypeError when trying to assign items to immutable types like tuple, str, bytes. Learn about immutability and frozen data structures."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 707
---

# Python TypeError — 'TYPE' object does not support item assignment

A `TypeError` with the message `'tuple' object does not support item assignment` (or similar for `str`, `bytes`, `frozenset`, etc.) is raised when you try to modify an immutable object. Immutable objects cannot be changed after creation — any operation that appears to modify them actually creates a new object.

## Common Causes

```python
# Cause 1: Assigning to a tuple element
t = (1, 2, 3)
t[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Cause 2: Assigning to a string character
s = "hello"
s[0] = "H"  # TypeError: 'str' object does not support item assignment

# Cause 3: Assigning to a bytes element
b = b"hello"
b[0] = 72  # TypeError: 'bytes' object does not support item assignment

# Cause 4: Modifying a named tuple field
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
p.x = 10  # TypeError: can't set attribute

# Cause 5: Modifying a frozenset
fs = frozenset([1, 2, 3])
fs.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'

# Cause 6: Mutating a frozen dataclass
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    host: str
    port: int

config = Config("localhost", 8080)
config.host = "example.com"  # TypeError: cannot assign to field 'host'
```

## How to Fix

### Fix 1: Use a list instead of a tuple for mutable data

```python
# Wrong — tuple doesn't support item assignment
t = (1, 2, 3)
t[0] = 10  # TypeError

# Correct — use a list
t = [1, 2, 3]
t[0] = 10  # Works
print(t)   # [10, 2, 3]
```

### Fix 2: Create a new tuple with modified values

```python
# Wrong
t = (1, 2, 3)
t[0] = 10  # TypeError

# Correct — create a new tuple
t = (1, 2, 3)
t = (10,) + t[1:]  # (10, 2, 3)
print(t)

# Or using unpacking
t = (1, 2, 3)
t = (10, *t[1:])
print(t)  # (10, 2, 3)
```

### Fix 3: Use string methods that return new strings

```python
# Wrong
s = "hello"
s[0] = "H"  # TypeError

# Correct — create a new string
s = "hello"
s = "H" + s[1:]  # "Hello"
print(s)

# Or use str.replace()
s = "hello"
s = s.replace("h", "H")  # "Hello"
print(s)
```

### Fix 4: Use a mutable alternative to frozen dataclass

```python
# Wrong — frozen dataclass
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    host: str
    port: int

config = Config("localhost", 8080)
config.host = "example.com"  # TypeError

# Correct — use regular dataclass
@dataclass
class Config:
    host: str
    port: int

config = Config("localhost", 8080)
config.host = "example.com"  # Works
print(config)  # Config(host='example.com', port=8080)
```

### Fix 5: Use replace() for named tuples and frozen dataclasses

```python
from collections import namedtuple
from dataclasses import dataclass, replace

# Named tuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
p = p._replace(x=10)  # Point(x=10, y=2)
print(p)

# Frozen dataclass
@dataclass(frozen=True)
class Config:
    host: str
    port: int

config = Config("localhost", 8080)
config = replace(config, host="example.com")  # Config(host='example.com', port=8080)
print(config)
```

## Examples

```python
# Real-world: Updating configuration
from dataclasses import dataclass, replace

@dataclass(frozen=True)
class DatabaseConfig:
    host: str
    port: int
    username: str

config = DatabaseConfig("localhost", 5432, "admin")

# Wrong — can't modify frozen dataclass
# config.port = 5433  # TypeError

# Correct — use replace()
production_config = replace(config, host="prod.db.example.com", port=5433)
print(production_config)

# Real-world: Working with immutable coordinate data
from collections import namedtuple

Coordinate = namedtuple("Coordinate", ["lat", "lon"])

def move_coordinate(coord, lat_delta, lon_delta):
    # Can't modify namedtuple, return new one
    return Coordinate(coord.lat + lat_delta, coord.lon + lon_delta)

origin = Coordinate(0.0, 0.0)
moved = move_coordinate(origin, 1.5, 2.3)
print(moved)  # Coordinate(lat=1.5, lon=2.3)
```

## Related Errors

- [TypeError](../typeerror) — general type mismatch errors.
- [AttributeError](../attributeerror) — object has no attribute.
- [Slots error](slots-error) — __slots__ restrictions on attribute creation.
