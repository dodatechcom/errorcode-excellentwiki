---
title: "[Solution] Python Typing Error — Type Hints and Generic Type Issues"
description: "Fix Python typing errors by handling Generic, TypeVar, Protocol, runtime type checking, and get_type_hints failures. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 213
---

# Python Typing Error — Type Hints and Generic Type Issues

Typing errors occur when type hints are incorrectly defined, when generic types are misused, when runtime type checking fails, or when `get_type_hints()` can't resolve forward references. The typing module provides a way to add static type hints to Python code.

## Common Causes

```python
# TypeVar without constraints
from typing import TypeVar

T = TypeVar("T")  # Unconstrained TypeVar — can be anything

def first(lst: T) -> T:  # Type error: T is not a sequence type
    return lst[0]  # Runtime error if T isn't subscriptable
```

```python
# get_type_hints fails with forward references
from typing import get_type_hints

class Node:
    def __init__(self, value: "Node"):  # Forward reference
        self.value = value

# get_type_hints(Node) may fail if Node isn't defined in the right scope
```

```python
# Generic class with wrong type parameters
from typing import Generic, TypeVar

T = TypeVar("T")
class Container(Generic[T]):
    def __init__(self, item: T):
        self.item = item

# Wrong: using a type that doesn't match the TypeVar
c: Container[int] = Container("hello")  # Type checker warns, but no runtime error
```

```python
# Protocol definition errors
from typing import Protocol, runtime_checkable

class Drawable(Protocol):
    def draw(self) -> None: ...

class NotDrawable:
    pass

obj = NotDrawable()
isinstance(obj, Drawable)  # TypeError: Protocols can only be used with @runtime_checkable
```

```python
# get_type_hints with missing annotations
from typing import get_type_hints

def unannotated(x, y):
    return x + y

get_type_hints(unannotated)  # Returns empty dict — no hints to check
```

## How to Fix

### Fix 1: Define TypeVar with proper bounds

```python
from typing import TypeVar, List

# Unconstrained — any type
T = TypeVar("T")

# Bounded — must be a subclass of the bound
from typing import Sequence
S = TypeVar("S", bound=Sequence)

# Constrained — must be one of the specified types
IntOrStr = TypeVar("IntOrStr", int, str)

def first(lst: S) -> S:
    """Return the first element of a sequence."""
    return lst[0]

def double(x: IntOrStr) -> IntOrStr:
    """Double an int or repeat a string."""
    if isinstance(x, int):
        return x * 2
    return x * 2

print(first([1, 2, 3]))      # 1
print(first("hello"))         # 'h'
print(double(5))              # 10
print(double("ab"))           # 'abab'
```

### Fix 2: Use Generic classes properly

```python
from typing import TypeVar, Generic, List

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()
    
    def is_empty(self) -> bool:
        return len(self._items) == 0

# Usage with type hints
stack: Stack[int] = Stack()
stack.push(1)
stack.push(2)
value: int = stack.pop()

print(value)  # 2
```

### Fix 3: Use Protocol for structural subtyping

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str:
        return "Drawing circle"

class Square:
    def draw(self) -> str:
        return "Drawing square"

def render(shape: Drawable) -> str:
    return shape.draw()

# Works with any class that has a draw() method
circle = Circle()
square = Square()

print(render(circle))  # Drawing circle
print(render(square))  # Drawing square

# Runtime check with @runtime_checkable
print(isinstance(circle, Drawable))  # True
print(isinstance("not a shape", Drawable))  # False
```

### Fix 4: Handle get_type_hints with fallback

```python
from typing import get_type_hints, Dict, Any

def safe_get_type_hints(obj, globalns=None, localns=None) -> Dict[str, Any]:
    """Safely get type hints with fallback."""
    try:
        return get_type_hints(obj, globalns, localns)
    except (NameError, TypeError) as e:
        print(f"Warning: Could not resolve type hints: {e}")
        return {}

class MyClass:
    def method(self, x: int, y: str = "hello") -> bool:
        return True

hints = safe_get_type_hints(MyClass.method)
print(hints)  # {'x': <class 'int'>, 'y': <class 'str'>, 'return': <class 'bool'>}
```

### Fix 5: Use TypedDict for dictionary type hints

```python
from typing import TypedDict, List

class UserDict(TypedDict):
    name: str
    age: int
    email: str

class ConfigDict(TypedDict, total=False):
    host: str
    port: int
    debug: bool

def process_user(user: UserDict) -> str:
    return f"{user['name']} ({user['age']})"

# Usage
user: UserDict = {"name": "Alice", "age": 30, "email": "alice@example.com"}
print(process_user(user))  # Alice (30)

# Config with optional fields
config: ConfigDict = {"host": "localhost"}  # port and debug are optional
print(config)
```

## Examples

### Complete type hint example

```python
from typing import (
    TypeVar, Generic, List, Optional, Union, 
    Callable, Iterator, Dict, Tuple
)

T = TypeVar("T")
U = TypeVar("U")

class Repository(Generic[T]):
    """Generic repository for CRUD operations."""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def add(self, item: T) -> None:
        self._items.append(item)
    
    def get(self, index: int) -> Optional[T]:
        if 0 <= index < len(self._items):
            return self._items[index]
        return None
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]
    
    def map(self, func: Callable[[T], U]) -> List[U]:
        return [func(item) for item in self._items]
    
    def __iter__(self) -> Iterator[T]:
        return iter(self._items)
    
    def __len__(self) -> int:
        return len(self._items)

# Usage
repo: Repository[int] = Repository()
repo.add(1)
repo.add(2)
repo.add(3)

result: Optional[int] = repo.get(0)
evens: List[int] = repo.filter(lambda x: x % 2 == 0)
doubled: List[int] = repo.map(lambda x: x * 2)

print(result)   # 1
print(evens)    # [2]
print(doubled)  # [2, 4, 6]
```

### Union types and TypeGuard

```python
from typing import Union, TypeGuard

def is_string_list(val: list[Union[str, int]]) -> TypeGuard[list[str]]:
    """Check if all elements are strings."""
    return all(isinstance(x, str) for x in val)

def process(data: list[Union[str, int]]) -> str:
    if is_string_list(data):
        # Type checker knows data is list[str] here
        return " ".join(data)
    else:
        return str(data)

print(process(["hello", "world"]))  # hello world
print(process([1, 2, 3]))          # [1, 2, 3]
```

## Related Errors

- [TypeError](/languages/python/typeerror/) — incorrect type hint syntax
- [NameError](/languages/python/nameerror/) — unresolvable forward references
- [AttributeError](/languages/python/attributeerror/) — accessing non-existent type attributes
