---
title: "[Solution] Python ValueError — Bad Callable for Frame"
description: "Fix Python ValueError: bad callable for frame. Understand frame-related errors and how to resolve them in Python."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["valueerror", "frame", "callable", "function"]
weight: 5
---

# ValueError — Bad Callable for Frame

A `ValueError` with the message "bad callable for frame" is raised when you try to use an invalid callable with a frame object. This typically occurs when using `sys.settrace`, `sys.setprofile`, or similar frame-related functions with an incorrect callback.

## Description

Frame objects represent execution frames in Python. When you set trace or profile functions using `sys.settrace` or `sys.setprofile`, the callback must be a callable that accepts specific arguments. Passing a non-callable or a callable with the wrong signature causes this error.

Common patterns:

- **Passing None to settrace** — `sys.settrace(None)` is valid, but passing a non-callable is not.
- **Wrong callback signature** — trace functions must accept `(frame, event, arg)`.
- **Using setprofile with wrong arguments** — profile functions need specific signatures.
- **Passing a non-callable** — `sys.settrace("not a function")`.

## Common Causes

```python
import sys

# Cause 1: Passing a non-callable to settrace
sys.settrace("not a function")  # ValueError: bad callable for frame

# Cause 2: Wrong callback signature
def my_trace():  # Missing required arguments
    pass

sys.settrace(my_trace)  # ValueError or TypeError

# Cause 3: Passing a class instance without __call__
class NotCallable:
    pass

sys.settrace(NotCallable())  # ValueError

# Cause 4: Passing a built-in with wrong interface
sys.settrace(len)  # May cause errors — wrong signature
```

## Solutions

### Fix 1: Define a trace function with the correct signature

```python
import sys

# Wrong
def my_trace():
    pass

# Correct
def my_trace(frame, event, arg):
    print(f"Event: {event}")
    return my_trace  # Return the trace function for continuation

sys.settrace(my_trace)
```

### Fix 2: Use a lambda or callable with correct arguments

```python
import sys

# Wrong
sys.settrace(lambda: None)

# Correct
sys.settrace(lambda frame, event, arg: None)
```

### Fix 3: Check if the callback is callable before passing it

```python
import sys

callback = get_trace_function()  # Might not be callable

if callback is not None and callable(callback):
    sys.settrace(callback)
else:
    print("Invalid trace callback")
```

### Fix 4: Stop tracing when done

```python
import sys

def my_trace(frame, event, arg):
    return my_trace

# Start tracing
sys.settrace(my_trace)

# ... code to trace ...

# Stop tracing
sys.settrace(None)
```

## Related Errors

- [TypeError](../typeerror) — general type mismatch errors.
- [ValueError](../valueerror) — general value errors.
- [RecursionError](../recursionerror) — maximum recursion depth exceeded.
