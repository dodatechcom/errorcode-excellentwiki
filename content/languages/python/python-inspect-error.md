---
title: "[Solution] Python Inspect Error — Module and Object Inspection Issues"
description: "Fix Python inspect errors by handling getsource failures, signature errors, module inspection, and stack introspection issues. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 209
---

# Python Inspect Error — Module and Object Inspection Issues

Inspect errors occur when trying to retrieve source code for dynamically created objects, when function signatures cannot be determined, or when stack introspection fails. The inspect module provides powerful tools for examining live objects but has limitations with certain object types.

## Common Causes

```python
# getsource() fails on built-in functions
import inspect

inspect.getsource(print)  # TypeError: <built-in function print> is not a module, class, method, function, traceback, frame, or code object

inspect.getsource(len)  # TypeError: <built-in function len> is a built-in
```

```python
# getsource() fails on lambda or exec-created functions
import inspect

func = eval("lambda x: x + 1")
inspect.getsource(func)  # OSError: could not get source code

# Dynamically created functions have no source file
code = compile("def dynamic(): pass", "<dynamic>", "exec")
exec(code)
```

```python
# Signature errors with complex decorators
import inspect
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def decorated(x, y=10):
    pass

# May fail if decorator doesn't properly use functools.wraps
sig = inspect.signature(decorated)  # Shows wrapper's signature instead of original
```

```python
# Getting source of classes defined in __main__
import inspect

# In interactive session or script without source file
class DynamicClass:
    pass

inspect.getsource(DynamicClass)  # OSError: could not get source code
```

```python
# Stack introspection in optimized mode
import inspect

# Python with -O flag strips assert statements
frame = inspect.currentframe()
# Some frame attributes may be None in optimized mode
```

## How to Fix

### Fix 1: Handle getsource failures gracefully

```python
import inspect

def safe_getsource(obj):
    """Safely get source code for an object."""
    try:
        return inspect.getsource(obj)
    except (TypeError, OSError) as e:
        return f"Cannot retrieve source: {e}"

# Usage
print(safe_getsource(print))  # Cannot retrieve source: <built-in function print> is a built-in

def my_function():
    """My function."""
    return 42

print(safe_getsource(my_function))  # Shows actual source code
```

### Fix 2: Use signature() with fallback handling

```python
import inspect

def safe_signature(func):
    """Safely get function signature."""
    try:
        sig = inspect.signature(func)
        return sig
    except (ValueError, TypeError) as e:
        return None

def my_func(a, b, c=10):
    pass

sig = safe_signature(my_func)
if sig:
    print(f"Parameters: {list(sig.parameters.keys())}")  # ['a', 'b', 'c']
    for name, param in sig.parameters.items():
        print(f"  {name}: default={param.default}")
```

### Fix 3: Use inspect module for runtime inspection

```python
import inspect

class Calculator:
    """A simple calculator class."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b

# Get all methods
methods = inspect.getmembers(Calculator, predicate=inspect.isfunction)
print("Methods:", [name for name, _ in methods])  # ['add', 'subtract']

# Get method signature
sig = inspect.signature(Calculator.add)
print("Add signature:", sig)  # (self, a, b)

# Get docstrings
for name, method in methods:
    doc = inspect.getdoc(method)
    print(f"{name}: {doc}")
```

### Fix 4: Use stack() for call stack introspection

```python
import inspect

def log_call_stack():
    """Log the current call stack."""
    frame = inspect.currentframe()
    try:
        stack = inspect.getouterframes(frame)
        for i, frame_info in enumerate(stack):
            print(f"Frame {i}: {frame_info.filename}:{frame_info.lineno} in {frame_info.function}")
    finally:
        del frame  # Avoid reference cycles

def a():
    b()

def b():
    c()

def c():
    log_call_stack()

a()
```

### Fix 5: Inspect module attributes safely

```python
import inspect

def inspect_object(obj):
    """Comprehensive object inspection."""
    result = {
        "type": type(obj).__name__,
        "doc": inspect.getdoc(obj),
        "module": getattr(obj, "__module__", None),
        "name": getattr(obj, "__name__", None),
    }
    
    # Check if it's callable
    if callable(obj):
        result["callable"] = True
        try:
            result["signature"] = str(inspect.signature(obj))
        except (ValueError, TypeError):
            result["signature"] = "N/A"
    
    # Check for source code
    try:
        result["source"] = inspect.getsource(obj)
    except (TypeError, OSError):
        result["source"] = "N/A"
    
    return result

def example_function(x, y=10):
    """Example function for inspection."""
    return x + y

info = inspect_object(example_function)
for key, value in info.items():
    print(f"{key}: {value}")
```

## Examples

### Module inspection and discovery

```python
import inspect
import json

def inspect_module(module):
    """Inspect all public items in a module."""
    items = []
    for name, obj in inspect.getmembers(module):
        if name.startswith("_"):
            continue
        
        item_info = {
            "name": name,
            "type": type(obj).__name__,
            "doc": inspect.getdoc(obj) or "No documentation",
        }
        
        if callable(obj):
            try:
                item_info["signature"] = str(inspect.signature(obj))
            except (ValueError, TypeError):
                item_info["signature"] = "N/A"
        
        items.append(item_info)
    
    return items

items = inspect_module(json)
for item in items[:5]:  # Show first 5
    print(f"{item['name']} ({item['type']}): {item['doc'][:50]}...")
```

### Custom decorator with signature preservation

```python
import inspect
from functools import wraps

def validated(*validators):
    """Decorator that validates function arguments."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            
            for param_name, validator in validators:
                if param_name in bound.arguments:
                    value = bound.arguments[param_name]
                    if not validator(value):
                        raise ValueError(f"Validation failed for {param_name}: {value}")
            
            return func(*args, **kwargs)
        
        # Preserve original signature
        wrapper.__signature__ = sig
        return wrapper
    return decorator

@validated(("x", lambda x: x > 0), ("y", lambda y: isinstance(y, str)))
def process(x, y):
    return f"{y}: {x}"

print(process(5, "result"))  # result: 5
# process(-1, "result")  # Raises ValueError
```

## Related Errors

- [OSError](/languages/python/oserror/) — getsource() can't find source files
- [TypeError](/languages/python/typeerror/) — inspect functions receive wrong object types
- [AttributeError](/languages/python/attributeerror/) — accessing non-existent object attributes
