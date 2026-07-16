---
title: "[Solution] Python TypeError — Descriptor Issues"
description: "Fix Python TypeError related to descriptors. Understand how descriptors work and resolve descriptor-related errors in Python."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["typeerror", "descriptor", "class", "attribute"]
weight: 5
---

# TypeError — Descriptor Issues

A `TypeError` related to descriptors is raised when there is a mismatch between how a descriptor is defined and how it is accessed. Descriptors are objects that define `__get__`, `__set__`, or `__delete__` methods, and they underpin methods, properties, and class methods in Python.

## Description

Descriptors are a core Python mechanism. When you access an attribute on an instance, Python checks if the attribute's class defines a `__get__` method. Common descriptor-related errors occur when:

- **Wrong number of arguments** — a descriptor's `__get__` or `__set__` receives unexpected arguments.
- **Descriptor protocol violation** — a descriptor does not implement the required methods.
- **Type mismatch in descriptor** — a non-data descriptor is used where a data descriptor is expected.
- **Instance attribute conflicts** — instance `__dict__` shadows a data descriptor.

## Common Causes

```python
# Cause 1: Descriptor __get__ with wrong arguments
class BadDescriptor:
    def __get__(self, obj, objtype=None):
        pass
    def __set__(self, obj, value):
        pass

class MyClass:
    attr = BadDescriptor()

obj = MyClass()
obj.attr = 10  # May raise TypeError if __set__ signature is wrong

# Cause 2: Inconsistent descriptor protocol
class IncompleteDescriptor:
    def __get__(self, obj, objtype=None):
        return "value"
    # Missing __set__ when setting is attempted

class MyClass:
    attr = IncompleteDescriptor()

obj = MyClass()
obj.attr = 10  # AttributeError or TypeError depending on context

# Cause 3: Wrong type passed to descriptor
class TypedDescriptor:
    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an int")
        obj.__dict__[self.name] = value

class MyClass:
    attr = TypedDescriptor()

obj = MyClass()
obj.attr = "hello"  # TypeError: attr must be an int
```

## Solutions

### Fix 1: Implement the descriptor protocol correctly

```python
# Wrong
class MyDescriptor:
    def __get__(self, obj):
        return "value"

# Correct — __get__ must accept obj and objtype
class MyDescriptor:
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return "value"
```

### Fix 2: Validate types in __set__

```python
class TypedDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an int")
        obj.__dict__[self.name] = value

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, 0)
```

### Fix 3: Use property() for simple descriptors

```python
# Wrong — manual descriptor with errors
class Temperature:
    def __init__(self):
        self._celsius = 0

# Correct — use property
class Temperature:
    def __init__(self):
        self._celsius = 0

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Temperature must be a number")
        self._celsius = value
```

### Fix 4: Use __set_name__ for automatic naming

```python
class ValidatedField:
    def __set_name__(self, owner, name):
        self.storage_name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.storage_name, None)

    def __set__(self, obj, value):
        setattr(obj, self.storage_name, value)
```

## Related Errors

- [AttributeError](../attributeerror) — object has no attribute.
- [TypeError](../typeerror) — general type mismatch errors.
- [Property attribute](property-attribute) — property-related attribute errors.
