---
title: "[Solution] Python Functools Error — Higher-Order Function and Decorator Issues"
description: "Fix Python functools errors by handling lru_cache, partial, reduce, wraps, total_ordering, and cached_property. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 214
---

# Python Functools Error — Higher-Order Function and Decorator Issues

Functools errors occur when caching decorators are used on unhashable arguments, when `partial` functions have incorrect signatures, when `reduce` lacks an initializer with empty sequences, or when `wraps` doesn't properly preserve function metadata.

## Common Causes

```python
# lru_cache with unhashable arguments
from functools import lru_cache

@lru_cache(maxsize=128)
def process(data: dict) -> int:
    return sum(data.values())

process({"a": 1, "b": 2})  # TypeError: unhashable type: 'dict'
```

```python
# reduce on empty sequence without initializer
from functools import reduce

reduce(lambda x, y: x + y, [])  # TypeError: reduce() of empty sequence with no initial value
```

```python
# partial with wrong argument order
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
square(5)  # Works
square = partial(power, 2)  # base=2
# square() missing 1 required positional argument: 'exponent'
```

```python
# wraps not preserving __wrapped__ attribute correctly
from functools import wraps

def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    # Missing: @wraps(func)
    return wrapper

@bad_decorator
def my_function():
    """My docstring."""
    pass

my_function.__name__  # 'wrapper' instead of 'my_function'
my_function.__doc__   # None instead of 'My docstring.'
```

```python
# cached_property on unhashable objects
from functools import cached_property

class BadCache:
    def __init__(self):
        self._data = None
    
    @cached_property
    def data(self):
        # cached_property uses __dict__ which may conflict with descriptors
        return expensive_computation()
```

## How to Fix

### Fix 1: Make arguments hashable for lru_cache

```python
from functools import lru_cache

# Option 1: Use frozenset or tuple instead of dict
@lru_cache(maxsize=128)
def process(data: tuple) -> int:
    return sum(data)

process((1, 2, 3))  # Works — tuple is hashable

# Option 2: Convert unhashable to hashable
@lru_cache(maxsize=128)
def process_dict(frozen_data: frozenset) -> int:
    return sum(v for _, v in frozen_data)

process_dict(frozenset({"a": 1, "b": 2}.items()))  # Works

# Option 3: Use a wrapper with manual caching
def process_with_cache(data: dict) -> int:
    cache_key = tuple(sorted(data.items()))
    if not hasattr(process_with_cache, "_cache"):
        process_with_cache._cache = {}
    
    if cache_key in process_with_cache._cache:
        return process_with_cache._cache[cache_key]
    
    result = sum(data.values())
    process_with_cache._cache[cache_key] = result
    return result
```

### Fix 2: Use reduce with proper initializer

```python
from functools import reduce

# Always provide initializer for potentially empty sequences
result = reduce(lambda x, y: x + y, [], 0)  # Returns 0 for empty list
print(result)  # 0

result = reduce(lambda x, y: x + y, [1, 2, 3], 0)  # Returns 6
print(result)  # 6

# For string concatenation
result = reduce(lambda x, y: x + " " + y, [], "")  # Returns ""
result = reduce(lambda x, y: x + " " + y, ["hello", "world"])  # "hello world"
```

### Fix 3: Use partial correctly with positional and keyword arguments

```python
from functools import partial

def connect(host, port, timeout=30, ssl=False):
    return f"Connecting to {host}:{port} (timeout={timeout}, ssl={ssl})"

# Fix keyword arguments with partial
connect_local = partial(connect, "localhost", 8080)
print(connect_local())  # Connecting to localhost:8080 (timeout=30, ssl=False)

# Override defaults
connect_secure = partial(connect, "localhost", 443, ssl=True)
print(connect_secure(timeout=60))  # Connecting to localhost:443 (timeout=60, ssl=True)

# Use partial for callback functions
def callback(prefix, message):
    print(f"{prefix}: {message}")

error_callback = partial(callback, "ERROR")
error_callback("Something went wrong")  # ERROR: Something went wrong
```

### Fix 4: Use wraps to preserve function metadata

```python
from functools import wraps
import time

def timer(func):
    """Decorator that times function execution."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

def log_calls(func):
    """Decorator that logs function calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@timer
@log_calls
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)  # 'add' — preserved by @wraps
print(add.__doc__)   # 'Add two numbers.' — preserved
add(1, 2)  # Shows both logging and timing
```

### Fix 5: Use cached_property correctly

```python
from functools import cached_property
import time

class DataProcessor:
    def __init__(self, data):
        self._data = data
    
    @cached_property
    def processed_data(self):
        """Expensive computation — result is cached."""
        print("Processing data...")
        time.sleep(1)  # Simulate expensive work
        return [x * 2 for x in self._data]
    
    @cached_property
    def summary(self):
        """Compute summary from processed data."""
        data = self.processed_data  # Uses cached value
        return {
            "count": len(data),
            "sum": sum(data),
            "avg": sum(data) / len(data) if data else 0,
        }

# Usage
processor = DataProcessor([1, 2, 3])
print(processor.processed_data)  # Processes and caches
print(processor.processed_data)  # Returns cached value instantly
print(processor.summary)          # Uses cached processed_data
```

### Fix 6: Use total_ordering for rich comparison

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __eq__(self, other):
        return self.grade == other.grade
    
    def __lt__(self, other):
        return self.grade < other.grade

alice = Student("Alice", 90)
bob = Student("Bob", 85)

print(alice > bob)    # True — auto-generated from __lt__
print(alice >= bob)   # True — auto-generated
print(alice <= bob)   # False — auto-generated
print(alice != bob)   # True — auto-generated from __eq__
```

## Examples

### Combining functools tools

```python
from functools import lru_cache, reduce, partial
from typing import List

# lru_cache with type conversion
@lru_cache(maxsize=256)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Partial for specialized operations
def fold operation(func, initial, iterable):
    return reduce(func, iterable, initial)

sum_all = partial(fold, lambda x, y: x + y, 0)
product_all = partial(fold, lambda x, y: x * y, 1)

print(fibonacci(30))         # 832040
print(sum_all([1, 2, 3, 4]))  # 10
print(product_all([1, 2, 3, 4]))  # 24
```

### Custom caching decorator

```python
from functools import wraps
import time

def memoize_with_ttl(ttl_seconds):
    """Cache function results with time-to-live."""
    def decorator(func):
        cache = {}
        
        @wraps(func)
        def wrapper(*args):
            current_time = time.time()
            
            if args in cache:
                result, timestamp = cache[args]
                if current_time - timestamp < ttl_seconds:
                    return result
            
            result = func(*args)
            cache[args] = (result, current_time)
            return result
        
        wrapper.cache_clear = lambda: cache.clear()
        wrapper.cache_info = lambda: {"size": len(cache), "ttl": ttl_seconds}
        return wrapper
    return decorator

@memoize_with_ttl(ttl_seconds=60)
def expensive_computation(n):
    print(f"Computing {n}...")
    return n ** 2

print(expensive_computation(5))  # Computes
print(expensive_computation(5))  # Returns cached
print(expensive_computation.cache_info())  # {'size': 1, 'ttl': 60}
```

## Related Errors

- [TypeError](/languages/python/typeerror/) — unhashable arguments in lru_cache
- [ValueError](/languages/python/valueerror/) — invalid reduce on empty sequences
- [AttributeError](/languages/python/attributeerror/) — missing function metadata without wraps
