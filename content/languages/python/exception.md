---
title: "[Solution] Python Exception — Base Class for All Application Exceptions"
description: "Fix Python Exception hierarchy issues. Learn how to create custom exceptions, use inheritance properly, and chain exceptions with cause syntax."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 16
---

# Python Exception — Base Class for All Application Exceptions

`Exception` is the base class for all built-in, non-system-exiting exceptions. It is the correct parent class for custom exceptions and the right type to catch for general error handling.

## Common Causes

```python
# Cause 1: Catching Exception too broadly hides bugs
def divide(a, b):
    try:
        return a / b
    except Exception:
        return 0
    # Hides ZeroDivisionError, TypeError, and every other bug

# Cause 2: Custom exception not inheriting from Exception
class MyError:
    pass

try:
    raise MyError("bad state")
except Exception:
    print("Not caught — MyError does not inherit from Exception")

# Cause 3: Swallowing exceptions without logging
def load_config(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return {}
        # Config errors are silently ignored

# Cause 4: Not chaining exceptions loses context
def parse_config(raw):
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid configuration") from e
        # Without 'from e', original error is lost

# Cause 5: Raising bare Exception instead of a specific type
def validate_age(age):
    if age < 0:
        raise Exception("Invalid age")  # Too generic — caller cannot distinguish
```

## How to Fix

### Fix 1: Catch the most specific exception type possible

```python
# Wrong
try:
    result = int(user_input)
except Exception:
    result = 0

# Correct
try:
    result = int(user_input)
except (ValueError, TypeError):
    result = 0
```

### Fix 2: Create custom exceptions that inherit from Exception

```python
class AppError(Exception):
    """Base exception for this application."""
    pass

class ConfigError(AppError):
    """Raised when configuration is invalid."""
    pass

class DatabaseError(AppError):
    """Raised when a database operation fails."""
    pass

# Callers can catch AppError for a broad handler, or specific subclasses
try:
    load_config("missing.json")
except ConfigError as e:
    print(f"Config problem: {e}")
except AppError as e:
    print(f"Application error: {e}")
```

### Fix 3: Always log exceptions before converting or suppressing

```python
import logging

def load_config(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning(f"Config file not found: {path}, using defaults")
        return {}
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON in {path}: {e}")
        return {}
```

### Fix 4: Use exception chaining to preserve context

```python
def process_order(order_data):
    try:
        validate(order_data)
    except ValidationError as e:
        # Chains the original error — accessible via __cause__
        raise ProcessingError(f"Order validation failed: {e}") from e
```

### Fix 5: Raise specific exception types instead of bare Exception

```python
# Wrong
def validate_age(age):
    if age < 0:
        raise Exception("Invalid age")

# Correct
def validate_age(age):
    if age < 0:
        raise ValueError(f"Age must be non-negative, got {age}")
```

## Prevention Checklist

- Inherit custom exceptions from `Exception`, not from `BaseException`.
- Use `except SpecificError` rather than `except Exception` whenever possible.
- Always chain exceptions with `raise NewError(...) from original_error` to preserve context.
- Log exceptions before returning fallback values so bugs are not silently swallowed.
- Raise specific, descriptive exception types instead of bare `Exception`.

## Related Errors

- [BaseException](/languages/python/baseexception/) — root of the exception hierarchy.
- [ValueError](/languages/python/valueerror/) — correct type but wrong value.
- [TypeError](/languages/python/typeerror/) — wrong type for an operation.
- [RuntimeError](/languages/python/runtimeerror/) — generic runtime failure.
