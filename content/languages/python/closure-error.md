---
title: "[Solution] Python UnboundLocalError — closure variable not bound"
description: "Fix Python UnboundLocalError in closures. Understand closure variable scope, nonlocal keyword, late binding closures, and loop variable capture."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 714
---

# Python UnboundLocalError — closure variable not bound

An `UnboundLocalError` in a closure occurs when a closure tries to use a variable that has been assigned to (making it local) but hasn't been assigned a value yet. This is common in nested functions where you try to modify an outer variable without using the `nonlocal` keyword, or in late-binding closures where the variable's value is captured at call time, not definition time.

## Common Causes

```python
# Cause 1: Assigning to a variable without nonlocal
def outer():
    x = 10
    def inner():
        x = 20  # This creates a new local variable
        print(x)
    inner()
    print(x)

outer()  # 20, then 10 — inner's x is local

# Cause 2: Using variable before assignment in closure
def outer():
    x = 10
    def inner():
        print(x)  # UnboundLocalError if x is assigned later
        x = 20
    inner()

outer()  # UnboundLocalError: local variable 'x' referenced before assignment

# Cause 3: Late-binding closure in a loop
functions = []
for i in range(5):
    functions.append(lambda: i)

# All functions return 4 — 'i' is bound at call time
print([f() for f in functions])  # [4, 4, 4, 4, 4]

# Cause 4: Modifying closure variable without nonlocal
def counter():
    count = 0
    def increment():
        count += 1  # UnboundLocalError: local variable referenced before assignment
        return count
    return increment

c = counter()
c()  # UnboundLocalError

# Cause 5: Conditional assignment in closure
def outer():
    x = 10
    def inner():
        if True:
            x = 20  # Makes x local
        print(x)  # UnboundLocalError if condition is False
    inner()

outer()  # 20 — but if condition were False, UnboundLocalError
```

## How to Fix

### Fix 1: Use the nonlocal keyword

```python
# Wrong
def counter():
    count = 0
    def increment():
        count += 1  # UnboundLocalError
        return count
    return increment

# Correct — use nonlocal
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

### Fix 2: Capture loop variables with default arguments

```python
# Wrong — late binding
functions = []
for i in range(5):
    functions.append(lambda: i)

print([f() for f in functions])  # [4, 4, 4, 4, 4]

# Correct — use default argument to capture value
functions = []
for i in range(5):
    functions.append(lambda i=i: i)

print([f() for f in functions])  # [0, 1, 2, 3, 4]
```

### Fix 3: Assign variable before using it in closure

```python
# Wrong
def outer():
    x = 10
    def inner():
        print(x)  # Works if x is not reassigned later
        x = 20  # Makes x local — UnboundLocalError above
    inner()

# Correct — assign after use, or use nonlocal
def outer():
    x = 10
    def inner():
        nonlocal x
        print(x)  # 10
        x = 20
    inner()
    print(x)  # 20

outer()
```

### Fix 4: Use a mutable container for closure state

```python
# Alternative to nonlocal — use mutable container
def counter():
    state = [0]
    def increment():
        state[0] += 1
        return state[0]
    return increment

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

## Examples

```python
# Real-world: Creating functions with different behaviors
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))  # 10
print(triple(5))  # 15

# Real-world: Event handlers in a loop
def create_handlers():
    handlers = []
    for i in range(3):
        handlers.append(lambda i=i: f"Handler {i}")
    return handlers

for handler in create_handlers():
    print(handler())  # Handler 0, Handler 1, Handler 2

# Real-world: Closure with nonlocal for configuration
def create_config():
    debug = False
    log_level = "INFO"

    def set_debug(value):
        nonlocal debug
        debug = value

    def set_log_level(level):
        nonlocal log_level
        log_level = level

    def get_config():
        return {"debug": debug, "log_level": log_level}

    return set_debug, set_log_level, get_config

set_debug, set_log_level, get_config = create_config()
print(get_config())  # {'debug': False, 'log_level': 'INFO'}
set_debug(True)
set_log_level("DEBUG")
print(get_config())  # {'debug': True, 'log_level': 'DEBUG'}
```

## Related Errors

- [UnboundLocalError](../unboundlocalerror) — general unbound local variable errors.
- [Local variable reference](local-variable-reference) — local variable scope issues.
- [NameError](../nameerror) — name not defined.
