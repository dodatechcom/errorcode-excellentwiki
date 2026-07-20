---
title: "[Solution] Python 3.12 @override Decorator — typing.override, Method Signatures"
description: "Fix Python 3.12 @override decorator errors including typing.override usage, method signature mismatches, inheritance detection, and typing_extensions fallback."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 512
---

# Python 3.12 @override Decorator — typing.override, Method Signatures

Python 3.12 added `@override` from `typing` to indicate methods that override a parent class method. Errors occur when the method doesn't actually override anything, signature mismatches, or using the wrong import path.

## Common Causes

```python
# Cause 1: Wrong import path
from typing import override  # Python 3.12+ only

# Cause 2: Method doesn't actually override parent
from typing import override

class Parent:
    def do_something(self):
        pass

class Child(Parent):
    @override
    def do_something_else(self):  # Error - doesn't override anything
        pass

# Cause 3: Signature mismatch with parent
class Parent:
    def process(self, x: int) -> str:
        return str(x)

class Child(Parent):
    @override
    def process(self, x: str) -> int:  # Different signature
        return len(x)

# Cause 4: Using @override on non-method
from typing import override

@override
def standalone_function():  # Error - not a method
    pass

# Cause 5: Missing @override when overriding (not an error, but bad practice)
class Parent:
    def method(self):
        pass

class Child(Parent):
    def method(self):  # No error, but should use @override
        pass
```

## How to Fix

### Fix 1: Import override correctly

```python
# Wrong - using wrong import for older Python
from typing import override  # Python 3.12+ only

# Correct - use typing_extensions for compatibility
# pip install typing-extensions
from typing_extensions import override

# Or version-conditional
import sys
if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override
```

### Fix 2: Ensure method actually overrides parent

```python
from typing import override

class Parent:
    def do_something(self):
        pass

    def process(self, x: int) -> str:
        return str(x)

class Child(Parent):
    @override
    def do_something(self):  # Correct - overrides Parent.do_something
        pass

    @override
    def process(self, x: int) -> str:  # Correct - same signature
        return f"processed: {x}"
```

### Fix 3: Fix signature mismatches

```python
from typing import override

class Parent:
    def process(self, x: int, verbose: bool = False) -> str:
        return str(x)

class Child(Parent):
    @override
    def process(self, x: int, verbose: bool = False) -> str:  # Correct - matches parent
        if verbose:
            return f"processing {x}"
        return str(x)

# If you need different behavior, don't use @override
class SpecialChild(Parent):
    def process_special(self, x: str) -> int:  # New method, no @override
        return len(x)
```

### Fix 4: Use @override with inheritance chains

```python
from typing import override

class Base:
    def method(self) -> str:
        return "base"

class Middle(Base):
    @override
    def method(self) -> str:
        return "middle"

class Top(Middle):
    @override
    def method(self) -> str:  # Overrides Middle.method
        return "top"
```

## Examples

```python
# Practical: API client with method overrides
from typing import override

class BaseClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def request(self, method: str, path: str) -> dict:
        return {"method": method, "path": path}

    def get(self, path: str) -> dict:
        return self.request("GET", path)

class CachedClient(BaseClient):
    def __init__(self, base_url: str):
        super().__init__(base_url)
        self._cache = {}

    @override
    def get(self, path: str) -> dict:
        if path not in self._cache:
            self._cache[path] = super().get(path)
        return self._cache[path]

# Type checker will verify override correctness
# mypy will flag methods with @override that don't match parent
```

## Related Errors

- [python-typing-error](../python-typing-error) — General typing errors
- [python-typing-self-error](../python-typing-self-error) — Self type usage
- [python312-deprecation](../python312-deprecation) — Python 3.12 changes
- [mypy-error](../mypy-error) — Type checking errors
