---
title: "[Solution] Python Abstract Base Class Error — How to Fix"
description: "Fix Python ABC and abstract method errors. Resolve instantiation and implementation issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Abstract Base Class Error

A `TypeError: Can't instantiate abstract class` occurs when Abstract classes prevent instantiation and enforce interface contracts..

## Why It Happens

This happens when concrete classes don't implement required abstract methods, or ABC is instantiated directly. Python enforces strict type and state checking.

## Common Error Messages

- `Can't instantiate abstract class with abstract methods`
- `subclass must override abstract method`
- `metaclass conflict`

## How to Fix It

### Fix 1: Define abstract classes

```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: pass
```

### Fix 2: Use abstract properties

```python
from abc import ABC, abstractmethod
class Animal(ABC):
    @property
    @abstractmethod
    def sound(self) -> str: pass
```

### Fix 3: Register implementations

```python
from abc import ABC
class Serializer(ABC): pass
def serialize(obj): return obj.serialize()
Serializer.register(dict)
```

### Fix 4: Virtual subclasses

```python
from abc import ABC
class MyABC(ABC): pass
class MyClass: pass
MyABC.register(MyClass)
```

## Common Scenarios

- **Missing methods** — Concrete class forgets to implement abstract method.
- **Constructor errors** — Abstract class __init__ not called by super().
- **Multiple inheritance** — Conflicting abstract method implementations.

## Prevent It

- Use ABCMeta and @abstractmethod to enforce contracts
- Always call super().__init__() in concrete classes
- Test by verifying ABCs cannot be instantiated

## Related Errors

- - [TypeError](/languages/python/typeerror/) — unsupported operand type
- - [NotImplementedError](/languages/python/notimplementederror/) — not implemented
