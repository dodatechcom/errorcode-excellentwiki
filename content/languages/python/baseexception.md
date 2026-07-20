---
title: "[Solution] Python BaseException — Base Class for All Exceptions"
description: "Fix Python BaseException handling issues. Learn the exception hierarchy, catch-all patterns, and how SystemExit, KeyboardInterrupt, and GeneratorExit work."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 15
---

# Python BaseException — Base Class for All Exceptions

`BaseException` is the root of Python's exception hierarchy. Every built-in exception inherits from it, and catching it blindly can suppress critical system signals like `KeyboardInterrupt` and `SystemExit`.

## Common Causes

```python
# Cause 1: Catching BaseException suppresses KeyboardInterrupt
while True:
    try:
        user_input = input("Enter command: ")
    except BaseException:
        print("Something went wrong")
    # Ctrl+C is silently swallowed — program cannot be stopped

# Cause 2: Catching BaseException suppresses SystemExit
try:
    import sys
    sys.exit(0)
except BaseException:
    print("Caught everything")
    # sys.exit() never actually exits

# Cause 3: Catching BaseException hides GeneratorExit
def gen():
    try:
        yield 1
        yield 2
    except BaseException:
        print("Suppressed GeneratorExit — generator cannot close cleanly")
    yield 3

g = gen()
next(g)
g.close()  # GeneratorExit is caught, generator keeps running

# Cause 4: Using BaseException instead of Exception in a library
def process_data(items):
    try:
        return [transform(item) for item in items]
    except BaseException:
        return []  # Hides SystemExit, KeyboardInterrupt from callers

# Cause 5: Inheriting from BaseException directly in custom exceptions
class AppShutdown(BaseException):
    pass
    # Will not be caught by bare 'except Exception' blocks
```

## How to Fix

### Fix 1: Catch `Exception` instead of `BaseException`

```python
# Wrong — swallows SystemExit and KeyboardInterrupt
try:
    result = risky_operation()
except BaseException:
    result = None

# Correct — only catches application-level exceptions
try:
    result = risky_operation()
except Exception:
    result = None
```

### Fix 2: Handle SystemExit and KeyboardInterrupt separately

```python
import sys

try:
    main_loop()
except KeyboardInterrupt:
    print("Interrupted by user")
    sys.exit(130)
except SystemExit as e:
    print(f"Exiting with code {e.code}")
    sys.exit(e.code)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)
```

### Fix 3: Allow GeneratorExit to propagate through generators

```python
def resource_generator():
    resource = acquire_resource()
    try:
        while True:
            yield process(resource)
    finally:
        # Cleanup runs on GeneratorExit — do NOT catch BaseException here
        release_resource(resource)

# Closing the generator triggers clean shutdown
g = resource_generator()
next(g)
g.close()  # finally block runs, resource is released
```

### Fix 4: Use `except Exception` in library code

```python
# Library code should never hide system-level exceptions
def safe_fetch(url):
    try:
        return requests.get(url, timeout=5)
    except Exception as e:
        logging.error(f"Request failed: {e}")
        return None
        # KeyboardInterrupt and SystemExit propagate to caller
```

## Prevention Checklist

- Never catch `BaseException` unless you have a specific reason to intercept `SystemExit` or `KeyboardInterrupt`.
- Use `except Exception` for general error handling in application and library code.
- Do not inherit custom exceptions from `BaseException` unless they represent unrecoverable shutdown signals.
- Always let `GeneratorExit` propagate through generators — clean up resources in `finally` blocks instead.
- Test that `Ctrl+C` works in long-running scripts by verifying `KeyboardInterrupt` is not caught.

## Related Errors

- [Exception](/languages/python/exception/) — base class for all non-system-exiting exceptions.
- [KeyboardInterrupt](/languages/python/sys-exit/) — user presses Ctrl+C.
- [SystemExit](/languages/python/sys-exit/) — `sys.exit()` called.
- [GeneratorExit](/languages/python/generatorexit/) — generator or coroutine is closed.
