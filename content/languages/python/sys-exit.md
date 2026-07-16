---
title: "[Solution] Python SystemExit — Program Exit"
description: "Fix Python SystemExit when sys.exit() is called. Understand how SystemExit works and when it's expected vs unexpected."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["systemexit", "sys", "exit", "program"]
weight: 5
---

# SystemExit — Program Exit

A `SystemExit` exception is raised when `sys.exit()` is called. This is not an error but a deliberate way to terminate a Python program. It can be caught with `try/except`, which is useful for cleanup but should be done carefully.

## Description

`sys.exit()` raises `SystemExit` to signal program termination. The exception can carry an exit code: `sys.exit(0)` for success, non-zero for error. When caught, the program continues unless `sys.exit()` is called again. This is different from `os._exit()` which terminates immediately without cleanup.

Common patterns:

- **Explicit program exit** — `sys.exit(0)`.
- **Exit with error code** — `sys.exit(1)`.
- **Caught by except** — `try: sys.exit() except SystemExit:`.
- **Interactive interpreter** — `exit()` command raises SystemExit.

## Common Causes

```python
import sys

# Cause 1: Explicit sys.exit()
sys.exit(0)  # SystemExit

# Cause 2: Exit with error message
sys.exit("Error: something went wrong")  # SystemExit with message

# Cause 3: sys.exit() in a script
def main():
    print("Starting...")
    sys.exit(0)  # Program terminates here
    print("This never prints")

# Cause 4: Caught by try/except
try:
    sys.exit(0)
except SystemExit:
    print("SystemExit was caught — program continues!")
```

## Solutions

### Fix 1: Check exit code before catching

```python
import sys

try:
    sys.exit(1)
except SystemExit as e:
    if e.code != 0:
        print(f"Program exited with error: {e.code}")
        # Re-raise if you want to exit
        raise
```

### Fix 2: Use sys.exit() intentionally

```python
import sys

def main():
    try:
        run_program()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### Fix 3: Don't catch SystemExit unless necessary

```python
# Wrong — catching SystemExit hides exit calls
try:
    sys.exit(0)
except SystemExit:
    pass  # Program continues unexpectedly

# Correct — let SystemExit propagate
sys.exit(0)  # Program exits cleanly
```

### Fix 4: Use os._exit() for immediate termination

```python
import os

# sys.exit() — raises SystemExit, runs finally blocks
sys.exit(0)

# os._exit() — immediate termination, no cleanup
os._exit(0)
```

## Related Errors

- [KeyboardInterrupt](#) — user interrupt (Ctrl+C).
- [SystemExit](sys-exit) — related to program exit.
- [RuntimeError](../runtimeerror) — general runtime errors.
