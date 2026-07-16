---
title: "[Solution] Python NotImplementedError — Abstract Method Not Implemented Fix"
description: "Fix Python NotImplementedError when calling unimplemented methods. Implement in subclasses or use abc.ABC for abstract methods properly."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["notimplementederror", "abstract", "inheritance", "subclass"]
weight: 65
---

# NotImplementedError — Abstract Method Not Implemented Fix

A `NotImplementedError` is raised when a method or function has not been implemented yet. It signals that a subclass must override the method, or that the code is incomplete.

## Description

`NotImplementedError` inherits from `RuntimeError` and is used as a marker for abstract or placeholder methods. Python doesn't enforce abstract methods at runtime unless you use `abc.ABC` and `abc.abstractmethod`. Without `abc`, calling an unimplemented method raises the error at call time.

Common scenarios:

- **Base class defines stub method** — subclass forgets to override.
- **Incomplete implementation** — developer left a `raise NotImplementedError`.
- **Using abc.ABC incorrectly** — forgetting to decorate methods.
- **Calling parent method directly** — calling `super().method()` on a stub.
- **Third-party library** — abstract interface not implemented by user code.

## Common Causes

```python
# Cause 1: Base class stub method
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    # Forgot to implement area()

c = Circle(5)
c.area()  # NotImplementedError

# Cause 2: Incomplete interface
class Database:
    def connect(self):
        raise NotImplementedError

    def query(self, sql):
        raise NotImplementedError

db = Database()
db.connect()  # NotImplementedError

# Cause 3: Calling super() on abstract method
class Base:
    def process(self):
        raise NotImplementedError

class Child(Base):
    def process(self):
        return super().process()  # Calls the stub

Child().process()  # NotImplementedError

# Cause 4: Third-party abstract class
from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def execute(self):
        pass

class MyPlugin(Plugin):
    pass  # Didn't implement execute()

MyPlugin()  # TypeError: Can't instantiate abstract class
```

## Solutions

### Fix 1: Implement the method in your subclass

```python
# Wrong — subclass doesn't implement area
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

# Correct
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2
```

### Fix 2: Use abc.ABC to enforce at instantiation

```python
from abc import ABC, abstractmethod

# Wrong — no enforcement, error at call time
class Base:
    def method(self):
        raise NotImplementedError

# Correct — error at instantiation time
class Base(ABC):
    @abstractmethod
    def method(self):
        pass

class Child(Base):
    def method(self):
        return "implemented"

Child()  # Works
# Base()  # TypeError: Can't instantiate abstract class Base
```

### Fix 3: Implement all abstract methods before instantiation

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

# Wrong — only implements one abstract method
class Dog(Animal):
    def speak(self):
        return "Woof"
    # move() not implemented

# Correct — implements both
class Dog(Animal):
    def speak(self):
        return "Woof"

    def move(self):
        return "Run"
```

### Fix 4: Don't call super() on stub methods

```python
class Base:
    def process(self):
        raise NotImplementedError("Override this method")

# Wrong
class Child(Base):
    def process(self):
        return super().process()  # Calls the stub

# Correct — implement fully
class Child(Base):
    def process(self):
        return "Processing done"
```

### Fix 5: Check if method is implemented before calling

```python
# Wrong — assumes method is implemented
def use_plugin(plugin):
    return plugin.execute()

# Correct — check first
def use_plugin(plugin):
    if not hasattr(plugin, 'execute') or callable(getattr(plugin, 'execute', None)):
        # Use a default or raise a clear error
        raise ValueError(f"{plugin} does not implement execute()")
    return plugin.execute()
```

## Related Errors

- [TypeError](../typeerror) — wrong type or missing required methods.
- [AttributeError](../attributeerror) — attribute or method doesn't exist.
- [RuntimeError](../runtimeerror) — generic runtime error.
