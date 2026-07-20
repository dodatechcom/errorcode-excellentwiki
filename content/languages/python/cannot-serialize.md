---
title: "[Solution] Python TypeError — cannot serialize object"
description: "Fix Python TypeError: cannot serialize object. Handle pickle failures, JSON encoding of custom objects, and multiprocessing serialization issues."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 702
---

# Python TypeError — cannot serialize object

A `TypeError` with the message `cannot serialize object` is raised when Python encounters an object that cannot be converted to a byte stream or other serializable format. This commonly occurs with `pickle`, `json.dumps()`, and `multiprocessing` when objects like file handles, lambda functions, generators, or custom objects without proper serialization support are passed.

## Common Causes

```python
import pickle
import json

# Cause 1: Pickling a file object
f = open("data.txt", "w")
pickle.dump(f, open("dump.pkl", "wb"))  # TypeError: cannot serialize object

# Cause 2: JSON encoding a custom object
class User:
    def __init__(self, name):
        self.name = name

user = User("Alice")
json.dumps(user)  # TypeError: Object of type User is not JSON serializable

# Cause 3: Multiprocessing with unpicklable arguments
from multiprocessing import Process

def worker(conn):
    print(conn)

conn = create_connection()  # Database connection
p = Process(target=worker, args=(conn,))  # TypeError: cannot pickle connection

# Cause 4: Pickling a lambda function
func = lambda x: x + 1
pickle.dumps(func)  # TypeError: cannot pickle function

# Cause 5: Pickling nested classes defined in closures
def make_class():
    class Inner:
        pass
    return Inner

MyClass = make_class()
pickle.dumps(MyClass())  # TypeError: cannot serialize
```

## How to Fix

### Fix 1: Implement __reduce__ for pickle serialization

```python
import pickle

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __reduce__(self):
        return (User, (self.name, self.age))

user = User("Alice", 30)
data = pickle.dumps(user)  # Works
restored = pickle.loads(data)
print(restored.name)  # Alice
```

### Fix 2: Implement a custom JSON encoder

```python
import json
from datetime import datetime

class User:
    def __init__(self, name, created_at):
        self.name = name
        self.created_at = created_at

class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {"name": obj.name, "created_at": obj.created_at.isoformat()}
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

user = User("Alice", datetime.now())
data = json.dumps(user, cls=UserEncoder)
print(data)  # {"name": "Alice", "created_at": "2024-01-01T12:00:00"}
```

### Fix 3: Use connection parameters instead of connection objects for multiprocessing

```python
from multiprocessing import Process

# Wrong — passing connection object
def worker(conn):
    print(conn)

# Correct — pass connection parameters
def worker(config):
    conn = create_connection(config["host"], config["port"])
    print(conn)

config = {"host": "localhost", "port": 5432}
p = Process(target=worker, args=(config,))
p.start()
p.join()
```

### Fix 4: Use dill for advanced serialization

```python
import dill

# dill can serialize lambdas, closures, and more
func = lambda x: x + 1
data = dill.dumps(func)       # Works
restored = dill.loads(data)
print(restored(5))            # 6

# dill can also serialize nested classes
def make_class():
    class Inner:
        pass
    return Inner

MyClass = make_class()
data = dill.dumps(MyClass())  # Works
```

## Examples

```python
# Real-world: Serializing a Pandas DataFrame for multiprocessing
import pandas as pd
from multiprocessing import Process

def process_data(df_dict):
    df = pd.DataFrame(df_dict)
    print(df.mean())

# Wrong — DataFrames can sometimes fail with pickle
df = pd.DataFrame({"a": [1, 2, 3]})

# Correct — convert to dict for safe serialization
p = Process(target=process_data, args=(df.to_dict(),))
p.start()
p.join()

# Real-world: JSON API with custom response objects
from dataclasses import dataclass, asdict
import json

@dataclass
class ApiResponse:
    status: int
    message: str
    data: dict

response = ApiResponse(200, "OK", {"users": 100})

# Correct — use dataclasses.asdict
data = json.dumps(asdict(response))
print(data)  # {"status": 200, "message": "OK", "data": {"users": 100}}
```

## Related Errors

- [PicklingError](pickling-error) — pickle-specific serialization failures.
- [JSON encode](json-encode) — JSON serialization errors.
- [TypeError](../typeerror) — general type mismatch errors.
