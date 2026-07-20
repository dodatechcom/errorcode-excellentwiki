---
title: "[Solution] Python NameError — Name Is Not Defined Fix"
description: "Fix Python NameError for undefined variables, scope issues, typos, and before-assignment errors. Debug variable scope and naming problems."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 23
---

# Python NameError — Name Is Not Defined Fix

A `NameError` is raised when Python encounters a name (variable, function, or class) that has not been defined in the current scope. This is one of the most common errors, often caused by typos, missing imports, or scope misunderstandings.

## Common Causes

```python
# Cause 1: Variable used before definition
print(greeting)  # NameError: name 'greeting' is not defined
greeting = "hello"

# Cause 2: Typo in variable name
user_name = "Alice"
print(username)  # NameError: name 'username' is not defined

# Cause 3: Variable defined in a different scope
def set_value():
    x = 10

print(x)  # NameError: name 'x' is not defined — x is local to set_value()

# Cause 4: Missing import
result = os.listdir(".")  # NameError: name 'os' is not defined

# Cause 5: Variable defined inside a conditional branch
if False:
    data = [1, 2, 3]

print(data)  # NameError: name 'data' is not defined
```

## How to Fix

### Fix 1: Define variables before using them

```python
# Wrong
print(message)  # NameError
message = "hello"

# Correct
message = "hello"
print(message)
```

### Fix 2: Check for typos in variable names

```python
# Wrong
user_name = "Alice"
print(user_Name)  # NameError — capital N

# Correct — use consistent naming (snake_case by convention)
user_name = "Alice"
print(user_name)
```

### Fix 3: Use global or pass variables as arguments for cross-function access

```python
# Wrong — x is local to set_value
def set_value():
    x = 10

print(x)  # NameError

# Correct — return the value
def set_value():
    return 10

x = set_value()
print(x)  # 10

# Alternative — use global (not recommended for most cases)
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # 1
```

### Fix 4: Import modules before using them

```python
# Wrong
print(os.listdir("."))  # NameError: name 'os' is not defined

# Correct
import os
print(os.listdir("."))

# Or import specific names
from os import listdir
print(listdir("."))
```

### Fix 5: Ensure variables are defined in all code paths

```python
# Wrong — data only defined when condition is True
if condition:
    data = fetch_data()

process(data)  # NameError if condition was False

# Correct
data = None
if condition:
    data = fetch_data()

if data is not None:
    process(data)
```

## Prevention Checklist

- Define all variables before their first use.
- Use your IDE's variable highlighting and linting to catch undefined names early.
- Import all required modules at the top of the file.
- Use `snake_case` consistently to avoid case-sensitivity typos.
- Initialize variables with default values when they might be skipped by conditionals.

## Related Errors

- [UnboundLocalError](/languages/python/unboundlocalerror/) — local variable referenced before assignment.
- [AttributeError](/languages/python/attributeerror/) — object exists but lacks the requested attribute.
- [ImportError](/languages/python/importerror/) — module exists but specific name cannot be imported.
- [ModuleNotFoundError](/languages/python/modulenotfounderror/) — module itself is missing.
