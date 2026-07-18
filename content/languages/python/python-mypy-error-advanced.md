---
title: "Solved Python mypy Advanced Error — How to Fix"
date: 2026-03-20T10:20:00+00:00
description: "Learn how to resolve advanced Python mypy type checking errors including generics, protocols, and complex type issues."
categories: ["python"]
keywords: ["python mypy", "mypy error", "mypy strict", "type checking", "mypy generics"]
error-types: ["runtime-error"]
severities: ["error"]
languages: ["python"]
weight: 5
comments: true
---

## Why It Happens

Advanced mypy errors arise from complex type patterns including generics, protocols, overloaded functions, and type variable constraints. These errors indicate type system misuse or overly complex type annotations.

Common causes include:
- Incorrect use of TypeVar bounds or constraints
- Protocol classes not properly structurally typed
- Missing overloads for functions with multiple signatures
- Recursive type definitions causing infinite loops
- Incompatible type variable variance

## Common Error Messages

```python
from typing import TypeVar, Generic

T = TypeVar('T', int, str)

class Container(Generic[T]):
    value: T

def process(x: Container[int]) -> None:
    reveal_type(x.value)

# mypy: error: "Container[int]" has no attribute "value" (maybe "Container" is not generic?)
```

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None: ...

def render(shape: Drawable) -> None:
    shape.draw()

# mypy: error: Argument 1 has incompatible type "Circle"; expected "Drawable"
```

## How to Fix It

### 1. Use Proper Generic Type Patterns

Define generic types with correct variance and bounds.

```python
from typing import TypeVar, Generic, Protocol, runtime_checkable
from typing import TypeAlias

# Simple generic
T = TypeVar('T')
U = TypeVar('U')

class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
    
    def map(self, func: 'Callable[[T], U]') -> 'Box[U]':
        return Box(func(self.value))

# Bounded TypeVar
from typing import Sequence

def first(seq: Sequence[T]) -> T:
    return seq[0]

# TypeVar with constraints
Numeric = TypeVar('Numeric', int, float, complex)

def add(a: Numeric, b: Numeric) -> Numeric:
    return a + b

# Generic with default
from typing import Generic, TypeVar

T = TypeVar('T')
DefaultT = TypeVar('DefaultT', default=int)

class Registry(Generic[T, DefaultT]):
    def __init__(self, default: DefaultT) -> None:
        self.default = default
```

### 2. Define Structural Types with Protocols

Use protocols for duck typing.

```python
from typing import Protocol, runtime_checkable
from typing import Optional, List

@runtime_checkable
class SupportsLessThan(Protocol):
    def __lt__(self, other: 'SupportsLessThan') -> bool: ...

@runtime_checkable
class Comparable(Protocol):
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: 'Comparable') -> bool: ...

def find_min(items: list[SupportsLessThan]) -> SupportsLessThan:
    return min(items)

class Money:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency
    
    def __lt__(self, other: 'Money') -> bool:
        assert self.currency == other.currency
        return self.amount < other.amount
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

def sort_money(prices: List[Money]) -> List[Money]:
    return sorted(prices)

# Protocol with method overloads
from typing import overload

class Parser(Protocol):
    @overload
    def parse(self, data: str) -> str: ...
    @overload
    def parse(self, data: bytes) -> bytes: ...
    def parse(self, data: str | bytes) -> str | bytes: ...
```

### 3. Handle Complex Type Operations

Use advanced type features correctly.

```python
from typing import (
    TypeVar, Generic, TypeAlias, Union,
    Callable, Protocol, overload, Literal
)
from typing import get_type_hints

# Recursive types
JSON: TypeAlias = Union[str, int, float, bool, None, list['JSON'], dict[str, 'JSON']]

def process_json(data: JSON) -> str:
    if isinstance(data, dict):
        return str({k: process_json(v) for k, v in data.items()})
    elif isinstance(data, list):
        return str([process_json(item) for item in data])
    return str(data)

# Type guards
from typing import TypeGuard

def is_string_list(val: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in val)

def process(data: list[object]) -> None:
    if is_string_list(data):
        # mypy now knows data is list[str]
        print(" ".join(data))

# ParamSpec for decorator typing
from typing import ParamSpec, TypeVar

P = ParamSpec('P')
R = TypeVar('R')

def log_calls(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a: int, b: int) -> int:
    return a + b

# Type alias with TypeVar
from typing import Callable, Awaitable

Handler = Callable[..., Awaitable[None]]
Middleware = Callable[[Handler], Handler]
```

## Common Scenarios

### Scenario 1: API Client Typing

Properly type an HTTP client with generics:

```python
from typing import TypeVar, Generic, Type, Optional
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class Response(Generic[T]):
    data: T
    status_code: int
    headers: dict[str, str]

class APIClient(Generic[T]):
    def __init__(self, base_url: str, model: Type[T]) -> None:
        self.base_url = base_url
        self.model = model
    
    def get(self, path: str) -> Response[T]:
        # Implementation
        raise NotImplementedError
    
    def post(self, path: str, data: dict) -> Response[T]:
        raise NotImplementedError

# Usage with specific model
@dataclass
class User:
    id: int
    name: str
    email: str

client = APIClient("https://api.example.com", User)
response: Response[User] = client.get("/users/1")
reveal_type(response.data.name)  # str
```

### Scenario 2: Plugin System with Type Safety

```python
from typing import Protocol, runtime_checkable, Type, Dict, Any

@runtime_checkable
class Plugin(Protocol):
    name: str
    
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]: ...

class PluginRegistry:
    _plugins: Dict[str, Plugin] = {}
    
    def register(self, plugin: Plugin) -> None:
        self._plugins[plugin.name] = plugin
    
    def get(self, name: str) -> Optional[Plugin]:
        return self._plugins.get(name)
    
    def execute_all(self, context: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        results = {}
        for name, plugin in self._plugins.items():
            results[name] = plugin.execute(context)
        return results

class LoggingPlugin:
    name = "logging"
    
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        print(f"Context: {context}")
        return {"logged": True}

registry = PluginRegistry()
registry.register(LoggingPlugin())  # Type-safe
```

## Prevent It

- Use `mypy --strict` incrementally to catch type issues early
- Use `reveal_type()` during development to verify inferred types
- Prefer `Protocol` over `ABC` for structural subtyping
- Use `TypeAlias` for complex repeated type patterns
- Run `mypy --show-error-codes` for clearer error messages