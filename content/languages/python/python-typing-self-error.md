---
title: "[Solution] Python 3.11+ typing.Self Error — Self Type, Classmethod Returns, Fluent Interfaces"
description: "Fix Python 3.11+ typing.Self errors including Self type usage, classmethod return types, fluent interface patterns, and forward reference issues."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 511
---

# Python 3.11+ typing.Self Error — Self Type, Classmethod Returns, Fluent Interfaces

Python 3.11 added `typing.Self` for type annotations that refer to the enclosing class. Common errors include using `Self` outside a class, incorrect `@classmethod` return types, and confusion with older `TypeVar` patterns.

## Common Causes

```python
# Cause 1: Using Self outside a class
from typing import Self

def get_self() -> Self:  # NameError - Self not defined outside class
    pass

# Cause 2: Wrong Self import for older Python
from typing import Self  # Python 3.11+ only

# Cause 3: Forgetting Self in classmethod return type
class Builder:
    @classmethod
    def create(cls) -> Builder:  # Works but not ideal for subclasses
        return cls()

# Cause 4: Using Self with non-class contexts
from typing import Self

def factory() -> Self:  # Self only valid in class methods/attributes
    pass

# Cause 5: Self with generic classes
from typing import Self, Generic, TypeVar

T = TypeVar("T")

class Container(Generic[T]):
    def get(self) -> Self:  # Fine, but may confuse type checkers
        return self
```

## How to Fix

### Fix 1: Import Self correctly

```python
# Wrong - Self not available in older Python
from typing import Self  # Python 3.11+

# Correct - version-conditional import
import sys
if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing import TypeVar
    Self = TypeVar("Self", bound="Self")  # Fallback

# Or use typing_extensions for compatibility
# pip install typing-extensions
from typing_extensions import Self
```

### Fix 2: Use Self in classmethod return types

```python
# Wrong - using class name directly
class Builder:
    def __init__(self, value=0):
        self.value = value

    @classmethod
    def create(cls) -> Builder:  # Not ideal for subclasses
        return cls()

    def with_value(self, v) -> Builder:  # Won't work with subclasses
        self.value = v
        return self

# Correct - use Self for return types
from typing import Self

class Builder:
    def __init__(self, value=0):
        self.value = value

    @classmethod
    def create(cls) -> Self:
        return cls()

    def with_value(self, v: int) -> Self:
        self.value = v
        return self

# Subclass works correctly
class TypedBuilder(Builder):
    def with_extra(self) -> Self:
        return self
```

### Fix 3: Use Self for fluent interfaces

```python
from typing import Self

class Query:
    def __init__(self):
        self._table = ""
        self._conditions = []
        self._limit = None

    def table(self, name: str) -> Self:
        self._table = name
        return self

    def where(self, condition: str) -> Self:
        self._conditions.append(condition)
        return self

    def limit(self, n: int) -> Self:
        self._limit = n
        return self

    def build(self) -> str:
        query = f"SELECT * FROM {self._table}"
        if self._conditions:
            query += " WHERE " + " AND ".join(self._conditions)
        if self._limit:
            query += f" LIMIT {self._limit}"
        return query

# Usage
q = Query().table("users").where("age > 18").limit(10).build()
```

### Fix 4: Use Self with __init_subclass__ patterns

```python
from typing import Self

class Base:
    def clone(self) -> Self:
        import copy
        return copy.copy(self)

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        instance = cls()
        instance.__dict__.update(data)
        return instance

class Child(Base):
    def __init__(self):
        self.name = ""

# Child.from_dict returns Child, not Base
child = Child.from_dict({"name": "test"})
```

## Examples

```python
# Fluent API pattern
from typing import Self

class HTMLBuilder:
    def __init__(self):
        self._elements = []

    def add_heading(self, text: str, level: int = 1) -> Self:
        self._elements.append(f"<h{level}>{text}</h{level}>")
        return self

    def add_paragraph(self, text: str) -> Self:
        self._elements.append(f"<p>{text}</p>")
        return self

    def add_list(self, items: list[str]) -> Self:
        li = "".join(f"<li>{item}</li>" for item in items)
        self._elements.append(f"<ul>{li}</ul>")
        return self

    def build(self) -> str:
        return "\n".join(self._elements)

# Chain calls fluently
html = (
    HTMLBuilder()
    .add_heading("Title")
    .add_paragraph("Hello world")
    .add_list(["Item 1", "Item 2"])
    .build()
)

# Builder pattern with inheritance
from typing import Self

class ResponseBuilder:
    def __init__(self):
        self._status = 200
        self._headers = {}
        self._body = ""

    def status(self, code: int) -> Self:
        self._status = code
        return self

    def header(self, key: str, value: str) -> Self:
        self._headers[key] = value
        return self

class JSONResponseBuilder(ResponseBuilder):
    def __init__(self):
        super().__init__()
        self._data = None

    def data(self, obj) -> Self:
        self._data = obj
        return self

    def build(self) -> str:
        import json
        self._headers["Content-Type"] = "application/json"
        self._body = json.dumps(self._data)
        return f"HTTP/1.1 {self._status}\n{self._headers}\n{self._body}"
```

## Related Errors

- [python-typing-error](../python-typing-error) — General typing errors
- [python-union-type-syntax](../python-union-type-syntax) — Type union syntax
- [python311-deprecation](../python311-deprecation) — Python 3.11 changes
- [mypy-error](../mypy-error) — Mypy type checking errors
