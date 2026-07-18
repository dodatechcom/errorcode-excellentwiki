---
title: "[Solution] Python Mypy Type Checking Error — How to Fix"
description: "Fix Python Mypy type errors. Resolve type inference, protocol, and plugin issues with Mypy."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Mypy Type Checking Error

A Mypy error occurs when static type checking finds type inconsistencies. Mypy enforces type annotations and detects potential runtime type errors before code execution.

## Why It Happens

Mypy performs static analysis of type annotations. Errors occur when function return types don't match annotations, when union types are used without narrowing, or when third-party libraries lack type stubs.

## Common Error Messages

- `error: Incompatible return value type`
- `error: Item 'None' of 'Optional[str]' has no attribute 'upper'`
- `error: Argument has incompatible type 'int'; expected 'str'`
- `error: Name 'undefined' is not defined`

## How to Fix It

### Fix 1: Narrow union types with isinstance

```python
def greet(name: str | None) -> str:
    if name is None:
        return 'Hello, World!'
    return f'Hello, {name.upper()}'
```

### Fix 2: Use TypeVar for generic functions

```python
from typing import TypeVar, List

T = TypeVar('T')

def first(items: List[T]) -> T:
    return items[0]
```

### Fix 3: Use Protocol for structural typing

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

def render(obj: Drawable) -> None:
    obj.draw()
```

### Fix 4: Add type ignore for known issues

```python
# For third-party libraries without stubs
import untyped_lib  # type: ignore

# Or inline
value = untyped_lib.get()  # type: ignore[no-untyped-call]
```

## Common Scenarios

- **Optional values** — Accessing attributes on Optional types without None checks.
- **Third-party stubs** — Missing type stubs for packages cause import errors.
- **Complex generics** — TypeVar bounds and constraints produce confusing errors.

## Prevent It

- Run mypy with --strict during CI/CD to catch issues early
- Use typing_extensions for features not yet in standard typing
- Add py.typed markers to your own packages

## Related Errors

- - [TypeError](/languages/python/typeerror/) — unsupported operand type
- - [pylint Error](/languages/python/pylint-error/) — linter configuration issues
