---
title: "[Solution] Python PicklingError — Object Cannot Be Pickled"
description: "Fix Python pickle.PicklingError when serializing objects. Learn which objects can be pickled and how to make custom objects picklable."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# PicklingError — Object Cannot Be Pickled

A `pickle.PicklingError` is raised when `pickle.dump()` or `pickle.dumps()` encounters an object that cannot be serialized. This includes objects with open file handles, lambda functions, generators, database connections, and other non-serializable resources.

## Description

Pickling is Python's serialization mechanism for converting objects to a byte stream. Not all objects can be pickled. Objects that hold system resources (file handles, sockets, locks), dynamic attributes, or certain built-in types cannot be serialized with pickle.

Common patterns:

- **Pickling file objects** — `pickle.dump(open("file.txt"), f)`.
- **Pickling lambda functions** — `pickle.dump(lambda x: x, f)`.
- **Pickling generators** — `pickle.dump((x for x in range(10)), f)`.
- **Pickling objects with __slots__** — missing `__getstate__`/`__setstate__`.
- **Pickling nested classes** — classes defined inside functions.

## Common Causes

```python
import pickle

# Cause 1: Pickling a file object
f = open("file.txt", "w")
pickle.dump(f, open("dump.pkl", "wb"))  # PicklingError: Cannot pickle file object

# Cause 2: Pickling a lambda function
func = lambda x: x * 2
pickle.dump(func, open("dump.pkl", "wb"))  # PicklingError: Can't pickle lambda

# Cause 3: Pickling a generator
gen = (x for x in range(10))
pickle.dump(gen, open("dump.pkl", "wb"))  # PicklingError: Can't pickle generator

# Cause 4: Pickling an object with unpicklable attributes
class MyClass:
    def __init__(self):
        self.connection = create_db_connection()

obj = MyClass()
pickle.dump(obj, open("dump.pkl", "wb"))  # PicklingError
```

## Solutions

### Fix 1: Implement __getstate__ and __setstate__

```python
import pickle

# Wrong
class MyClass:
    def __init__(self):
        self.connection = create_db_connection()

# Correct
class MyClass:
    def __init__(self):
        self.connection = create_db_connection()
        self.data = {}

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["connection"]  # Remove unpicklable attribute
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.connection = create_db_connection()  # Reconnect on unpickle

obj = MyClass()
pickle.dump(obj, open("dump.pkl", "wb"))
```

### Fix 2: Convert objects to picklable types

```python
import pickle

# Wrong — pickling a lambda
func = lambda x: x * 2
pickle.dump(func, open("dump.pkl", "wb"))

# Correct — use a named function
def multiply(x):
    return x * 2

pickle.dump(multiply, open("dump.pkl", "wb"))
```

### Fix 3: Use copyreg for custom reduction

```python
import pickle
import copyreg

class MyClass:
    def __init__(self, value):
        self.value = value

def reduce_myclass(obj):
    return (MyClass, (obj.value,))

copyreg.pickle(MyClass, reduce_myclass)

obj = MyClass(42)
pickle.dump(obj, open("dump.pkl", "wb"))
```

### Fix 4: Use alternatives to pickle

```python
# Wrong — pickling database connection
import pickle
conn = create_db_connection()
pickle.dump(conn, open("dump.pkl", "wb"))

# Correct — save connection parameters instead
config = {"host": "localhost", "port": 5432, "db": "mydb"}
pickle.dump(config, open("dump.pkl", "wb"))
```

## Related Errors

- [JSON encode](json-encode) — JSON serialization errors.
- [TypeError](../typeerror) — general type mismatch errors.
- [ValueError](../valueerror) — general value errors.
