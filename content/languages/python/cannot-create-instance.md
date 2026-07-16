---
title: "[Solution] Python TypeError — Cannot Create Instance"
description: "Fix Python TypeError: cannot create instance when trying to instantiate a type that doesn't support it. Learn common causes and solutions."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["typeerror", "instance", "class", "instantiate"]
weight: 5
---

# TypeError — Cannot Create Instance

A `TypeError` with the message "cannot create instance" is raised when you try to instantiate a type that does not allow object creation, such as certain C-level types, abstract base classes, or types with restricted `__new__` methods.

## Description

Some types in Python cannot be instantiated directly. This includes types like `NoneType`, `EllipsisType`, `NotImplementedType`, certain abstract base classes, and types that override `__new__` to prevent instantiation. This error can also occur when you try to call a type that is not actually a class.

Common patterns:

- **Trying to instantiate NoneType** — `NoneType()`.
- **Calling an abstract base class** — creating an instance of `abc.ABC` directly.
- **Calling a non-type** — using parentheses on a variable that is not a class.
- **Restricted `__new__`** — a class that overrides `__new__` to raise an error.

## Common Causes

```python
# Cause 1: Trying to create NoneType
import types
value = types.NoneType()  # TypeError: cannot create 'NoneType' instances

# Cause 2: Calling a non-type object
value = 42
obj = value()  # TypeError: 'int' object is not callable

# Cause 3: Calling an abstract base class
from abc import ABC
obj = ABC()  # TypeError: Can't instantiate abstract class

# Cause 4: Calling a module
import os
obj = os()  # TypeError: 'module' object is not callable
```

## Solutions

### Fix 1: Use the correct type or value

```python
# Wrong
import types
value = types.NoneType()

# Correct
value = None
```

### Fix 2: Instantiate the concrete class, not the abstract one

```python
# Wrong
from abc import ABC
obj = ABC()

# Correct — create a concrete subclass
from abc import ABC, abstractmethod

class MyAbstract(ABC):
    @abstractmethod
    def my_method(self):
        pass

class Concrete(MyAbstract):
    def my_method(self):
        return "hello"

obj = Concrete()
```

### Fix 3: Check if the object is a class before instantiating

```python
# Wrong
obj = 42
instance = obj()

# Correct
if isinstance(obj, type):
    instance = obj()
else:
    print(f"{obj} is not a class")
```

### Fix 4: Use the correct callable

```python
# Wrong — calling a module
import json
data = json()

# Correct — calling a function from the module
import json
data = json.loads('{"key": "value"}')
```

## Related Errors

- [Module not callable](module-not-callable) — calling a module instead of a function.
- [AttributeError](../attributeerror) — object has no attribute.
- [TypeError](../typeerror) — general type mismatch errors.
