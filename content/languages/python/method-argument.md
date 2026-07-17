---
title: "[Solution] Python TypeError — Method Argument Issues"
description: "Fix Python TypeError related to method argument mismatches. Learn about self parameter errors, wrong argument counts, and method signature issues."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# TypeError — Method Argument Issues

A `TypeError` related to method arguments is raised when there is a mismatch between the arguments expected by a method and the arguments provided. This includes missing `self`, wrong argument counts, or incorrect argument types.

## Description

Methods in Python classes receive the instance (`self`) as the first argument automatically. Errors occur when `self` is explicitly passed, when methods are called with wrong argument counts, or when argument types don't match the method signature.

Common patterns:

- **Missing self parameter** — method defined without `self` as first parameter.
- **Explicitly passing self** — `obj.method(obj)` instead of `obj.method()`.
- **Wrong argument count** — calling a method with too many or too few arguments.
- **Positional vs keyword argument conflicts** — mixing argument styles incorrectly.

## Common Causes

```python
# Cause 1: Missing self in method definition
class MyClass:
    def greet():  # Missing self
        return "hello"

obj = MyClass()
obj.greet()  # TypeError: greet() takes 0 positional arguments but 1 was given

# Cause 2: Explicitly passing self
class MyClass:
    def greet(self):
        return "hello"

obj = MyClass()
obj.greet(obj)  # TypeError: greet() takes 1 positional argument but 2 were given

# Cause 3: Wrong argument count
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
calc.add(1)  # TypeError: add() missing 1 required positional argument: 'b'

# Cause 4: Passing keyword argument for positional-only parameter
class MyClass:
    def method(self, x, /, y):
        return x + y

obj = MyClass()
obj.method(x=1, y=2)  # TypeError: 'x' passes the formal parameter as positional
```

## Solutions

### Fix 1: Always include self as the first parameter

```python
# Wrong
class MyClass:
    def greet():  # Missing self
        return "hello"

# Correct
class MyClass:
    def greet(self):
        return "hello"
```

### Fix 2: Don't explicitly pass self

```python
# Wrong
class MyClass:
    def greet(self):
        return "hello"

obj = MyClass()
obj.greet(obj)  # TypeError

# Correct
obj.greet()
```

### Fix 3: Provide the correct number of arguments

```python
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()

# Wrong
calc.add(1)  # Missing argument

# Correct
calc.add(1, 2)  # Returns 3
```

### Fix 4: Use default arguments for optional parameters

```python
class MyClass:
    def greet(self, name="World"):
        return f"Hello, {name}!"

obj = MyClass()
obj.greet()  # "Hello, World!"
obj.greet("Alice")  # "Hello, Alice!"
```

### Fix 5: Use *args and **kwargs for flexible signatures

```python
class MyClass:
    def method(self, *args, **kwargs):
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")

obj = MyClass()
obj.method(1, 2, 3, key="value")
```

## Related Errors

- [TypeError](../typeerror) — general type mismatch errors.
- [AttributeError](../attributeerror) — object has no attribute.
- [Descriptor](descriptor) — descriptor-related errors.
