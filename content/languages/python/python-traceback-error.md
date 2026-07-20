---
title: "[Solution] Python Traceback Error — Exception Formatting and Chaining Issues"
description: "Fix Python traceback errors by handling format_exc, print_exc, exception chaining (__context__), and traceback objects properly. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 210
---

# Python Traceback Error — Exception Formatting and Chaining Issues

Traceback errors occur when exception information is improperly formatted, lost, or chained. Common issues include losing traceback context when catching exceptions, incorrect use of exception chaining, and traceback formatting failures in logging or error reporting systems.

## Common Causes

```python
# Losing traceback when catching and re-raising
import traceback

def process():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        pass  # Exception is swallowed — no traceback preserved

process()  # Silent failure — no error output
```

```python
# Incorrect exception chaining
def fetch_data():
    try:
        result = open("nonexistent.txt").read()
    except FileNotFoundError as e:
        raise RuntimeError("Failed to fetch data")  # Loses original exception info

# RuntimeError: Failed to fetch data
# (original FileNotFoundError is not shown)
```

```python
# traceback.format_exc() called outside exception handler
import traceback

result = traceback.format_exc()  # Returns "NoneType: None" when no exception is active
print(result)  # NoneType: None
```

```python
# Traceback object reference cycle
import traceback
import sys

def create_cycle():
    try:
        raise ValueError("error")
    except:
        exc_info = sys.exc_info()
        # exc_info[2] is the traceback object — creates reference cycle if stored
        return exc_info  # Reference cycle: traceback -> frame -> local -> exc_info -> traceback

tb_info = create_cycle()
# Memory leak if traceback object is not explicitly deleted
```

```python
# format_list() with invalid frame info
import traceback

# Frame info tuples must have 4 elements
bad_frame = ("file.py", 10, "function")  # Missing line text
traceback.format_list([bad_frame])  # TypeError or incorrect output
```

## How to Fix

### Fix 1: Use proper exception chaining with `raise ... from`

```python
def fetch_data():
    try:
        result = open("nonexistent.txt").read()
    except FileNotFoundError as e:
        raise RuntimeError("Failed to fetch data") from e

try:
    fetch_data()
except RuntimeError as e:
    print(f"Error: {e}")
    print(f"Original cause: {e.__cause__}")
# Shows both the RuntimeError and the original FileNotFoundError
```

### Fix 2: Preserve tracebacks with `raise` or `traceback`

```python
import traceback

def process():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        # Option 1: Re-raise with original traceback
        raise
    
    # Option 2: Log the traceback
    # except ZeroDivisionError:
    #     traceback.print_exc()  # Prints full traceback to stderr

try:
    process()
except ZeroDivisionError:
    traceback.print_exc()
```

### Fix 3: Use traceback.format_exc() safely

```python
import traceback

def safe_format_exc():
    """Safely get current exception traceback."""
    return traceback.format_exc()

# Usage in exception handler
try:
    result = 1 / 0
except ZeroDivisionError:
    tb_str = safe_format_exc()
    print(f"Exception traceback:\n{tb_str}")

# Usage outside exception handler
tb_str = safe_format_exc()
print(f"No active exception: {tb_str}")  # Shows "NoneType: None"
```

### Fix 4: Chain exceptions correctly with `__context__` and `__cause__`

```python
# Implicit chaining (exception raised during handling)
def implicit_chain():
    try:
        open("missing.txt")
    except FileNotFoundError:
        raise ValueError("Invalid input")  # __context__ is set automatically

# Explicit chaining (raise ... from)
def explicit_chain():
    try:
        open("missing.txt")
    except FileNotFoundError as e:
        raise ValueError("Invalid input") from e  # __cause__ is set explicitly

# Suppress chaining
def suppress_chain():
    try:
        open("missing.txt")
    except FileNotFoundError:
        raise ValueError("Invalid input") from None  # No chaining shown

for func in [implicit_chain, explicit_chain, suppress_chain]:
    try:
        func()
    except ValueError as e:
        print(f"\n{func.__name__}:")
        print(f"  Exception: {e}")
        print(f"  __cause__: {e.__cause__}")
        print(f"  __context__: {e.__context__}")
```

### Fix 5: Format tracebacks for logging

```python
import traceback
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

def process_with_logging():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        # Log with full traceback
        logging.error(
            "An error occurred",
            exc_info=True  # Automatically includes traceback
        )
        
        # Or manually format
        tb_string = traceback.format_exception(*sys.exc_info())
        logging.debug("Formatted traceback: %s", "".join(tb_string))
        
        raise  # Re-raise after logging

try:
    process_with_logging()
except ZeroDivisionError:
    pass  # Exception was logged
```

## Examples

### Custom exception formatter

```python
import traceback
import sys
from datetime import datetime

class ExceptionFormatter:
    """Format exceptions for logging or display."""
    
    @staticmethod
    def format_exception(exc, include_locals=False):
        """Format exception with optional local variables."""
        tb = exc.__traceback__
        frames = []
        
        while tb is not None:
            frame = tb.tb_frame
            frame_info = {
                "file": tb.tb_frame.f_code.co_filename,
                "line": tb.tb_lineno,
                "function": tb.tb_frame.f_code.co_name,
            }
            
            if include_locals:
                frame_info["locals"] = {
                    k: repr(v)[:100]
                    for k, v in frame.f_locals.items()
                    if not k.startswith("_")
                }
            
            frames.append(frame_info)
            tb = tb.tb_next
        
        return {
            "timestamp": datetime.now().isoformat(),
            "type": type(exc).__name__,
            "message": str(exc),
            "frames": frames,
            "traceback": "".join(traceback.format_tb(exc.__traceback__)),
        }

def risky_operation():
    x = 42
    result = x / 0
    return result

try:
    risky_operation()
except Exception as e:
    formatted = ExceptionFormatter.format_exception(e, include_locals=True)
    print(f"Error Type: {formatted['type']}")
    print(f"Message: {formatted['message']}")
    print(f"Frames: {len(formatted['frames'])}")
```

### Safe exception context manager

```python
import traceback
import sys
from contextlib import contextmanager

@contextmanager
def exception_handler():
    """Context manager that logs exceptions and preserves traceback."""
    try:
        yield
    except Exception as e:
        tb_str = traceback.format_exception(type(e), e, e.__traceback__)
        print(f"Exception in context:\n{''.join(tb_str)}")
        raise  # Re-raise with preserved traceback

# Usage
with exception_handler():
    result = 1 / 0  # Exception is logged and re-raised
```

## Related Errors

- [RuntimeError](/languages/python/runtimeerror/) — general runtime failures
- [SyntaxError](/languages/python/syntaxerror/) — code that can't be parsed
- [RecursionError](/languages/python/recursionerror/) — deep recursion causing traceback stack overflow
