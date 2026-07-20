---
title: "[Solution] Python Pdb Error — Debugger Breakpoints and Debugging Issues"
description: "Fix Python pdb errors by handling breakpoint(), set_trace() issues, post-mortem debugging, and pdb commands. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 206
---

# Python Pdb Error — Debugger Breakpoints and Debugging Issues

Pdb errors occur when breakpoints are placed in wrong contexts, the debugger can't attach to the running process, post-mortem debugging fails after exceptions, or pdb commands are used incorrectly. These issues disrupt the debugging workflow.

## Common Causes

```python
# breakpoint() in code without terminal access
def background_task():
    breakpoint()  # Raises BdbQuit or hangs in non-interactive contexts
    result = expensive_computation()
    return result

# Running in a subprocess, cron job, or web server — no terminal available
```

```python
# set_trace() in a threaded program
import threading
import pdb

def worker():
    pdb.set_trace()  # May interfere with other threads or cause deadlocks
    print("Working")

t = threading.Thread(target=worker)
t.start()
```

```python
# Post-mortem debugging after exception with no traceback
import pdb
import traceback

def broken_function():
    x = 1 / 0

try:
    broken_function()
except:
    pass  # Exception swallowed — no traceback to debug

# pdb.pm() fails: no active exception to debug
```

```python
# pdb commands fail due to incorrect syntax
# (pdb) p locals()  # SyntaxError in some contexts
# (pdb) continue     # Must use 'c' or 'continue' — typo causes error
# (pdb) step         # Must be at a function call to step into
```

```python
# Breakpoint disabled by environment variable
# PYTHONBREAKPOINT=0 python script.py
# All breakpoint() calls are silently disabled
```

## How to Fix

### Fix 1: Use breakpoint() with proper environment setup

```python
# Set PYTHONBREAKPOINT to enable/disable breakpoints
# export PYTHONBREAKPOINT=0          # Disable all breakpoints
# export PYTHONBREAKPOINT=pdb.set_trace  # Default behavior

def process_data(data):
    cleaned = data.strip()
    breakpoint()  # Only triggers when PYTHONBREAKPOINT is set
    return cleaned.upper()

# In Docker or remote servers, redirect pdb to a file:
# PYTHONBREAKPOINT="python3 -c \"import pdb; pdb.set_trace(open('/dev/null','w'))\"" \
#   python script.py
```

### Fix 2: Use post-mortem debugging correctly

```python
import pdb
import sys

def buggy_function():
    data = {"key": [1, 2, 3]}
    return data["missing"]

try:
    result = buggy_function()
except KeyError as e:
    print(f"KeyError: {e}")
    # Option 1: Use sys.exc_info() for proper traceback
    exc_type, exc_value, exc_tb = sys.exc_info()
    pdb.post_mortem(exc_tb)

# Option 2: Use the -m pdb flag from command line
# python -m pdb script.py
# After crash: pdb automatically enters post-mortem
```

### Fix 3: Use conditional breakpoints

```python
def find_issues(data):
    for i, item in enumerate(data):
        # Set conditional breakpoint: i == 50
        if i == 50:
            breakpoint()  # Only breaks when i reaches 50
        if item is None:
            continue
        process_item(item)

# Or use logging-based debugging as an alternative
import logging
logging.basicConfig(level=logging.DEBUG)

def find_issues_logged(data):
    for i, item in enumerate(data):
        logging.debug(f"Processing item {i}: {item}")
        if item is None:
            logging.warning(f"None at index {i}")
            continue
        process_item(item)
```

### Fix 4: Use remote pdb for non-interactive environments

```python
# Install remote-pdb: pip install remote-pdb

# In your code:
from remote_pdb import set_trace

def background_task():
    set_trace(host="0.0.0.0", port=4444)
    result = expensive_computation()
    return result

# Connect from another terminal:
# rdp -c 4444 localhost
```

### Fix 5: Use pdbpp for enhanced debugging

```python
# Install pdbpp: pip install pdbpp

import pdb

def complex_function(data):
    pdb.set_trace()  # pdbpp provides better output, tab completion
    result = transform(data)
    return result

# pdbpp features:
# - Syntax highlighting
# - Tab completion for locals/globals
# - Sticky mode (shows source code around current line)
# - Better pretty-printing
```

## Examples

### Using pdb in a test framework

```python
import unittest
import pdb

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        if result != 4:
            pdb.set_trace()  # Debug when test fails
        self.assertEqual(result, 4)
    
    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

# Or use pytest with pdb: pytest --pdb
```

### Custom debugger context manager

```python
import pdb
import contextlib
import sys

@contextlib.contextmanager
def debug_on_error():
    """Automatically enter debugger on exception."""
    try:
        yield
    except Exception:
        print("Exception occurred, entering debugger...")
        pdb.post_mortem(sys.exc_info()[2])
        raise

# Usage
with debug_on_error():
    x = 1 / 0  # Drops into pdb on ZeroDivisionError
```

### Debugging with traceback module

```python
import traceback
import pdb

def monitor_execution(func):
    """Decorator that enters pdb on exception."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            traceback.print_exc()
            pdb.post_mortem()
            raise
    return wrapper

@monitor_execution
def risky_function():
    data = [1, 2, 3]
    return data[10]  # IndexError — triggers debugger
```

## Related Errors

- [BdbQuit](/languages/python/bdbquit/) — debugger quit command
- [SyntaxError](/languages/python/syntaxerror/) — incorrect pdb command syntax
- [RuntimeError](/languages/python/runtimeerror/) — debugger can't attach in certain contexts
