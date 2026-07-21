---
title: "[Solution] Deprecated Function Migration: abc.abstractproperty to abc.abstractmethod"
description: "Migrate from deprecated abc.abstractproperty to abc.abstractmethod with @property decorator."
deprecated_function: "abc.abstractproperty"
replacement_function: "@abc.abstractmethod + @property"
languages: ["python"]
deprecated_since: "Python 3.3"
---

# [Solution] Deprecated Function Migration: abc.abstractproperty to abc.abstractmethod

The `abc.abstractproperty` has been deprecated in favor of `@abc.abstractmethod + @property`.

## Migration Guide

abc.abstractproperty was deprecated in Python 3.3. Use @abc.abstractmethod combined with @property.

## Before (Deprecated)

```python
from abc import ABC, abstractproperty

class Animal(ABC):
    @abstractproperty
    def sound(self):
        pass
```

## After (Modern)

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def sound(self):
        pass
```

## Key Differences

- Replace @abstractproperty with @property + @abstractmethod
- @property must be the outer decorator
- abstractproperty is deprecated but still functional
