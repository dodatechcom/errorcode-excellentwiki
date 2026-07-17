---
title: "[Solution] Python TypeError — Cannot Use Operator on Different Types"
description: "Fix Python TypeError: unsupported operand type(s). Learn why TypeErrors occur and how to fix them with type conversion and proper data handling."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# TypeError — Cannot Use Operator on Different Types

A `TypeError` is raised when an operation or function is applied to an object of inappropriate type. This is one of the most frequent errors in Python, often caused by mixing types in arithmetic, concatenation, or function calls without proper conversion.

## Description

The `TypeError` family covers several distinct failure modes:

- **Unsupported operand type(s)** — performing `+`, `-`, `*`, etc. on incompatible types (e.g., `int + str`).
- **Argument of type 'X' is not iterable** — using `in` on a non-iterable like an `int`.
- **'X' object is not callable** — treating a non-function (like a list or string) as a function by using parentheses `()`.
- **Can only concatenate 'str' (not 'int') to 'str'** — implicit string concatenation fails when types differ.
- **'NoneType' object has no attribute 'X'** — trying to call a method on `None`.

Python is strongly typed, so it refuses to guess how to convert between unrelated types. You must convert explicitly.

## Common Causes

```python
# Cause 1: Adding a string and an integer
result = "age: " + 25

# Cause 2: Using 'in' on a non-iterable
5 in 123

# Cause 3: Calling a non-callable object
my_list = [1, 2, 3]
my_list()

# Cause 4: Forgetting to convert before concatenation
name = "Alice"
print("Hello, " + name + ", you are " + age + " years old.")

# Cause 5: Method returns None but code treats it as a value
data = [3, 1, 2].sort()
print(data[0])
```

## Solutions

### Fix 1: Convert types explicitly before arithmetic

```python
# Wrong
result = "age: " + 25

# Correct — convert int to str
result = "age: " + str(25)

# Even better — use an f-string
result = f"age: {25}"
```

### Fix 2: Check for iterability before using 'in'

```python
# Wrong
5 in 123

# Correct — verify the value is iterable first
value = 123
if hasattr(value, '__iter__'):
    print(5 in value)
else:
    print("Cannot check membership on a non-iterable")
```

### Fix 3: Don't call non-callable objects

```python
# Wrong
my_list = [1, 2, 3]
my_list()

# Correct
my_list = [1, 2, 3]
print(len(my_list))
```

### Fix 4: Use f-strings to avoid concatenation pitfalls

```python
# Wrong
name = "Alice"
age = 25
print("Hello, " + name + ", you are " + age + " years old.")

# Correct
print(f"Hello, {name}, you are {age} years old.")
```

### Fix 5: Distinguish methods that mutate in place from those that return values

```python
# Wrong — .sort() sorts in place and returns None
data = [3, 1, 2].sort()
print(data[0])  # TypeError: 'NoneType' object is not subscriptable

# Correct — call sort() on the list, then use it
data = [3, 1, 2]
data.sort()
print(data[0])

# Alternative — use sorted() which returns a new list
data = sorted([3, 1, 2])
print(data[0])
```

## Related Errors

- [ValueError](../valueerror) — right type, wrong value (e.g., `int("abc")`).
- [AttributeError](../attributeerror) — object exists but doesn't have the requested attribute.
- [NameError](#) — variable or function name is not defined at all.
