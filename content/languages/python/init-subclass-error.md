---
title: "[Solution] Python TypeError — error in __init_subclass__"
description: "Fix Python TypeError in __init_subclass__. Handle metaclass conflicts, class hierarchy errors, and __set_name__ protocol issues."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 712
---

# Python TypeError — error in __init_subclass__

A `TypeError` raised during `__init_subclass__` occurs when there's an error in the subclass initialization hook or when there's a metaclass conflict in the class hierarchy. The `__init_subclass__` method is called when a class is defined as a subclass of another, and errors here can cause confusing `TypeError` messages.

## Common Causes

```python
# Cause 1: __init_subclass__ with wrong arguments
class Base:
    def __init_subclass__(cls, required_attr=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if required_attr is None:
            raise TypeError(f"{cls.__name__} must define 'required_attr'")

class GoodChild(Base, required_attr="hello"):  # Works
    pass

class BadChild(Base):  # TypeError: BadChild must define 'required_attr'
    pass

# Cause 2: Metaclass conflict
class MetaA(type):
    pass

class MetaB(type):
    pass

class A(metaclass=MetaA):
    pass

class B(metaclass=MetaB):
    pass

class C(A, B):  # TypeError: metaclass conflict
    pass

# Cause 3: __set_name__ protocol error
class Field:
    def __set_name__(self, owner, name):
        if not name.startswith("_"):
            raise TypeError(f"Field {name} must be private (start with _)")
        self.name = name

class MyClass:
    field = Field()  # TypeError if field name doesn't start with _

# Cause 4: __init_subclass__ calling super incorrectly
class Base:
    def __init_subclass__(cls, **kwargs):
        # Forgot to call super().__init_subclass__(**kwargs)
        pass

class Child(Base):  # May cause TypeError in Python 3.6+
    pass

# Cause 5: TypeError from __init_subclass__ validation
class ValidatedBase:
    def __init_subclass__(cls, min_length=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if min_length is not None and not isinstance(min_length, int):
            raise TypeError("min_length must be an integer")
```

## How to Fix

### Fix 1: Always call super().__init_subclass__()

```python
# Wrong
class Base:
    def __init_subclass__(cls, **kwargs):
        pass  # Forgot super()

# Correct
class Base:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

class Child(Base):
    pass
```

### Fix 2: Handle metaclass conflicts explicitly

```python
# Wrong — conflicting metaclasses
class MetaA(type):
    pass

class MetaB(type):
    pass

class A(metaclass=MetaA):
    pass

class B(metaclass=MetaB):
    pass

# class C(A, B):  # TypeError

# Correct — create a shared metaclass
class CombinedMeta(MetaA, MetaB):
    pass

class A(metaclass=CombinedMeta):
    pass

class B(metaclass=CombinedMeta):
    pass

class C(A, B):  # Works
    pass
```

### Fix 3: Validate in __init_subclass__ with proper error messages

```python
class ValidatedBase:
    def __init_subclass__(cls, required_attr=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if required_attr is not None:
            setattr(cls, "_required_attr", required_attr)

class Config(ValidatedBase, required_attr="database"):
    pass

print(Config._required_attr)  # database

# Raise clear errors
class StrictBase:
    def __init_subclass__(cls, must_implement=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if must_implement:
            for method in must_implement:
                if not hasattr(cls, method):
                    raise TypeError(
                        f"{cls.__name__} must implement {method}"
                    )

class Plugin(StrictBase, must_implement=["execute", "validate"]):
    def execute(self):
        pass
    def validate(self):
        pass
```

### Fix 4: Use __set_name__ for automatic attribute naming

```python
class Descriptor:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)

    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)

class MyClass:
    name = Descriptor()
    age = Descriptor()

obj = MyClass()
obj.name = "Alice"
obj.age = 30
print(obj.name, obj.age)  # Alice 30
```

## Examples

```python
# Real-world: Plugin system with __init_subclass__
class Plugin:
    _registry = {}

    def __init_subclass__(cls, plugin_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        name = plugin_name or cls.__name__.lower()
        Plugin._registry[name] = cls

class CSVPlugin(Plugin, plugin_name="csv"):
    def process(self, data):
        return f"Processing CSV: {data}"

class JSONPlugin(Plugin, plugin_name="json"):
    def process(self, data):
        return f"Processing JSON: {data}"

print(Plugin._registry)  # {'csv': <class 'CSVPlugin'>, 'json': <class 'JSONPlugin'>}

# Real-world: ORM-style model with field validation
class Field:
    def __init__(self, field_type):
        self.field_type = field_type

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, self.field_type):
            raise TypeError(f"{self.name} must be {self.field_type.__name__}")
        obj.__dict__[self.name] = value

class Model:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._fields = {
            name: obj for name, obj in cls.__dict__.items()
            if isinstance(obj, Field)
        }

class User(Model):
    name = Field(str)
    age = Field(int)

user = User()
user.name = "Alice"
user.age = 30
print(user.name, user.age)  # Alice 30
```

## Related Errors

- [TypeError](../typeerror) — general type mismatch errors.
- [Cannot create instance](cannot-create-instance) — instance creation errors.
- [AttributeError](../attributeerror) — object has no attribute.
