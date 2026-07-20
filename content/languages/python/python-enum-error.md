---
title: "[Solution] Python Enum Error — Enumeration and Constant Definition Issues"
description: "Fix Python enum errors by handling duplicate values, auto(), enum inheritance, functional API, and unique decorator. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 212
---

# Python Enum Error — Enumeration and Constant Definition Issues

Enum errors occur when duplicate values are used without the `@unique` decorator, when `auto()` is misused, when enum inheritance creates conflicts, or when the functional API is incorrectly applied. Enums provide a way to define named constants with specific behaviors.

## Common Causes

```python
# Duplicate values without @unique
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 1  # Duplicate value — RED and BLUE are aliases

print(Color.RED)  # Color.RED
print(Color.BLUE)  # Color.RED — alias, not a separate member
```

```python
# auto() with mixed manual and automatic values
from enum import Enum, auto

class Status(Enum):
    PENDING = auto()    # 1
    ACTIVE = 5          # Manual value
    INACTIVE = auto()   # 6 — continues from last auto value, not from 5

print(Status.INACTIVE.value)  # 6
```

```python
# Enum inheritance from non-Enum class
from enum import Enum

class Base:
    pass

class BadEnum(Base, Enum):  # TypeError: BadEnum: cannot extend both Enum and <class 'Base'>
    A = 1
```

```python
# Modifying enum values after creation
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

Color.RED = 3  # AttributeError: cannot reassign members
```

```python
# Comparing enums of different types
from enum import Enum

class Color(Enum):
    RED = 1

class Shape(Enum):
    CIRCLE = 1

Color.RED == Shape.CIRCLE  # False — different enum types
Color.RED == 1  # False — enum doesn't compare with int by default
```

## How to Fix

### Fix 1: Use @unique to prevent duplicate values

```python
from enum import Enum, unique

@unique
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3  # All values must be unique

# This will raise ValueError if duplicates exist:
# @unique
# class Bad(Enum):
#     A = 1
#     B = 1  # ValueError: duplicate values found: A, B
```

### Fix 2: Use auto() with custom value generation

```python
from enum import Enum, auto

class Status(Enum):
    def _generate_next_value_(name, start, count, last_values):
        """Custom auto() value generation."""
        return count * 10 + 1
    
    PENDING = auto()    # 1
    ACTIVE = auto()     # 11
    INACTIVE = auto()   # 21

# Or use IntEnum for integer comparison
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

print(Priority.HIGH > Priority.LOW)  # True
print(Priority.HIGH == 3)  # True
```

### Fix 3: Implement enum methods correctly

```python
from enum import Enum

class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    
    def __init__(self, rgb):
        self.rgb = rgb
        self.hex = "#{:02x}{:02x}{:02x}".format(*rgb)
    
    def is_bright(self):
        """Check if color is bright."""
        return sum(self.rgb) > 382
    
    @classmethod
    def from_hex(cls, hex_str):
        """Create Color from hex string."""
        hex_str = hex_str.lstrip("#")
        rgb = tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))
        for color in cls:
            if color.rgb == rgb:
                return color
        raise ValueError(f"No color found for {hex_str}")

print(Color.RED.hex)       # #ff0000
print(Color.GREEN.is_bright())  # True
print(Color.from_hex("#0000ff"))  # Color.BLUE
```

### Fix 4: Use functional API for dynamic enum creation

```python
from enum import Enum

# Create enum dynamically
Animal = Enum("Animal", ["ant", "bee", "cat", "dog"])

print(Animal.ant)       # Animal.ant
print(Animal.ant.value)  # 'ant'

# Or with explicit values
Planet = Enum("Planet", {"MERCURY": 1, "VENUS": 2, "EARTH": 3})

print(Planet.EARTH)       # Planet.EARTH
print(Planet.EARTH.value)  # 3

# Or with (name, value) pairs
HttpStatus = Enum("HttpStatus", [
    ("OK", 200),
    ("NOT_FOUND", 404),
    ("SERVER_ERROR", 500),
])

print(HttpStatus.OK.value)  # 200
```

### Fix 5: Implement __missing__ for default handling

```python
from enum import Enum

class Status(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    
    @classmethod
    def _missing_(cls, value):
        """Handle missing enum values."""
        # Try to find by case-insensitive match
        for member in cls:
            if member.value.lower() == value.lower():
                return member
        # Return default for unknown values
        return cls.PENDING

# Usage
print(Status("active"))      # Status.ACTIVE
print(Status("ACTIVE"))      # Status.ACTIVE (via _missing_)
print(Status("unknown"))     # Status.PENDING (default)
```

## Examples

### State machine with enums

```python
from enum import Enum, auto
from typing import Dict, Callable

class State(Enum):
    IDLE = auto()
    RUNNING = auto()
    PAUSED = auto()
    STOPPED = auto()

class StateMachine:
    def __init__(self):
        self.state = State.IDLE
        self.transitions: Dict[State, Dict[str, State]] = {
            State.IDLE: {"start": State.RUNNING},
            State.RUNNING: {"pause": State.PAUSED, "stop": State.STOPPED},
            State.PAUSED: {"resume": State.RUNNING, "stop": State.STOPPED},
            State.STOPPED: {"reset": State.IDLE},
        }
    
    def transition(self, action: str) -> State:
        if action in self.transitions.get(self.state, {}):
            self.state = self.transitions[self.state][action]
        else:
            raise ValueError(f"Invalid transition: {self.state.value} -> {action}")
        return self.state

sm = StateMachine()
print(sm.state)          # State.IDLE
sm.transition("start")
print(sm.state)          # State.RUNNING
sm.transition("pause")
print(sm.state)          # State.PAUSED
```

### Flag enums for bit operations

```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
    NONE = 0

# Combine permissions
user_perms = Permission.READ | Permission.WRITE
print(user_perms)  # Permission.READ | Permission.WRITE

# Check permissions
print(Permission.READ in user_perms)  # True
print(Permission.EXECUTE in user_perms)  # False

# Add/remove permissions
user_perms |= Permission.EXECUTE
print(user_perms)  # Permission.READ | Permission.WRITE | Permission.EXECUTE

user_perms ^= Permission.WRITE
print(user_perms)  # Permission.READ | Permission.EXECUTE
```

## Related Errors

- [ValueError](/languages/python/valueerror/) — duplicate values or invalid enum creation
- [AttributeError](/languages/python/attributeerror/) — accessing non-existent enum members
- [TypeError](/languages/python/typeerror/) — incorrect enum inheritance or operations
