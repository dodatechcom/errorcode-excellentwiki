---
title: "[Solution] Python TypeError — 'TYPE' object does not support item assignment (slots)"
description: "Fix Python TypeError related to __slots__ restrictions. Understand __slots__ limitations, dynamic attribute creation, and __dict__ vs __slots__."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 713
---

# Python TypeError — 'TYPE' object does not support item assignment (slots)

A `TypeError` with the message `'TYPE' object does not support item assignment` related to `__slots__` is raised when you try to set an attribute on an object that uses `__slots__` but the attribute name is not defined in the `__slots__` declaration. Classes with `__slots__` restrict attribute creation to only those names listed in `__slots__`.

## Common Causes

```python
# Cause 1: Setting an attribute not in __slots__
class Point:
    __slots__ = ("x", "y")

p = Point()
p.x = 1
p.y = 2
p.z = 3  # AttributeError: 'Point' object has no attribute 'z'

# Cause 2: Trying to create __dict__ on slotted class
class Point:
    __slots__ = ("x", "y")

p = Point()
p.__dict__  # AttributeError: 'Point' object has no attribute '__dict__'

# Cause 3: Inherited slotted class without updating __slots__
class Base:
    __slots__ = ("x",)

class Child(Base):
    pass  # No __slots__ defined — gets __dict__

child = Child()
child.x = 1
child.new_attr = 2  # Works — Child has __dict__

# Cause 4: Trying to use **kwargs with slotted class
class Point:
    __slots__ = ("x", "y")

p = Point(**{"x": 1, "y": 2, "z": 3})  # TypeError: unexpected keyword argument 'z'

# Cause 5: Multiple inheritance with __slots__
class A:
    __slots__ = ("x",)

class B:
    __slots__ = ("y",)

class C(A, B):
    __slots__ = ()  # Merged slots

c = C()
c.x = 1
c.y = 2
c.z = 3  # AttributeError
```

## How to Fix

### Fix 1: Only set attributes defined in __slots__

```python
# Wrong
class Point:
    __slots__ = ("x", "y")

p = Point()
p.z = 3  # AttributeError

# Correct — only set defined attributes
class Point:
    __slots__ = ("x", "y")

p = Point()
p.x = 1
p.y = 2
print(p.x, p.y)  # 1 2
```

### Fix 2: Include all needed attributes in __slots__

```python
# Wrong — missing 'z'
class Point:
    __slots__ = ("x", "y")

p = Point()
p.x = 1
p.y = 2
p.z = 3  # AttributeError

# Correct — include all needed attributes
class Point:
    __slots__ = ("x", "y", "z")

p = Point()
p.x = 1
p.y = 2
p.z = 3
print(p.x, p.y, p.z)  # 1 2 3
```

### Fix 3: Define __slots__ in all classes in the hierarchy

```python
# Wrong — Child gets __dict__ because it doesn't define __slots__
class Base:
    __slots__ = ("x",)

class Child(Base):
    pass

child = Child()
child.new_attr = "anything"  # Works — but wastes memory

# Correct — define __slots__ in Child too
class Base:
    __slots__ = ("x",)

class Child(Base):
    __slots__ = ("y",)  # Only adds 'y' to Base's slots

child = Child()
child.x = 1
child.y = 2
# child.new_attr = "anything"  # AttributeError
```

### Fix 4: Allow optional extra attributes with __dict__

```python
class Point:
    __slots__ = ("x", "y", "__dict__")  # Allow __dict__ for extra attributes

p = Point()
p.x = 1
p.y = 2
p.z = 3  # Works — goes into __dict__
print(p.__dict__)  # {'z': 3}
```

## Examples

```python
# Real-world: Memory-efficient class with slots
class User:
    __slots__ = ("name", "email", "age")

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

# Create many users — much less memory than __dict__
users = [User(f"user{i}", f"user{i}@example.com", i) for i in range(10000)]

# Each user only stores the defined slots
u = User("Alice", "alice@example.com", 30)
print(u.name, u.email, u.age)  # Alice alice@example.com 30

# Trying to set undefined attribute raises AttributeError
# u.phone = "555-1234"  # AttributeError

# Real-world: Slotted class with validation
class ValidatedPoint:
    __slots__ = ("_x", "_y")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x must be a number")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y must be a number")
        self._y = value

p = ValidatedPoint()
p.x = 1.5
p.y = 2.5
print(p.x, p.y)  # 1.5 2.5
```

## Related Errors

- [Immutable type error](immutable-type-error) — immutability restrictions.
- [AttributeError](../attributeerror) — object has no attribute.
- [TypeError](../typeerror) — general type mismatch errors.
