---
title: "[Solution] Python AttributeError — 'TYPE' object has no attribute '__get__'"
description: "Fix Python AttributeError related to descriptor protocol. Learn how __get__, __set__, property, classmethod, and staticmethod descriptors work."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 711
---

# Python AttributeError — 'TYPE' object has no attribute '__get__'

An `AttributeError` with the message `'TYPE' object has no attribute '__get__'` is raised when you try to use an object as a descriptor but it doesn't implement the descriptor protocol. The descriptor protocol requires `__get__` (and optionally `__set__` and `__delete__`) to be defined. This error often occurs when trying to use a non-descriptor object in a class attribute position where a descriptor is expected.

## Common Causes

```python
# Cause 1: Using a plain function as a descriptor without __get__
class NotADescriptor:
    def __call__(self, obj):
        return "value"

class MyClass:
    attr = NotADescriptor()

obj = MyClass()
obj.attr  # Works as __call__, but not as a descriptor

# Cause 2: Confusing classmethod/staticmethod with plain methods
class MyClass:
    @classmethod
    def my_classmethod(cls):
        return cls

# Wrong — trying to access __get__ on a bound method
method = MyClass.my_classmethod
# This works, but trying to use it as a descriptor fails

# Cause 3: Property without proper getter
class BadProperty:
    pass

class MyClass:
    prop = BadProperty()  # Not a descriptor

obj = MyClass()
obj.prop  # AttributeError: 'BadProperty' object has no attribute '__get__'

# Cause 4: Non-data descriptor used where data descriptor needed
class NonDataDescriptor:
    def __get__(self, obj, objtype=None):
        return "value"

class MyClass:
    attr = NonDataDescriptor()

obj = MyClass()
obj.attr = 10  # Overwrites descriptor — instance __dict__ takes precedence
print(obj.attr)  # 10 — descriptor is shadowed

# Cause 5: Missing __set__ on a data descriptor
class IncompleteDescriptor:
    def __get__(self, obj, objtype=None):
        return "value"
    # No __set__ defined

class MyClass:
    attr = IncompleteDescriptor()

obj = MyClass()
obj.attr = 10  # This overwrites the descriptor in __dict__
```

## How to Fix

### Fix 1: Implement __get__ correctly

```python
# Wrong — no __get__ method
class MyDescriptor:
    pass

class MyClass:
    attr = MyDescriptor()

# Correct — implement __get__
class MyDescriptor:
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self  # Accessing from class, return descriptor itself
        return "value"

class MyClass:
    attr = MyDescriptor()

obj = MyClass()
print(obj.attr)     # value
print(MyClass.attr) # <__main__.MyDescriptor object at 0x...>
```

### Fix 2: Use property for simple data descriptors

```python
# Wrong — manual descriptor
class TemperatureDescriptor:
    def __get__(self, obj, objtype=None):
        return obj._temp if obj else None

# Correct — use property
class Temperature:
    def __init__(self):
        self._temp = 0

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._temp = value

t = Temperature()
t.temp = 25
print(t.temp)  # 25
```

### Fix 3: Implement both __get__ and __set__ for data descriptors

```python
class ValidatedField:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an int")
        obj.__dict__[self.name] = value

class MyClass:
    age = ValidatedField()

obj = MyClass()
obj.age = 30    # Works
print(obj.age)  # 30
```

### Fix 4: Use __set_name__ for automatic naming

```python
class ValidatedField:
    def __set_name__(self, owner, name):
        self.storage_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.storage_name, None)

    def __set__(self, obj, value):
        setattr(obj, self.storage_name, value)

class User:
    name = ValidatedField()
    age = ValidatedField()

user = User()
user.name = "Alice"
user.age = 30
print(user.name)  # Alice
```

## Examples

```python
# Real-world: Custom property with caching
class CachedProperty:
    def __init__(self, func):
        self.func = func
        self.attrname = None

    def __set_name__(self, owner, name):
        self.attrname = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = self.func(obj)
        obj.__dict__[self.attrname] = value
        return value

class DataProcessor:
    def __init__(self, data):
        self.data = data

    @CachedProperty
    def processed(self):
        print("Processing...")
        return [x * 2 for x in self.data]

processor = DataProcessor([1, 2, 3])
print(processor.processed)  # Processing... [2, 4, 6]
print(processor.processed)  # [2, 4, 6] — cached, no "Processing..."

# Real-world: Type-validated descriptor
class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} must be {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )
        obj.__dict__[self.name] = value

class Product:
    name = Typed(str)
    price = Typed(float)

product = Product()
product.name = "Widget"
product.price = 9.99
print(product.name, product.price)  # Widget 9.99
```

## Related Errors

- [Descriptor issues](descriptor) — general descriptor protocol errors.
- [AttributeError](../attributeerror) — object has no attribute.
- [Property attribute](property-attribute) — property-related errors.
