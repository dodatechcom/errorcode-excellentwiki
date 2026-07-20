---
title: "[Solution] Python Doctest Error — Example Failures and Output Mismatches"
description: "Fix Python doctest errors by handling example failures, option flags, whitespace normalization, and expected output mismatches. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 205
---

# Python Doctest Error — Example Failures and Output Mismatches

Doctest errors occur when code examples in docstrings produce output that doesn't match the expected results. Common issues include whitespace differences, floating-point precision, exception message formatting, and encoding differences across platforms.

## Common Causes

```python
# Floating-point precision mismatch
def circle_area(radius):
    """Calculate circle area.
    
    >>> circle_area(1)
    3.14
    """
    import math
    return math.pi * radius ** 2

# Doctest fails: Expected: 3.14, Got: 3.141592653589793
```

```python
# Exception message mismatch across Python versions
def divide(a, b):
    """Divide two numbers.
    
    >>> divide(1, 0)
    ZeroDivisionError: division by zero
    """
    return a / b

# Python 3.10+ might show: ZeroDivisionError: division by zero
# Older versions: ZeroDivisionError: integer division or modulo by zero
```

```python
# Whitespace mismatch
def get_dict():
    """Return a dictionary.
    
    >>> get_dict()
    {'a': 1, 'b': 2}
    """
    return {"a": 1, "b": 2}

# Dictionary ordering differs between Python versions and insertion order
# Python 3.7+: {'a': 1, 'b': 2}
# Python 3.6-: {'b': 2, 'a': 1} (hash-based ordering)
```

```python
# Missing doctest directive for ellipsis or whitespace
def get_list():
    """Return a list.
    
    >>> get_list()
    [1, 2, 3, ...]
    """
    return [1, 2, 3, 4, 5]

# Fails: Expected: [1, 2, 3, ...], Got: [1, 2, 3, 4, 5]
```

```python
# Encoding issues in docstrings
def greet(name):
    """Greet someone.
    
    >>> greet("Alice")
    'Hello, Alice!'
    """
    return f"Hello, {name}!"

# Fails if docstring has Unicode characters and file encoding is wrong
```

## How to Fix

### Fix 1: Use doctest directives for floating-point and ellipsis

```python
def circle_area(radius):
    """Calculate circle area.
    
    >>> circle_area(1)  # doctest: +ELLIPSIS
    3.14159...
    
    >>> circle_area(1)  # doctest: +ROUND
    3.14
    """
    import math
    return math.pi * radius ** 2
```

### Fix 2: Use NORMALIZE_WHITESPACE for flexible formatting

```python
def get_matrix():
    """Return a 2x2 matrix.
    
    >>> get_matrix()  # doctest: +NORMALIZE_WHITESPACE
    [[1, 2],
     [3, 4]]
    """
    return [[1, 2], [3, 4]]

def format_table(data):
    """Format data as a table.
    
    >>> format_table(["a", "b"])  # doctest: +NORMALIZE_WHITESPACE
    'a\\tb'
    """
    return "\\t".join(data)
```

### Fix 3: Handle exception messages with ELLIPSIS

```python
def risky_operation(value):
    """Perform a risky operation.
    
    >>> risky_operation(-1)
    Traceback (most recent call last):
        ...
    ValueError: ...
    """
    if value < 0:
        raise ValueError(f"Negative value: {value}")
    return value * 2

def divide(a, b):
    """Divide two numbers.
    
    >>> divide(1, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError
    """
    return a / b
```

### Fix 4: Use SKIP directive for platform-dependent tests

```python
import sys
import os

def get_temp_dir():
    """Get the system temp directory.
    
    >>> result = get_temp_dir()  # doctest: +SKIP
    >>> os.path.exists(result)
    True
    """
    return os.path.join(os.path.dirname(__file__), "tmp")

def platform_specific():
    """Return platform info.
    
    >>> out = platform_specific()  # doctest: +SKIP
    >>> print("linux" in out.lower() or "windows" in out.lower())
    True
    """
    return sys.platform
```

### Fix 5: Use doctest runner with custom options

```python
import doctest
import mymodule

def run_tests():
    """Run doctests with custom options."""
    results = doctest.testmod(
        mymodule,
        verbose=False,
        optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    )
    print(f"Attempted: {results.attempted}, Failed: {results.failed}")
    return results.failed == 0

if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
```

## Examples

### Comprehensive docstring with multiple examples

```python
def fibonacci(n):
    """Generate Fibonacci sequence up to n terms.
    
    >>> fibonacci(0)
    []
    
    >>> fibonacci(1)
    [0]
    
    >>> fibonacci(5)
    [0, 1, 1, 2, 3]
    
    >>> fibonacci(10)  # doctest: +ELLIPSIS
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    >>> fibonacci(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be non-negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib
```

### Running doctests from a file

```python
# In your test script:
import doctest
import mymodule

if __name__ == "__main__":
    # Run all doctests in the module
    doctest.testmod(mymodule, verbose=True)
    
    # Or run doctests from a specific file
    doctest.testfile("examples.txt", module=mymodule)
```

### Using -m doctest from command line

```python
# Run from command line:
# python -m doctest mymodule.py -v
# python -m doctest examples.txt -v

# In mymodule.py:
def add(a, b):
    """Add two numbers.
    
    >>> add(2, 3)
    5
    
    >>> add(-1, 1)
    0
    """
    return a + b
```

## Related Errors

- [AssertionError](/languages/python/assertionerror/) — doctest failures are essentially assertion errors
- [IndentationError](/languages/python/indentationerror/) — whitespace issues in doctests
- [SyntaxError](/languages/python/syntaxerror/) — malformed code examples in doctests
